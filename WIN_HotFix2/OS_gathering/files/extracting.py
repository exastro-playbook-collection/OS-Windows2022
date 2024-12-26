import re
import json
import sys
import os

# 以下のの四つ方法により、順番にWindowsUpdate情報を採取してマッジすることを実装する。
# 方法１：
#　レジストリ「HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall」から
#　インストールしたソフトウェアの更新プログラム一覧を採取する。
# 方法２：
# 　Get-HotFix命令によりCBSで提供されたWindows Update情報を採取する。
# 方法３：
# 　Microsoft.Update.SessionというCOMオブジェクトを使用する方法によりWindows更新履歴情報から
# 　Windows更新一覧情報を採取する。
# 方法４：
# 　レジストリ「HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing
# 　\Packages」からCBSで提供されたWindows Update情報を採取する。

# データが重複した場合、上記のように全て残すのではなく優先順方法１→方法２→方法３→方法４で優先度の高い情報を残している。


class Data_processing:
    def __init__(self) -> None:
        """
        方法３では、有効な情報を抽出するための情報
        ・KB_REGEX：採取したTitle情報からHotfixID情報を抽出する。
        ・operation_codesは1または3である場合、抽出対象とする。
        """
        self.KB_REGEX = re.compile(r"KB[0-9]{5,7}", re.IGNORECASE)
        self.operation_codes = {1: "Installed", 2: "uninstall", 3: "other"}

        """
        方法４では、CurrentStateの値の一覧は下記の通りである。
        その中に、112または128である場合、正しくインストール済みのプログラム更新と認識して、採取する。
        """
        self.states = {
            0: "Absent",
            5: "Uninstall Pending",
            16: "Resolving",
            32: "Resolved",
            48: "Staging",
            64: "Staged",
            80: "Superseeded",
            96: "Install Pending",
            101: "Partially Installed",
            112: "Installed",
            128: "Permanent",
        }
    """
    コンテンツ中のkeyの値に基づいて分類処理を行う
    """

    def recognition(self, stdout: list):
        if 'HotFixID' in stdout[0].keys():
            # 方法２により採取情報の処理
            return self.processing_hotfix(stdout)

        elif 'KBNumber' in stdout[0].keys():
            # 方法１により採取情報の処理
            return self.processing_Uninstall(stdout)

        elif 'InstallName' in stdout[0].keys():
            # 方法４により採取情報の処理
            return self.processing_package(stdout)

        elif 'Title' in stdout[0].keys():
            # 方法３により採取情報の処理
            return self.processing_msupdate(stdout)

    """
    方法１により採取情報の処理：
    　命令により採取された情報：    　　DisplayName,DisplayVersion,KBNumber,PatchType
            DisplayName：パッチ名
            DisplayVersion：バージョン番号 
            KBNumber：パッチ番号
            PatchType：パッチの種類
      dict_message：出力用情報
      　　　DisplayName：　←　採取したDisplayNameを設定
      　　　DisplayVersion：　←　採取したDisplayVersionを設定
      　　　HotFixID：　←　採取したKBNumberを設定
      　　　HotFixType：　←　採取したPatchTypeを設定
      　　　InstallState：　←　採取できないので、常にnull
    """

    def processing_Uninstall(self, stdout: list):
        uninstall_list = []
        for std in stdout:
            dict_message = {"HotFixID": None, "HotFixType": None,
                            "DisplayName": None, "DisplayVersion": None, "InstallState": None}
            dict_message['DisplayName'] = std['DisplayName']
            dict_message['HotFixID'] = std['KBNumber']
            dict_message['HotFixType'] = std['PatchType']
            dict_message['DisplayVersion'] = std['DisplayVersion']
            uninstall_list.append(dict_message)

        return uninstall_list

    """
    方法２により採取情報の処理：
    　命令により採取された情報：　HotFixID,Description
    　　   HotFixID：パッチ番号
    　　   Description:パッチの種類
      dict_message：出力用情報
      　　　DisplayName：　←　採取できないので、常にnull
      　　　DisplayVersion：　←　採取できないので、常にnull
      　　　HotFixID：　←　採取したHotFixIDを設定
      　　　HotFixType：　←　採取したDescriptionを設定
      　　　InstallState：　←　採取できないので、常にnull
    """

    def processing_hotfix(self, stdout: list):
        hotfix_list = []
        for std in stdout:
            dict_message = {"HotFixID": None, "HotFixType": None,
                            "DisplayName": None, "DisplayVersion": None, "InstallState": None}
            dict_message['HotFixID'] = std['HotFixID']
            dict_message['HotFixType'] = std['Description']
            hotfix_list.append(dict_message)
        return hotfix_list

    """
    方法３により採取情報の処理：
    　命令により採取された情報：Title,Operation,ResultCode
    　　   Title：更新プログラムの説明文字(パッチ番号が含まれています)
    　　   Operation：更新プログラムに関する操作　1: "Installed", 2: "uninstall", 3: "other"
    　　   ResultCode：操作実行結果　1: in process, 2: succeeded, 3: succeeded with errors, 4: failed, 5: aborted
      dict_message：出力用情報
      　　　DisplayName：　←　採取したTitleを設定
      　　　DisplayVersion：　←　採取できないので、常にnull
      　　　HotFixID：　←　採取したTitleから正規表現により抽出したHotFixIDを設定
      　　　HotFixType：　←　採取できないので、常にnull
      　　　InstallState：　←採取したOperation を設定 
    """

    def processing_msupdate(self, stdout: list):
        msupdate_list = []
        for std in stdout:
            dict_message = {"HotFixID": None, "HotFixType": None,
                            "DisplayName": None, "DisplayVersion": None, "InstallState": None}
            # 収集されたOperationとResultCodeがnullであることを防止
            if std['Operation'] and std['ResultCode']:
                # Operation=1はインストール、Operation=3はその他、ResultCode=2は成功，条件適合で処理
                if (int(std['Operation']) == 1 or int(std['Operation']) == 3) and int(std['ResultCode']) == 2:
                    # self.operation_codes対応情報の取得 Operation=1はインストール、Operation=3はその他
                    dict_message['InstallState'] = self.operation_codes[int(
                        std['Operation'])]
                    name = std['Title']
                    dict_message['DisplayName'] = name
                    # 使バージョン番号正則を使用して名前の内容を照合してパッチ番号を取得
                    kb = self.KB_REGEX.search(name)
                    # 正規一致エラーの防止
                    try:
                        dict_message['HotFixID'] = kb.group(0)
                    except:
                        dict_message['HotFixID'] = None
                    msupdate_list.append(dict_message)
                else:
                    continue
            else:
                continue
        return msupdate_list

    """
    方法４により採取された情報の処理：
    　命令により採取された情報：InstallName,CurrentState
    　　　　InstallName：更新プログラムのパッケージ情報（パッチ番号、バージョン番号が含まれています）
    　　　　CurrentState：更新動作の実行結果
      dict_message：出力用情報
      　　　DisplayName：　←　採取したInstallNameを設定
      　　　DisplayVersion：　←　採取したInstallNameから正規表現により抽出したバージョン情報を設定
      　　　HotFixID：　←　採取したInstallNameから正規表現により抽出したHotFixIDを設定
      　　　HotFixType：　←　採取できないので、常にnull
      　　　InstallState：　←　採取できないので、常にnull 
    """

    def processing_package(self, stdout: list):
        cbspackage_list = []
        for std in stdout:
            dict_message = {"HotFixID": None, "HotFixType": None,
                            "DisplayName": None, "DisplayVersion": None, "InstallState": None}
            name = std["InstallName"]
            dict_message['DisplayName'] = name
            kb = self.KB_REGEX.search(name)
            version_re = re.compile(r'\d+\.(?:\d+\.)*\d+', re.IGNORECASE)
            version = version_re.search(name)
            # 正規一致エラーの防止
            try:
                # 正規一致パッチ番号
                dict_message['HotFixID'] = kb.group(0)
            except:
                dict_message['HotFixID'] = None
            # 正規一致エラーの防止
            try:
                # 正規一致バージョン番号
                dict_message['DisplayVersion'] = version.group(0)
            except:
                dict_message['DisplayVersion'] = None
            if std['CurrentState']:
                # self.states対応情報の取得 CurrentState=112はインストール，CurrentState=128アンインストール不可
                dict_message["InstallState"] = self.states[int(
                    std['CurrentState'])]
            else:
                dict_message["InstallState"] = None
            cbspackage_list.append(dict_message)
        return cbspackage_list

    """
    HotFixIDが重なるものを削除する。
    """

    def iteration_rearrangement(self, update_list):
        truth_list_all = []
        kb_list = []
        for value in update_list:
            if value['HotFixID'] != None and value['HotFixID'] not in kb_list:
                kb_list.append(value['HotFixID'])
                truth_list_all.append(value)
            elif value['HotFixID'] == None:
                truth_list_all.append(value)
        return truth_list_all


"""
データ処理の主処理
"""
args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

target_filepath_list = []
update_list = []
file_number_id = 0

# ファイルパスが存在するかどうかを判断し、存在する場合はリストにファイルパスを追加します。
while os.path.exists(path + '/command' + '/{}/stdout.txt'.format(file_number_id)):
    target_filepath_list.append('/{}/stdout.txt'.format(file_number_id))
    file_number_id += 1

# 各方法採取した情報の処理
processing = Data_processing()
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    # ファイルかどうかを判断し、ファイルが0より大きい
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                #  複数レコード
                processing_data = processing.recognition(reader)
            else:
                #　一つレコード
                rows = []
                rows.append(reader)
                processing_data = processing.recognition(rows)
            for update_data in processing_data:
                update_list.append(update_data)
# 重なるレコードの処理
result_filedata_list_all = processing.iteration_rearrangement(update_list)
result = {}
target_parameter_root_key = 'VAR_WIN_HotFix2'
result[target_parameter_root_key] = result_filedata_list_all
print(json.dumps(result))
