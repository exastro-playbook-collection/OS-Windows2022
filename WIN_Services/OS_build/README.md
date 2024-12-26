Ansible Role: OS-Windows2022/WIN_Services/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するWindowsサービスについての情報の設定を行います。

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
OS-Windows2022/WIN_Services/OS_gatheringロールを利用します。

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
| `VAR_WIN_Services` | 
| `- Name` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「サービス名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayName` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「表示名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Status` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「サービスの状態」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`StartType` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「スタートアップの種類」に該当<br>Auto ： 自動／自動（遅延開始)<br>Manual ： 手動<br>Disabled ： 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction1` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「最初のエラー」に該当<br>RUN PROCESS ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay1(msec)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「最初のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction2` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「次のエラー」に該当<br>RUN PROCESS ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay2(msec)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「次のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction3` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「その後のエラー」に該当<br>RUN PROCESS ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay3(msec)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「その後のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RebootMessage` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「再起動する前に、このメッセージをネットワーク上のコンピュータに送信する」のチェックボックスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ResetPeriod(sec)` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「エラーカウントのリセット」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`CmdLine` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「プログラムの実行」の「プログラム」 「コマンドラインのパラメタ―」 「コマンドラインにエラーカウントのオプションを追加」のチェックボックスに該当する<br>プログラム ： プログラム実行パス<br>コマンドラインのパラメタ― ： パラメタ―値<br>コマンドラインにエラーカウントのオプションを追加 ： 追加の場合は/fail=%1%'を記載、追加しない場合は記載しない | 

### Example
~~~
VAR_WIN_Services:
- CmdLine: ''
  Delay1(msec): '3000'
  Delay2(msec): '3000'
  DisplayName: AllJoyn Router Service
  FailureAction1: RESTART
  FailureAction2: RESTART
  Name: AJRouter
  RebootMessage: ''
  ResetPeriod(sec): '86400'
  StartType: Manual
  Status: Stopped
- CmdLine: ''
  Delay1(msec): '120000'
  Delay2(msec): '300000'
  DisplayName: Application Layer Gateway Service
  FailureAction1: RESTART
  FailureAction2: RESTART
  Name: ALG
  RebootMessage: ''
  ResetPeriod(sec): '900'
  StartType: Manual
  Status: Stopped
・・・
~~~


## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_build_exclusive_service_names` | ["DPS", "WinDefend"] | 設定対象からの除外サービス一覧 | 

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
    │         └── WIN_Services/
    │              └── OS_build/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_Services_each.yml
    │                   │      build_Services_win_service.yml
    │                   │      build_Services_win_shell_actions.yml
    │                   │      build_Services_win_shell_command.yml
    │                   │      build_Services_win_shell_reboot.yml
    │                   │      build_Services.yml
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
    - role: OS-Windows2022/WIN_Services/OS_build
      VAR_WIN_Services:
      - CmdLine: ''
        Delay1(msec): '3000'
        Delay2(msec): '3000'
        DisplayName: AllJoyn Router Service
        FailureAction1: RESTART
        FailureAction2: RESTART
        Name: AJRouter
        RebootMessage: ''
        ResetPeriod(sec): '86400'
        StartType: Manual
        Status: Stopped
      - CmdLine: ''
        Delay1(msec): '120000'
        Delay2(msec): '300000'
        DisplayName: Application Layer Gateway Service
        FailureAction1: RESTART
        FailureAction2: RESTART
        Name: ALG
        RebootMessage: ''
        ResetPeriod(sec): '900'
        StartType: Manual
        Status: Stopped
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
    - role: OS-Windows2022/WIN_Services/OS_build
      VAR_WIN_Services:
      - CmdLine: ''
        Delay1(msec): '3000'
        Delay2(msec): '3000'
        DisplayName: AllJoyn Router Service
        FailureAction1: RESTART
        FailureAction2: RESTART
        Name: AJRouter
        RebootMessage: ''
        ResetPeriod(sec): '86400'
        StartType: Manual
        Status: Stopped
      - CmdLine: ''
        Delay1(msec): '120000'
        Delay2(msec): '300000'
        DisplayName: Application Layer Gateway Service
        FailureAction1: RESTART
        FailureAction2: RESTART
        Name: ALG
        RebootMessage: ''
        ResetPeriod(sec): '900'
        StartType: Manual
        Status: Stopped
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_Services/OS_gathering
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
    │              └── WIN_Services/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_Services.yml
~~~

# Remarks
-------
設定値としてRebootMessageに値が設定されていた場合、値に変更が無い場合でもansible-playbookの結果としてchangedとなります。<br>
実際に値が変更されたかどうかはエビデンス収集を行い、その結果を確認してください。<br>
Windowsサービスによっては、アクセスエラーとなるサービスがあるため、収集した全てのWindowsサービスの設定はできません。<br>
サービスの追加、削除は不可です。<br>
タスクスケジューラ(Name=Scheduler)の取得値が不正になり、設定もできないことが判明しているため、当機能の利用は推奨されません。<br>
サービスの回復操作は最大で32個設定可能だが、3個目までしか設定できません。また、サービスに設定済みの4個目以降の回復操作は、ツールで設定を変更したときに削除されます。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
