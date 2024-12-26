Ansible Role: OS-Windows2022/WIN_Reboot/OS_build 
=======================================================

## Description
本ロールは、Windows Server 2022に関するOSの再起動、シャットダウンおよびサービスの再起動についての情報の設定を行います。
以下の用途で使用することができます。
* 単独で行いたい場合
* 複数のロールを呼び出し、それぞれで再起動またはシャットダウンが必要になる可能性があるが、再起動またはシャットダウンは最後に一度だけ行えば良い場合

## Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL8）
  * Ansible バージョン 2.11.0 以上 (動作確認バージョン [core 2.11.12])
  * Python バージョン 3.x  (動作確認バージョン 3.6.8)
- 管理対象マシン
  * Windows Server 2022

## Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2022
  * Powershell3.0+

# Dependencies

本ロールでは、他のロールは必要ありません。

## Role Variables
本ロールで指定できる変数値について説明します。

### Mandatory variables

ロール利用時に以下の変数値を指定する必要があります。

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_WIN_Reboot` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`restarted_services` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 指定されたサービスを再起動する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`reboot_requires` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | OSを再起動するフラグ<br>true: OSを再起動する<br>false: OSを再起動しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`shutdown_requires` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | OSをシャットダウンするフラグ<br>true: OSをシャットダウンする<br>false: OSをシャットダウンしない | 

### Example
~~~
VAR_WIN_Reboot:
  restarted_services:
    - ALG
    - AppMgmt
  reboot_requires: true
  shutdown_requires: false

~~~
### Optional variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

### ■単独で再起動を行う方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成
~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2022
    │         └── WIN_Reboot/
    │              └── OS_build/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── handlers/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      main.yml
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
    - role: OS-Windows2022/WIN_Reboot/OS_build
      VAR_WIN_Reboot:
        restarted_services:
          - ALG
          - AppMgmt
        reboot_requires: true
        shutdown_requires: false
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

### ■複数ロール間で再起動を制御する方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成（2つの設定ロール`WIN_AutoMount`/`WIN_AutoShareServer`とともに使用する例）
~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2022
    │         └── WIN_AutoMount/
    │         │     └── OS_build/
    │         │         │── tasks/
    │         │         │      build_AutoMount.yml
    │         │         │      check.yml
    │         │         │      main.yml
    │         │         └─ README.md
    │         └── WIN_AutoShareServer/
    │         │     └── OS_build/
    │         │         │── tasks/
    │         │         │      build_Registry_present.yml
    │         │         │      build_WIN_AutoShareServer.yml
    │         │         │      main.yml
    │         │         └─ README.md
    │         └── WIN_Reboot/
    │               └── OS_build/
    │                   │── defaults/
    │                   │       main.yml
    │                   │── handlers/
    │                   │       main.yml
    │                   │── tasks/
    │                   │       main.yml
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
    - role: OS-Windows2022/WIN_AutoMount/OS_build
      VAR_WIN_AutoMount:
        NoAutoMount: 0
    - role: OS-Windows2022/WIN_AutoShareServer/OS_build
      VAR_WIN_AutoShareServer:
        AutoShareServer: 0
    - role: OS-Windows2022/WIN_Reboot/OS_build
      VAR_WIN_Reboot:
        reboot_requires: true
        shutdown_requires: false
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
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
