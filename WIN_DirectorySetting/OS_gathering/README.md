Ansible Role: OS-Windows2022/WIN_DirectorySetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関するディレクトリ設定についての情報の取得を行います。

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
| `VAR_OS_gathering_dir_path_recurse` | #- 'C:\Users\Public'<br>配列で設定 | ディレクトリ情報を再帰的に取得するディレクトリパス  | 
| `VAR_OS_gathering_dir_path` | #- 'C:\Users\Public'<br>配列で設定  | ディレクトリ情報を再帰的に取得しないディレクトリパス | 

# Results

本ロールの出力について説明します。

## ディレクトリ情報を取得する方法
- roles/OS-Windows2022/WIN_DirectorySetting/OS_gathering/defaults/main.ymlに以下のように設定

~~~
VAR_OS_gathering_dir_path_recurse:
 - 'C:\Test\test01'

VAR_OS_gathering_dir_path:
 - 'C:\Test\test02'
~~~

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_DirectorySetting/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_DirectorySetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_DirectorySetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_DirectorySetting` |     | 
| `- Name` | ディレクトリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AccessToString` | エクスプローラーでフォルダ選択「プロパティ」「セキュリティ」「詳細設定」「アクセス許可エントリ」の「種類」+「プリンシバル」+「アクセス」に該当<br>構築で使用できないため変更できない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Owner` | エクスプローラーでフォルダ選択「プロパティ」「セキュリティ」「詳細設定」の「所有者」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Encrypt` | 暗号化<br>E ： 暗号化されている<br>U ： 暗号化されていない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築のアクション設定値<br>directory ： ディレクトリの作成、更新<br>absent ： ディレクトリの削除 | 

### Example
~~~
VAR_WIN_DirectorySetting:
- AccessToString:
  - CREATOR OWNER Allow  268435456
  - NT AUTHORITY\SYSTEM Allow  268435456
  - NT AUTHORITY\SYSTEM Allow  FullControl
  - BUILTIN\Administrators Allow  FullControl
  - BUILTIN\Administrators Allow  268435456
  ・・・
  Action: directory
  Encrypt: U
  Name: C:\Windows\Temp
  Owner: NT AUTHORITY\SYSTEM
- AccessToString:
  - BUILTIN\Users Allow  CreateFiles, AppendData, ExecuteFile, Synchronize
  - NT SERVICE\TrustedInstaller Allow  FullControl
  - NT SERVICE\TrustedInstaller Allow  268435456
  - NT AUTHORITY\SYSTEM Allow  FullControl
  - NT AUTHORITY\SYSTEM Allow  268435456
  ・・・
  Action: directory
  Encrypt: U
  Name: C:\Windows\Temp\Amazon
  Owner: BUILTIN\Administrators
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
    │         └── WIN_DirectorySetting/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering_definition_copy.yml
    │                   │      gathering_definition_set.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition_base.yml
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
    - role: OS-Windows2022/WIN_DirectorySetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_DirectorySetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_DirectorySetting.yml  # パラメータ
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
    - role: OS-Windows2022/WIN_DirectorySetting/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_DirectorySetting.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
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
