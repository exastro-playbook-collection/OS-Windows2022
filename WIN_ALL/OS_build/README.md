Ansible Role: OS-Windows2022/WIN_ALL/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に 関する情報の設定を一括で行います。

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

本ロールでは、<VAR_OS_target_rolename>で定義したパラメータ生成対象のOS_buildロールを利用します。
また、本READMEに書かれている「エビデンスを取得する場合」の手順を行う場合は、
WIN_ALLのOS_gatheringおよび<VAR_OS_target_rolename>で定義したパラメータ生成対象のOS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値は、<VAR_OS_target_rolename>の定義によって変動します。
<VAR_OS_target_rolename>で定義したパラメータ生成対象のOS_buildロールを確認してください。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_reboot` | false | OSに関する設定後の再起動実行有無<br>true: 再起動する<br>false: 再起動しない | 
| `VAR_OS_target_rolename` | (*1) | OSに関する設定対象 | 

(*1) 本変数値はOSに関する設定対象とするロールを定義します。
     運用に合わせて対象の追加/削除を行ってください。

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
    │    └── OS-Windows2022/
    │         └── WIN_ALL/
    │              └── OS_build/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build.yml
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
    - role: OS-Windows2022/WIN_ALL/OS_build
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
    - role: OS-Windows2022/WIN_ALL/OS_build
      VAR_OS_reboot: true
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_ALL/OS_gathering
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

- エビデンス収集結果一覧

エビデンス収集結果は、以下のように格納されます。
エビデンス収集結果の詳細は、各エビデンス収集対象のOS_gatheringロールを確認してください。

~~~
#エビデンス構成
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── エビデンス収集対象/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        エビデンス収集対象.yml
~~~

# Remarks
-------
下記ロールは初期設定では、設定対象ではないため設定が必要な場合はコメントを削除して実施してください。<br>
・WIN_WindowsFeature<br>
・WIN_Services<br>
・WIN_DirectorySetting<br>
・WIN_ErrorReporting<br>
・WIN_NetFirewallRule_Inbound<br>
・WIN_NetFirewallRule_Outbound<br>
・WIN_GroupPolicy<br>
・WIN_SecurityPolicy<br>
・WIN_EventLog<br>
・WIN_FileProtectionSetting<br>
・WIN_Reboot<br>

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
