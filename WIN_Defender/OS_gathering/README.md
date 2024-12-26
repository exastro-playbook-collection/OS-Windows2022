Ansible Role: OS-Windows2022/WIN_Defender/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関するWindowsDefender設定についての情報の取得を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11.0 以上 (動作確認バージョン [core 2.11.12])
  * Python バージョン 3.x  (動作確認バージョン 3.6.8)
- 管理対象マシン
  * Windows Server 2022

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2022
  * Powershell3.0+

# Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_Defender/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        └── command/
                               ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_Defender.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_Defender.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_Defender` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableRealtimeMonitoring` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「リアルタイム保護」に該当<br>false ： オン<br>true ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MAPSReporting` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「クラウド提供の保護」に該当<br>2 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SubmitSamplesConsent` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「サンプルの自動送信」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`EnableControlledFolderAccess` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ランサムウェアの防止」の「ランサムウェア防止の管理」「コントロールされたフォルダーアクセス」に該当<br>1 ： オン<br>0 ： オフ<br>※ OSのビルドバージョンによって取得/反映が行えない場合があります | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableEnhancedNotifications` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」の「情報提供の通知を受け取る」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SummaryNotificationDisabled` | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「最近のアクティビティとスキャン結果」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NoActionNotificationDisabled` | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「脅威が見つかりましたが、直ちに対処する必要性はありません」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FilesBlockedNotificationDisabled` | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「ファイルまたはアクティビティがブロックされています」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallPublicProfileNotice` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「ドメイン ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallStandardProfileNotice` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「プライベート ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallDomainProfileNotice` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「パブリック ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SmartScreenEnabled` | 「Windows セキュリティ」「アプリとブラウザーコントロール」の「アプリとファイルの確認」に該当<br>Warn ： オン<br>Off ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BlockApps` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「アプリとブラウザー　コントロール」「評価ベースの保護設定」「望ましくない可能性のあるアプリのブロック」「アプリをブロックする」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BlockDownloads` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「アプリとブラウザー　コントロール」「評価ベースの保護設定」「望ましくない可能性のあるアプリのブロック」「ダウンロードをブロックする」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ApplicationBlock` | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「アプリとブラウザー　コントロール」「評価ベースの保護設定」「望ましくない可能性のあるアプリのブロック」に該当<br>1 ： オン<br>0 ： オフ | 

### Example
~~~
VAR_WIN_Defender:
  DisableEnhancedNotifications: 0
  DisableRealtimeMonitoring: false
  EnableControlledFolderAccess: 0
  FilesBlockedNotificationDisabled: 0
  FireWallDomainProfileNotice: 1
  FireWallPublicProfileNotice: 1
  FireWallStandardProfileNotice: 1
  MAPSReporting: 2
  NoActionNotificationDisabled: 0
  SmartScreenEnabled: 'Off'
  SubmitSamplesConsent: 1
  SummaryNotificationDisabled: 0
  BlockApps: 0
  BlockDownloads: 0
  ApplicationBlock: 0
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2022
    │         └── WIN_Defender/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_Defender/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_Defender/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_Defender.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_Defender/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_Defender.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
~~~

# Remarks
-------
Windows Defenderをインストールしていない場合は、本ロール実行時にエラーとなるため実行しないでください。<br>
レジストリキーが存在しないパラメタの値はnullとして取得されます。<br>
<br>
変数説明に該当する内容は、OSエディションによって、内容が変わる場合があります。<br>

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
