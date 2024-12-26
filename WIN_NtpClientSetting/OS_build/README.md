Ansible Role: OS-Windows2022/WIN_NtpClientSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関する時刻同期（Windows Timeサービス）についての情報の設定を行います。

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
OS-Windows2022/WIN_NtpClientSetting/OS_gatheringロールを利用します。

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
| `VAR_WIN_NtpClientSetting` | 
| `- Key` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 時刻同期（Windows Timeサービス）に関連するレジストリパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Values` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- ValueName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ValueType` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | レジストリ値 | 

### Example
~~~
VAR_WIN_NtpClientSetting:
- Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
  Values:
  - Value: 1
    ValueName: AllowNonstandardModeCombinations
    ValueType: REG_DWORD
  - Value: 2147483648
    ValueName: CompatibilityFlags
    ValueType: REG_DWORD
  ・・・
- Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
  Values:
  - Value: 192.168.0.1,0x9
    ValueName: NtpServer
    ValueType: REG_SZ
  - Value: C:\Windows\system32\w32time.dll
    ValueName: ServiceDll
    ValueType: REG_EXPAND_SZ
  ・・・
- Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
  Values:
  - Value: 10
    ValueName: AnnounceFlags
    ValueType: REG_DWORD
  - Value: 2
    ValueName: EventLogFlags
    ValueType: REG_DWORD
  ・・・
- Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpServer
  Values:
  - Value: 1
    ValueName: AllowNonstandardModeCombinations
    ValueType: REG_DWORD
  - Value: 0
    ValueName: Enabled
    ValueType: REG_DWORD
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
    │         └── WIN_NtpClientSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NtpClientSetting.yml
    │                   │      build_NtpClientSetting_item.yml
    │                   │      build_Registry_present.yml
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
    - role: OS-Windows2022/WIN_NtpClientSetting/OS_build
      VAR_WIN_NtpClientSetting:
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 2147483648
          ValueName: CompatibilityFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
        Values:
        - Value: 192.168.0.1,0x9
          ValueName: NtpServer
          ValueType: REG_SZ
        - Value: C:\Windows\system32\w32time.dll
          ValueName: ServiceDll
          ValueType: REG_EXPAND_SZ
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
        Values:
        - Value: 10
          ValueName: AnnounceFlags
          ValueType: REG_DWORD
        - Value: 2
          ValueName: EventLogFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpServer
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 0
          ValueName: Enabled
          ValueType: REG_DWORD
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
    - role: OS-Windows2022/WIN_NtpClientSetting/OS_build
      VAR_WIN_NtpClientSetting:
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 2147483648
          ValueName: CompatibilityFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
        Values:
        - Value: 192.168.0.1,0x9
          ValueName: NtpServer
          ValueType: REG_SZ
        - Value: C:\Windows\system32\w32time.dll
          ValueName: ServiceDll
          ValueType: REG_EXPAND_SZ
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
        Values:
        - Value: 10
          ValueName: AnnounceFlags
          ValueType: REG_DWORD
        - Value: 2
          ValueName: EventLogFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpServer
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 0
          ValueName: Enabled
          ValueType: REG_DWORD
        ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_NtpClientSetting/OS_gathering
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
    │              └── WIN_NtpClientSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NtpClientSetting.yml
~~~

# Remarks
-------
レジストリ種別がREG_MULTI_SZの場合でかつ、Valueの配列に対して重複した文字列(空文字を含む)が含まれていた場合、設定時にスキップとなります。Valueの配列より重複した文字列を削除して設定を行うようにしてください。<br>
取得パラメタの値によっては、時間経過で動的に値が変わるものがあり、設定変更されたことを表すメッセージ「changed」が出力されますが、<br>
設定後自動的に戻るため影響はないものになります。<br>
レジストリ種別がREG_MULTI_SZの場合、空白行データが含まれると、空白行データが余分に表示されます。空白行データをそのまま使用して構築した場合、設定自体行われず、エラーで停止します。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
