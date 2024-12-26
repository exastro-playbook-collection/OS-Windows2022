Ansible Role: OS-Windows2022/WIN_NetAdapterBinding/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するネットワーク接続の詳細設定についての情報の設定を行います。

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
OS-Windows2022/WIN_NetAdapterBinding/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  ◎：キーのため変更不可の変数<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_WIN_NetAdapterBinding` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」のネットワークアダプター名称に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`parameter` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークアダプター名称の「プロパティ」「この接続は次の項目を使用します」の項目に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Value` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークアダプター名称の「プロパティ」「この接続は次の項目を使用します」の項目のチェックボックスに該当<br>true ： 項目を使用する<br>false ： 項目を使用しない | 

### Example
~~~
VAR_WIN_NetAdapterBinding:
- Name: Ethernet
  Value: true
  parameter: Microsoft LLDP Protocol Driver
- Name: Ethernet
  Value: false
  parameter: Microsoft Network Adapter Multiplexor Protocol
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
    │         └── WIN_NetAdapterBinding/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetAdapterBinding.yml
    │                   │      build_NetAdapterBinding_item.yml
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
    - role: OS-Windows2022/WIN_NetAdapterBinding/OS_build
      VAR_WIN_NetAdapterBinding:
      - Name: Ethernet
        Value: true
        parameter: Microsoft LLDP Protocol Driver
      - Name: Ethernet
        Value: false
        parameter: Microsoft Network Adapter Multiplexor Protocol
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
    - role: OS-Windows2022/WIN_NetAdapterBinding/OS_build
      VAR_WIN_NetAdapterBinding:
      - Name: Ethernet
        Value: true
        parameter: Microsoft LLDP Protocol Driver
      - Name: Ethernet
        Value: false
        parameter: Microsoft Network Adapter Multiplexor Protocol
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NetAdapterBinding/OS_gathering
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
    │              └── WIN_NetAdapterBinding/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetAdapterBinding.yml
~~~

# Remarks
-------
Parameterが「Microsoft Network Adapter Multiplexor Protocol」の行は設定変更できません。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
