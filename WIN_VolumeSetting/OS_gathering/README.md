Ansible Role: OS-Windows2022/WIN_VolumeSetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関するディスク管理についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_VolumeSetting/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_VolumeSetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_VolumeSetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_VolumeSetting` |     | 
| `- HealthStatus` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「記憶域」「ディスクの管理」の「状態」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DriveType` | ドライブ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DriveLetter` | システム内のドライブまたはボリュームを識別するために使用される文字 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FileSystem` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「記憶域」「ディスクの管理」の「ファイルシステム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FileSystemLabel` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「記憶域」「ディスクの管理」の「ボリューム」に該当  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Size` | ドライブサイズ (byte) | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SizeRemaining` | ドライブ空き容量 (byte) | 

### Example
~~~
VAR_WIN_VolumeSetting:
- DriveLetter: C
  DriveType: Fixed
  FileSystem: NTFS
  FileSystemLabel: ''
  HealthStatus: Healthy
  Size: 32210153472
  SizeRemaining: 15508439040
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
    │         └── WIN_VolumeSetting/
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
    - role: OS-Windows2022/WIN_VolumeSetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_VolumeSetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_VolumeSetting.yml  # パラメータ
~~~

# Remarks
-------
取得パラメタの値によっては、時間経過で動的に値が変わるものがあります。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
