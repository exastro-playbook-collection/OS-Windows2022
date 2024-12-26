Ansible Role: OS-Windows2022/WIN_NetFirewallRule_Outbound/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するファイアウォール設定（送信規則）についての情報の設定を行います。

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
OS-Windows2022/WIN_NetFirewallRule_Outbound/OS_gatheringロールを利用します。

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
| `VAR_WIN_NetFirewallRule_Outbound` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | DisplayNameのOS内情報 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RuleDescription` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」「各ファイアウォールの送信の規則のプロパティ」「全般」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Group` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | DisplayGroupのOS内情報<br>※構築では送信規則の新規作成時にのみ使用し、更新時には使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Enabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「有効」に該当<br>1 ： はい<br>2 ： いいえ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FirewallAction` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「操作」に該当<br>2 ： 許可またはセキュリティ保護<br>4 ： ブロック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Profile` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「プロファイル」に該当<br>0 ： すべて<br>1 ： ドメイン<br>2 ： プライベート<br>3 ： ドメイン、プライベート<br>4 ： パブリック<br>5 ： ドメイン、パブリック<br>6 ： プライベート、パブリック<br>7 ： ドメイン、プライベート、パブリック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalAddress` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「ローカルアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalPort` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「ローカルポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteAddress` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「リモートアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemotePort` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「リモートポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Program` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「プログラム」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Protocol` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」の「プロトコル」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Service` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows Defender ファイアウォール」「詳細設定」「セキュリティが強化されたWindows Defender ファイアウォール」「送信の規則」「各ファイアウォールの送信の規則のプロパティ」「プログラムおよびサービス」「サービス」の設定ボタン押下、「サービス設定のカスタマイズ」で設定したサービスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
VAR_WIN_NetFirewallRule_Outbound:
- Action: present
  DisplayName: Windows Media Player x86 (UDP-Out)
  Enabled: 2
  FirewallAction: 2
  Group: '@FirewallAPI.dll,-31002'
  LocalAddress:
  - Any
  LocalPort:
  - Any
  Name: WMP-Out-UDP-x86
  Profile: 0
  Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
  Protocol: UDP
  RemoteAddress:
  - Any
  RemotePort:
  - Any
  RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
  Service: Any
- Action: present
  DisplayName: Test_Outbound_FireWall
  Enabled: 1
  FirewallAction: 2
  Group: null
  LocalAddress:
  - Any
  LocalPort:
  - Any
  Name: Test_Outbound_FireWall
  Profile: 0
  Program: '%ProgramFiles% (x86)\Test_Outbound_FireWall\Test_Outbound_FireWall.exe'
  Protocol: Any
  RemoteAddress:
  - Any
  RemotePort:
  - Any
  RuleDescription: Test_Outbound_FireWall
  Service: Any
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
    │         └── WIN_NetFirewallRule_Outbound/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetFirewallRule_Outbound_adapter_absent.yml
    │                   │      build_NetFirewallRule_Outbound_adapter_present.yml
    │                   │      build_NetFirewallRule_Outbound_adapter.yml
    │                   │      build_NetFirewallRule_Outbound_item.yml
    │                   │      build_NetFirewallRule_Outbound.yml
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
    - role: OS-Windows2022/WIN_NetFirewallRule_Outbound/OS_build
      VAR_WIN_NetFirewallRule_Outbound:
      - Action: present
        DisplayName: Windows Media Player x86 (UDP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        Name: WMP-Out-UDP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: UDP
        RemoteAddress:
        - Any
        RemotePort:
        - Any
        RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
        Service: Any
      - Action: present
        DisplayName: Test_Outbound_FireWall
        Enabled: 1
        FirewallAction: 2
        Group: null
        LocalAddress:
        - Any
        LocalPort:
        - Any
        Name: Test_Outbound_FireWall
        Profile: 0
        Program: '%ProgramFiles% (x86)\Test_Outbound_FireWall\Test_Outbound_FireWall.exe'
        Protocol: Any
        RemoteAddress:
        - Any
        RemotePort:
        - Any
        RuleDescription: Test_Outbound_FireWall
        Service: Any
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
    - role: OS-Windows2022/WIN_NetFirewallRule_Outbound/OS_build
      VAR_WIN_NetFirewallRule_Outbound:
      - Action: present
        DisplayName: Windows Media Player x86 (UDP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        Name: WMP-Out-UDP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: UDP
        RemoteAddress:
        - Any
        RemotePort:
        - Any
        RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
        Service: Any
      - Action: present
        DisplayName: Test_Outbound_FireWall
        Enabled: 1
        FirewallAction: 2
        Group: null
        LocalAddress:
        - Any
        LocalPort:
        - Any
        Name: Test_Outbound_FireWall
        Profile: 0
        Program: '%ProgramFiles% (x86)\Test_Outbound_FireWall\Test_Outbound_FireWall.exe'
        Protocol: Any
        RemoteAddress:
        - Any
        RemotePort:
        - Any
        RuleDescription: Test_Outbound_FireWall
        Service: Any
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NetFirewallRule_Outbound/OS_gathering
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
    │              └── WIN_NetFirewallRule_Outbound/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetFirewallRule_Outbound.yml
~~~

# Remarks
-------
定義済みの規則では、パラメータのいくつかは変更できません。<br>
パラメタ値がnullで設定を実行した際に、設定変更されたことを表すメッセージ「changed」が出力され、OSの動作としてはレジストリキーが存在しない場合と同等になります。<br>
本ロールの実行により値を変更したくない場合は、入力パラメタから値がnullのパラメタを手動で削除してください。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
