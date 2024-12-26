Ansible Role: OS-Windows2022/WIN_NICTeaming_VLAN/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するNICチーミング設定（VLAN）についての情報の設定を行います。

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
OS-Windows2022/WIN_NICTeaming_VLAN/OS_gatheringロールを利用します。

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
| `VAR_WIN_NICTeaming_VLAN` | 
| `- Team` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「チーム インターフェース」の「チーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ifDesc` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | VLANのInterface　Description<br>「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「一般情報」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「一般情報」のVLAN名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Primary` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | プライマリ インターフェースの有無<br>true ： プライマリ インターフェース<br>false ： セカンダリ インターフェース |
| &nbsp;&nbsp;&nbsp;&nbsp;`Default` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「VLAN メンバーシップ」の「既定」に該当<br>true ： 既定<br>false ： 既定でない<br>※既定はプライマリのVLANのみ設定可能 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`VlanID` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「VLAN メンバーシップ」の「特定のVLAN」に該当<br>※Defaultがfalseの場合のみVlanIDの設定が有効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
VAR_WIN_NICTeaming_VLAN: 
- Action: present
  Default: true
  Name: PFTEST
  Primary: true
  Team: Primary
  VlanID: null
  ifDesc: Microsoft Network Adapter Multiplexor Driver
- Action: present
  Default: false
  Name: PFTEST_VLAN_8
  Primary: false
  Team: Secondary_8
  VlanID: 8
  ifDesc: Microsoft Network Adapter Multiplexor Driver8
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
    │         └── WIN_NICTeaming_VLAN/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NICTeaming_VLAN_adapter.yml
    │                   │      build_NICTeaming_VLAN_item_absent.yml
    │                   │      build_NICTeaming_VLAN_item_present_detail_Primary.yml
    │                   │      build_NICTeaming_VLAN_item_present_detail_Secondary.yml
    │                   │      build_NICTeaming_VLAN_item_present_Primary.yml
    │                   │      build_NICTeaming_VLAN_item_present_Secondary.yml
    │                   │      build_NICTeaming_VLAN.yml
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
    - role: OS-Windows2022/WIN_NICTeaming_VLAN/OS_build
      VAR_WIN_NICTeaming_VLAN: 
      - Action: present
        Default: true
        Name: PFTEST
        Primary: true
        Team: Primary
        VlanID: null
        ifDesc: Microsoft Network Adapter Multiplexor Driver
      - Action: present
        Default: false
        Name: PFTEST_VLAN_8
        Primary: false
        Team: Secondary_8
        VlanID: 8
        ifDesc: Microsoft Network Adapter Multiplexor Driver8
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
    - role: OS-Windows2022/WIN_NICTeaming_VLAN/OS_build
      VAR_WIN_NICTeaming_VLAN: 
      - Action: present
        Default: true
        Name: PFTEST
        Primary: true
        Team: Primary
        VlanID: null
        ifDesc: Microsoft Network Adapter Multiplexor Driver
      - Action: present
        Default: false
        Name: PFTEST_VLAN_8
        Primary: false
        Team: Secondary_8
        VlanID: 8
        ifDesc: Microsoft Network Adapter Multiplexor Driver8
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NICTeaming_VLAN/OS_gathering
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
    │              └── WIN_NICTeaming_VLAN/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NICTeaming_VLAN.yml
~~~

# Remarks
-------
チームが設定されていないと、VLANは追加できません。<br>
プライマリ インターフェースのVLANは作成、削除できません。<br>
セカンダリ インターフェースのVLANを作成する際には、ifDescを空文字としてください。　設定内容： ifDesc: ''<br>
本ロールのパラメータはNICのチーミング設定後にVLAN IDが確定してから設定する必要があります。そのため、NICTeaming_Teamとセットで設定する場合、NICTeaming_Teamの設定後に本ロールのパラメータの設定を実行する必要があります。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
