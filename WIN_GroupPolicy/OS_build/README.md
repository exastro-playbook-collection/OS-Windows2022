Ansible Role: OS-Windows2022/WIN_GroupPolicy/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するローカルグループポリシーについての情報の設定を行います。

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

本ロールでは、他のロールは必要ありません。
ただし、本READMEに書かれている「エビデンスを取得する場合」の手順を行う場合は、
OS-Windows2022/WIN_GroupPolicy/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  ◎：キーのため変更不可の変数（更新、削除の場合）<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_WIN_GroupPolicy` | 
| `- Key` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | グループポリシーに関連するレジストリパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Values` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- ValueName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ValueType` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_GroupPolicy:
- Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
  Values:
  - Action: present
    Value: 5
    ValueName: ConsentPromptBehaviorAdmin
    ValueType: REG_DWORD
  - Action: present
    Value: 3
    ValueName: ConsentPromptBehaviorUser
    ValueType: REG_DWORD
  ・・・
- Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
  Values:
  - Action: present
    Value: 0
    ValueName: ForceActiveDesktopOn
    ValueType: REG_DWORD
  - Action: present
    Value: 1
    ValueName: NoActiveDesktop
    ValueType: REG_DWORD
  ・・・
・・・
~~~


## Optional Variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

## ■エビデンスを取得しない場合の呼び出す方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2022
    │         └── WIN_GroupPolicy/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_GroupPolicy_item.yml
    │                   │      build_GroupPolicy.yml
    │                   │      build_Registry_absent.yml
    │                   │      build_Registry_present.yml
    │                   │      build_Registry.yml
    │                   │      check_parameter_item.yml
    │                   │      check_parameter.yml
    │                   │      check.yml
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
    - role: OS-Windows2022/WIN_GroupPolicy/OS_build
      VAR_WIN_GroupPolicy:
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
        Values:
        - Action: present
          Value: 5
          ValueName: ConsentPromptBehaviorAdmin
          ValueType: REG_DWORD
        - Action: present
          Value: 3
          ValueName: ConsentPromptBehaviorUser
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
        Values:
        - Action: present
          Value: 0
          ValueName: ForceActiveDesktopOn
          ValueType: REG_DWORD
        - Action: present
          Value: 1
          ValueName: NoActiveDesktop
          ValueType: REG_DWORD
        ・・・
      ・・・
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

## ■エビデンスを取得する場合の呼び出す方法

エビデンスを収集する場合、以下のようなエビデンス収集用のPlaybookを作成してください。  

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_GroupPolicy/OS_build
      VAR_WIN_GroupPolicy:
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
        Values:
        - Action: present
          Value: 5
          ValueName: ConsentPromptBehaviorAdmin
          ValueType: REG_DWORD
        - Action: present
          Value: 3
          ValueName: ConsentPromptBehaviorUser
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
        Values:
        - Action: present
          Value: 0
          ValueName: ForceActiveDesktopOn
          ValueType: REG_DWORD
        - Action: present
          Value: 1
          ValueName: NoActiveDesktop
          ValueType: REG_DWORD
        ・・・
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_GroupPolicy/OS_gathering
  strategy: free
~~~

- エビデンス収集結果一覧

エビデンス収集結果は、以下のように格納されます。
エビデンス収集結果の詳細は、OS_gatheringロールを確認してください。

~~~
#エビデンス構成
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_GroupPolicy/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_GroupPolicy.yml
~~~

# Remarks
-------
情報取得でレジストリ値では空白だが取得結果が"\0"と設定されるレジストリ値があります。<br>
例) HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Systemのlegalnoticetext<br>
その情報取得結果のパラメターファイルで、情報設定を行った場合は情報は変更されません。<br>
ansible-playbookで変更したレジストリは、ローカルグループポリシーエディタからは確認できません。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
