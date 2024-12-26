Ansible Role: OS-Windows2022/WIN_UserAccount/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するローカルユーザーについての情報の設定を行います。

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
OS-Windows2022/WIN_UserAccount/OS_gatheringロールを利用します。

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
| `VAR_WIN_UserAccount` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FullName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「フルネーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Description` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordRequired` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「ユーザーは次回ログオン時にパスワードの変更が必要」のチェックボックスに該当<br>true ： パスワードの変更が必要でない<br>false ： パスワードの変更が必要 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordChangeable` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「ユーザーはパスワードを変更できない」のチェックボックスに該当<br>true ： パスワードを変更できる<br>false ： パスワードを変更できない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordExpires` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「パスワードを無期限にする」のチェックボックスに該当<br>true ： パスワードを無期限にしない<br>false ： パスワードを無期限にする | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Disabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「アカウントを無効にする」のチェックボックスに該当<br>true ： アカウントを無効にする<br>false ： アカウントを無効にしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Password` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ユーザー作成時に設定するパスワード | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordApply` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | パスワード変更情報フラグ<br>true ： ユーザー作成、パスワードを含めたユーザー更新の際に設定<br>false ： パスワードを含めないユーザー更新時に設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present ： ユーザー作成、更新<br>absent ： ユーザーの削除 | 

### Example
~~~
VAR_WIN_UserAccount:
- Action: present
  Description: Test User Create
  Disabled: false
  FullName: 'TestUser'
  Name: TestUser
  Password: 'Passw0rd123'
  PasswordApply: true
  PasswordChangeable: true
  PasswordExpires: false
  PasswordRequired: false
- Action: absent
  Name: TestUser2
・・・
~~~


## Optional Variables

特にありません。

# Usage

1. 本Roleを用いたPlaybookを作成します。
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
    │         └── WIN_UserAccount/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_User_item.yml
    │                   │      build_User.yml
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
    - role: OS-Windows2022/WIN_UserAccount/OS_build
      VAR_WIN_UserAccount:
      - Action: present
        Description: Test User Create
        Disabled: false
        FullName: 'TestUser'
        Name: TestUser
        Password: 'Passw0rd123'
        PasswordApply: true
        PasswordChangeable: true
        PasswordExpires: false
        PasswordRequired: false
      - Action: absent
        Name: DelUser
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
    - role: OS-Windows2022/WIN_UserAccount/OS_build
      VAR_WIN_UserAccount:
      - Action: present
        Description: Test User Create
        Disabled: false
        FullName: 'TestUser'
        Name: TestUser
        Password: 'Passw0rd123'
        PasswordApply: true
        PasswordChangeable: true
        PasswordExpires: false
        PasswordRequired: false
      - Action: absent
        Name: DelUser
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_UserAccount/OS_gathering
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
    │              └── WIN_UserAccount/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_UserAccount.yml
~~~

# Remarks
-------
値に変更が無い場合でも、ansible-playbookの結果としてchangedとなる場合があります。実際に値が変更されたかどうかはエビデンス収集を行い、その結果を確認してください。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
