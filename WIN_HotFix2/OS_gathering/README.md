Ansible Role: OS-Windows2022/WIN_HotFix2/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関する更新とインストールされたプログラム一覧についての情報の取得を行います。
下記の４つの方法でHotFix情報を収集するので、同じHotFix情報が複数手段で採取できた場合、下記の優先順位で優先度の高い情報を残しています。
- 方法一
  レジストリ「HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall」からインストールしたソフトウェアの更新プログラム一覧を採取します。
- 方法二
  Get-HotFix命令によりCBSで提供されたWindows Update情報を採取します。
- 方法三
  Microsoft.Update.SessionというCOMオブジェクトを使用する方法によりWindows更新履歴情報からWindows更新一覧情報を採取します。
- 方法四
  レジストリ「HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages」からCBSで提供されたWindows Update情報を採取します。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_HotFix2/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_HotFix2.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_HotFix2.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description |
| ---- | ----------- |
| `VAR_WIN_HotFix2` |     |
| `- DisplayName`                          | 更新プログラムの名<br>null ： 収集できない場合<br>更新したプログラムの名 ： 収集したDisplayName、TitleまたはInstallName  |
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayVersion` | 更新プログラムの版数<br>null ： 収集できない場合<br>更新したプログラムの版数 ： 収集したInstallNameの版数  |
| &nbsp;&nbsp;&nbsp;&nbsp;`HotFixID`       | 更新プログラムファイルのHotFixID<br>更新したプログラムファイルのHotFixID ： 収集したKBNUMBER  |
| &nbsp;&nbsp;&nbsp;&nbsp;`HotFixType`     | 更新プログラムのタイプ<br>null ： 収集できない場合<br>更新したプログラムのタイプ ： 収集したPatchtypeまたはDescription |
| &nbsp;&nbsp;&nbsp;&nbsp;`InstallState`   | 更新プログラムのインストール状態<br>null ： 収集できない場合<br>Installed ： インストールされた<br>Permanent ： アンインストールできない <br>other ： その他  |

### Example
~~~
VAR_WIN_HotFix2:
- DisplayName: SQL Server 2017 の修正プログラム 3421 (KB5006944) (64-bit)
  DisplayVersion: 14.0.3421.10
  HotFixID: KB5006944
  HotFixType: SmallUpdateQFE
  InstallState: null
- DisplayName: null
  DisplayVersion: null
  HotFixID: KB4483452
  HotFixType: Update
  InstallState: null
- DisplayName: Windows 用セキュリティ更新プログラム (KB5003711)
  DisplayVersion: null
  HotFixID: KB5003711
  HotFixType: null
  InstallState: Installed
- DisplayName: Package_1000_for_KB4489899~31bf3856ad364e35~amd64~~10.0.1.11.mum
  DisplayVersion: 10.0.1.11
  HotFixID: KB4489899
  HotFixType: null
  InstallState: Installed
・・・
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
    │         └── WIN_HotFix2/
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
    - role: OS-Windows2022/WIN_HotFix2/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_HotFix2/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_HotFix2.yml  # パラメータ
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
