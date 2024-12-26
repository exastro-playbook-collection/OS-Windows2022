Ansible Role: OS-Windows2022/WIN_NetworkDrive/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するネットワークドライブ設定についての情報の設定を行います。

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
OS-Windows2022/WIN_NetworkDrive/OS_gatheringロールを利用します。

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
| `VAR_WIN_NetworkDrive` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークドライブ割り当ての「ドライブ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ProviderName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークドライブ割り当ての「フォルダー」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`User` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークドライブ割り当て時の「資格情報」の「ユーザー名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Password` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークドライブ割り当て時の「資格情報」の「パスワード」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築のアクション設定値<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_NetworkDrive:
- Action: present
  Name: Z
  Password: Passw0rd123
  ProviderName: \\192.168.0.1\TESTPF
  User: TestUser
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
    │         └── WIN_NetworkDrive/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetworkDrive_item.yml
    │                   │      build_NetworkDrive.yml
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
    - role: OS-Windows2022/WIN_NetworkDrive/OS_build
      VAR_WIN_NetworkDrive:
      - Action: present
        Name: Z
        Password: Passw0rd123
        ProviderName: \\192.168.0.1\TESTPF
        User: TestUser
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
    - role: OS-Windows2022/WIN_NetworkDrive/OS_build
      VAR_WIN_NetworkDrive:
      - Action: present
        Name: Z
        Password: Passw0rd123
        ProviderName: \\192.168.0.1\TESTPF
        User: TestUser
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NetworkDrive/OS_gathering
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
    │              └── WIN_NetworkDrive/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetworkDrive.yml
~~~

# Remarks
-------
ネットワークドライブの割り当て設定の反映にはOS再起動が必要となります。
ネットワークドライブの割り当てには、接続ユーザーの設定のみ追加・削除可能です。
設定したネットワークドライブの割り当ては、設定後にサインインしたセッションからしか利用できません。
「指定されたログオン セッションは存在しません。そのセッションは既に終了している可能性があります。」というエラーは、ansibleの接続ユーザーが、RDP等でansibleとは別にログイン中であることが原因です。
ansibleとは別にログインしているセッションをサインアウトして再実行することは必要があります。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
