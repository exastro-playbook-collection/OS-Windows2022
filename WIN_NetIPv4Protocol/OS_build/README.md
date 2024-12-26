Ansible Role: OS-Windows2022/WIN_NetIPv4Protocol/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するIPv4の設定についての情報の設定を行います。

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
OS-Windows2022/WIN_NetIPv4Protocol/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_WIN_NetIPv4Protocol` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultHopLimit` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | デフォルトのホップ制限値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NeighborCacheLimit` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネイバーキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RouteCacheLimit` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ルートキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ReassemblyLimit` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 再構成バッファーの最大サイズ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IcmpRedirects` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ICMPリダイレクト<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SourceRoutingBehavior` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ソースルーティングされたパケットの動作<br>0 ： Forward<br>1 ： DontForward<br>2 ： Drop | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DhcpMediaSense` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | MediaSense<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MediaSenseEventLog` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | MediaSenseイベントログ<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IGMPLevel` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | インターネットグループ管理プロトコル（IGMP）レベル<br>0 ： None<br>1 ： SendOnly<br>2 ： All | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IGMPVersion` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | IGMPバージョン番号<br>2 ： Version1<br>3 ： Version2<br>4 ： Version3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MulticastForwarding` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | マルチキャスト転送<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`GroupForwardedFragments` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | グループ転送フラグメント<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RandomizeIdentifiers` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 識別子のランダム化<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressMaskReply` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | アドレスマスク応答<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MinimumMtu` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ネットワーク層の最大伝送ユニット（MTU）の値をバイト単位数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DeadGatewayDetection` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 停止しているゲートウェイの検出 | 

### Example
~~~
VAR_WIN_NetIPv4Protocol:
  AddressMaskReply: 0
  DefaultHopLimit: 128
  DhcpMediaSense: 1
  GroupForwardedFragments: 0
  IGMPLevel: 2
  IGMPVersion: 4
  IcmpRedirects: 1
  MediaSenseEventLog: 0
  MinimumMtu: 576
  MulticastForwarding: 0
  NeighborCacheLimit: 1024
  RandomizeIdentifiers: 1
  ReassemblyLimit: 33551232
  RouteCacheLimit: 32768
  SourceRoutingBehavior: 1
  DeadGatewayDetection: 1
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
    │         └── WIN_NetIPv4Protocol/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetIPv4Protocol.yml
    │                   │      build_NetIPv4Protocol_each.yml
    │                   │      build_NetIPv4Protocol_item.yml
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
    - role: OS-Windows2022/WIN_NetIPv4Protocol/OS_build
      VAR_WIN_NetIPv4Protocol:
        AddressMaskReply: 0
        DefaultHopLimit: 128
        DhcpMediaSense: 1
        GroupForwardedFragments: 0
        IGMPLevel: 2
        IGMPVersion: 4
        IcmpRedirects: 1
        MediaSenseEventLog: 0
        MinimumMtu: 576
        MulticastForwarding: 0
        NeighborCacheLimit: 1024
        RandomizeIdentifiers: 1
        ReassemblyLimit: 33551232
        RouteCacheLimit: 32768
        SourceRoutingBehavior: 1
        DeadGatewayDetection: 1
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
    - role: OS-Windows2022/WIN_NetIPv4Protocol/OS_build
      VAR_WIN_NetIPv4Protocol:
        AddressMaskReply: 0
        DefaultHopLimit: 128
        DhcpMediaSense: 1
        GroupForwardedFragments: 0
        IGMPLevel: 2
        IGMPVersion: 4
        IcmpRedirects: 1
        MediaSenseEventLog: 0
        MinimumMtu: 576
        MulticastForwarding: 0
        NeighborCacheLimit: 1024
        RandomizeIdentifiers: 1
        ReassemblyLimit: 33551232
        RouteCacheLimit: 32768
        SourceRoutingBehavior: 1
        DeadGatewayDetection: 1
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NetIPv4Protocol/OS_gathering
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
    │              └── WIN_NetIPv4Protocol/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetIPv4Protocol.yml
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
