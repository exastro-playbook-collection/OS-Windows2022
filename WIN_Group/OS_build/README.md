Ansible Role: OS-Windows2022/WIN_Group/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するローカルグループについての情報の設定を行います。

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
OS-Windows2022/WIN_Group/OS_gatheringロールを利用します。

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
| `VAR_WIN_Group` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「グループ」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`user` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「グループ」「グループのプロパティ」「全般」の「所属するメンバー」に該当<br>このパラメータは配列で記載する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Domain` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |  対象のグループがドメイングループかローカルグループかを指定します<br>ドメイングループの場合、対象のドメイン名を指定してください<br>ローカルグループの場合、対象のサーバ名を指定してください | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present: 作成/更新<br>absent: 削除 | 

### Example
~~~
VAR_WIN_Group:
- Action: present
  Domain: TESTDOMAIN
  Name: TESTGROUP1
  user:
  - Administrator
  - ansible
- Action: absent
  Domain: TESTDOMAIN
  Name: DELGROUP
  user:
  - Administrator
  - ansible
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
    │         └── WIN_Group/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_Group_item.yml
    │                   │      build_Group_list.yml
    │                   │      build_Group.yml
    │                   │      build_GroupMmemberShip.yml
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
    - role: OS-Windows2022/WIN_Group/OS_build
      VAR_WIN_Group:
      - Action: present
        Domain: TESTDOMAIN
        Name: TESTGROUP1
        user:
        - Administrator
        - ansible
      - Action: absent
        Domain: TESTDOMAIN
        Name: DELGROUP
        user:
        - Administrator
        - ansible
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
    - role: OS-Windows2022/WIN_Group/OS_build
      VAR_WIN_Group:
      - Action: present
        Domain: TESTDOMAIN
        Name: TESTGROUP1
        user:
        - Administrator
        - ansible
      - Action: absent
        Domain: TESTDOMAIN
        Name: DELGROUP
        user:
        - Administrator
        - ansible
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_Group/OS_gathering
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
    │              └── WIN_Group/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_Group.yml
~~~

# Remarks
-------
1. ゲストマシンがドメインに未加入の場合、グループのメンバにドメインユーザー、またはドメイングループを追加することはできません。
2. グループのメンバに"APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES"を指定すると本ロールの実行時にエラーとなります。"ALL APPLICATION PACKAGES"を指定して実行してください。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
