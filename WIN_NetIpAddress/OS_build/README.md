Ansible Role: OS-Windows2022/WIN_NetIpAddress/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するネットワーク基本情報についての情報の設定を行います。

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
OS-Windows2022/WIN_NetIpAddress/OS_gatheringロールを利用します。

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
| `VAR_WIN_NetIpAddress` | 
| `- ifDesc` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティの接続の方法に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ipaddr` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークデバイスのプロパティの接続方法「インターネットプロトコルバージョン4」または「インターネットプロトコルバージョン6」のプロパティのIPアドレス、Microsoft ISATAP AdapterのIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`prefix` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワークアドレス部分の長さ（プレフィックス）<br>プレフィックス値として指定可能な数値を指定する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressFamily` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | IPアドレスファミリ<br>2 ： IPv4を使用<br>23 ： IPv6を使用 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Type` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | IPアドレスタイプ<br>1 ： Unicastを使用<br>2 ： Anycastを使用 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`connectionName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |  ネットワークインターフェース名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`mask` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |  「ネットワークプロトコル」 -> 「インターネット プロトコル バージョン 4(TCP/IPv4)」 -> 「サブネットマスク」に該当<br>デフォルトは255.255.0.0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present:  IPｖ4、IPv6をネットワークデバイスに追加<br>absent: IPｖ4、IPv6をネットワークデバイスから削除 | 

### Example
~~~
VAR_WIN_NetIpAddress:
- Action: present
  AddressFamily: 23
  Type: 1
  connectionName: test1
  ifDesc: Network Device #0
  ipaddr: 0:0:0:0:0:0:0:0
  prefix: 64
- Action: present
  AddressFamily: 23
  Type: 1
  connectionName: test2
  ifDesc: Network Device #1
  ipaddr: 0:0:0:0:0:0:0:0
  prefix: 64
- Action: present
  AddressFamily: 2
  AddressState: 4
  PolicyStore: 1
  Type: 1
  connectionName: test_NICTeam
  ifDesc: Microsoft Network Adapter Multiplexor Driver
  ipaddr: 172.28.1.1
  mask: 255.255.0.0
  prefix: 16
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
    │         └── WIN_NetIpAddress/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetIpAddress_adapter.yml
    │                   │      build_NetIpAddress_item.yml
    │                   │      build_NetIpAddress.yml
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
    - role: OS-Windows2022/WIN_NetIpAddress/OS_build
      VAR_WIN_NetIpAddress:
      - Action: present
        AddressFamily: 23
        Type: 1
        connectionName: test1
        ifDesc: Network Device #0
        ipaddr: 0:0:0:0:0:0:0:0
        prefix: 64
      - Action: present
        AddressFamily: 23
        Type: 1
        connectionName: test2
        ifDesc: Network Device #1
        ipaddr: 0:0:0:0:0:0:0:0
        prefix: 64
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
    - role: OS-Windows2022/WIN_NetIpAddress/OS_build
      VAR_WIN_NetIpAddress:
      - Action: present
        AddressFamily: 23
        Type: 1
        connectionName: test1
        ifDesc: Network Device #0
        ipaddr: 0:0:0:0:0:0:0:0
        prefix: 64
      - Action: present
        AddressFamily: 23
        Type: 1
        connectionName: test2
        ifDesc: Network Device #1
        ipaddr: 0:0:0:0:0:0:0:0
        prefix: 64
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NetIpAddress/OS_gathering
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
    │              └── WIN_NetIpAddress/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetIpAddress.yml
~~~

# Remarks
-------
ipaddrに指定したIPアドレスが該当のネットワークアダプターに追加されるため、すでにIPアドレスが設定されている場合は複数のIPアドレスが追加されるため注意してください。<br>
誤って追加した場合は、本ロールで削除してください。<br>
IPv6のアドレス設定はRFC5952推奨の省略形で記載します。記載しない場合は、エラーになります。記載については、次のサイトにある「IPv6アドレスの推奨テキスト表記」を参照してください。<br>
https://www.nic.ad.jp/ja/newsletter/No46/0800.html<br>
IPアドレスの削除は、収集したネットワークデバイスのIPアドレスを変更せずに実施した場合のみ削除されます。<br>
IPV6を使用するアドレスの構成にマスクがないので、IPV6のIPを設定するとき、マスク(mask)を指定しないでください。<br>
Ansibleで通信中のNICの情報は変更しないでください。<br>

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
