Ansible Role: OS-Windows2022/WIN_InternetOption/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関するインターネットオプションでセキュリティ（SSL 3.0、TLS 1.0、TLS 1.1、TLS 1.2、TLS 1.3）の情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_InternetOption/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_InternetOption.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_InternetOption.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_InternetOption` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SecureProtocols` | 「コントロール パネル」「すべてのコントロール パネル項目」「インターネット オプション」「詳細設定」「SSL 3.0を使用する/TLS 1.0を使用する/TLS 1.1の使用/TLS 1.2の使用/TLS 1.3の使用」に該当<br>0： すべて選択しない<br>32： 「SSL 3.0を使用する」を選択する<br>128： 「TLS 1.0を使用する」を選択する<br>512： 「TLS 1.1の使用」を選択する<br>2048： 「TLS 1.2の使用」を選択する<br>8192 ： 「TLS 1.3の使用」を選択する<br>160： 「SSL 3.0を使用する,TLS 1.0を使用する」を選択する<br>544： 「SSL 3.0を使用する,TLS 1.1の使用」を選択する<br>2080： 「SSL 3.0を使用する,TLS 1.2の使用」を選択する<br>8224： 「SSL 3.0を使用する,TLS 1.3の使用」を選択する<br>640： 「TLS 1.0を使用する,TLS 1.1の使用」を選択する<br>2176： 「TLS 1.0を使用する,TLS 1.2の使用」を選択する<br>8320： 「TLS 1.0を使用する,TLS 1.3の使用」を選択する<br>2560： 「TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8704： 「TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10240： 「TLS 1.2の使用,TLS 1.3の使用」を選択する<br>672： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用」を選択する<br>2208： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.2の使用」を選択する<br>8352： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.3の使用」を選択する<br>2592： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8736： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10272： 「SSL 3.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>2688： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8832： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10368： 「TLS 1.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10752： 「TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>2720： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8864： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10400： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10784： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10880： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10912： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」すべてを選択する | 

### Example
~~~
VAR_WIN_InternetOption:
  SecureProtocols: 2048
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
    │         └── WIN_InternetOption/
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
    - role: OS-Windows2022/WIN_InternetOption/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_InternetOption/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_InternetOption.yml  # パラメータ
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
    - role: OS-Windows2022/WIN_InternetOption/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_InternetOption.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
~~~

# Remarks
-------
レジストリキーが存在しないパラメタの値はnullとして取得されます。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
