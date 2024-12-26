Ansible Role: OS-Windows2022/WIN_OSRecoveryConfiguration/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するWindows詳細情報（起動と回復）についての情報の設定を行います。

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
OS-Windows2022/WIN_OSRecoveryConfiguration/OS_gatheringロールを利用します。

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
| `VAR_WIN_OSRecoveryConfiguration` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BootSystem` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 起動と回復 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`default` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◎&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「起動システム」の「既定のオペレーティングシステム」に該当<br>ブートエントリの識別子を設定する。<br>ブートエントリの識別子は、「bcdedit」または「bcdedit /v」コマンドで出力される、ブート構成データ (BCD)」の「Windowsブートローダー」-「identifier」の値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`timeout` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「起動システム」の「オペレーティングシステムの一覧を表示する時間」に該当<br>該当の設定項目で入力できる数値<br>値設定範囲：0～999（0に設定した場合、この項目は無効になる） | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SystemError` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | システムエラー | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AutoReboot` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「自動的に再起動する」のチェックボックスに該当<br>true ： 自動的に再起動する<br>false ： 自動的に再起動しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DebugInfoType` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「デバッグ情報の書き込み」に該当<br>0 ： なし<br>1 ： 完全メモリ ダンプ/アクティブメモリダンプ<br>2 ： カーネル メモリ ダンプ<br>3 ： 最小メモリ ダンプ (256KB)<br>7 ： 自動メモリ ダンプ | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`FilterPages` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | DebugInfoTypeで完全メモリ/アクティブメモリを設定した場合に設定する<br>1：アクティブメモリダンプ<br>0：完全メモリダンプ<br>※ 完全メモリダンプ/アクティブメモリダンプを設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DebugFilePath` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「ダンプファイル」に該当<br>DebugInfoTypeで完全メモリ ダンプ、アクティブメモリダンプ、カーネル メモリ ダンプ、自動メモリ ダンプを設定した際のダンプファイル出力先<br>※ 完全メモリ ダンプ、アクティブメモリダンプ、カーネル メモリ ダンプ、自動メモリ ダンプを設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MiniDumpDirectory` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「最小ダンプディレクトリ」に該当<br>DebugInfoTypeで 最小メモリ ダンプ (256KB)を設定した際のダンプファイル出力先<br>※  最小メモリ ダンプ (256KB)を設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OverwriteExistingDebugFile` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「既存のファイルに上書きする」に該当<br>true ： 上書きする<br>false ： 上書きしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AlwaysKeepMemoryDump` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「ディスク領域が少ないときでもメモリダンプの自動削除を無効にする」のチェックボックスに該当<br>1 ： 無効にする<br>1以外の数字(0など) ： 無効にしない | 

### Example
~~~
VAR_WIN_OSRecoveryConfiguration:
  BootSystem:
    default: '{0daf9bba-94c8-11e6-b1fd-0e5bdc9ce43b}'
    timeout: '30'
  SystemError:
    AlwaysKeepMemoryDump: null
    AutoReboot: true
    DebugFilePath: '%SystemRoot%\MEMORY.DMP'
    DebugInfoType: 7
    FilterPages: null
    MiniDumpDirectory: '%SystemRoot%\Minidump'
    OverwriteExistingDebugFile: true

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
    │         └── WIN_OSRecoveryConfiguration/
    │              └── OS_build/
    │                   │── files/
    │                   │      timeDisplay.ps1
    │                   │── tasks/
    │                   │      build_OSRecoveryConfiguration.yml
    │                   │      build_OSRecoveryConfiguration_boot.yml
    │                   │      build_OSRecoveryConfiguration_dump.yml
    │                   │      build_OSRecoveryConfiguration_recover.yml
    │                   │      build_Registry_absent.yml
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
    - role: OS-Windows2022/WIN_OSRecoveryConfiguration/OS_build
      VAR_WIN_OSRecoveryConfiguration:
        BootSystem:
          default: '{0daf9bba-94c8-11e6-b1fd-0e5bdc9ce43b}'
          timeout: '30'
        SystemError:
          AlwaysKeepMemoryDump: null
          AutoReboot: true
          DebugFilePath: '%SystemRoot%\MEMORY.DMP'
          DebugInfoType: 7
          FilterPages: null
          MiniDumpDirectory: '%SystemRoot%\Minidump'
          OverwriteExistingDebugFile: true
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
    - role: OS-Windows2022/WIN_OSRecoveryConfiguration/OS_build
      VAR_WIN_OSRecoveryConfiguration:
        BootSystem:
          default: '{0daf9bba-94c8-11e6-b1fd-0e5bdc9ce43b}'
          timeout: '30'
        SystemError:
          AlwaysKeepMemoryDump: null
          AutoReboot: true
          DebugFilePath: '%SystemRoot%\MEMORY.DMP'
          DebugInfoType: 7
          FilterPages: null
          MiniDumpDirectory: '%SystemRoot%\Minidump'
          OverwriteExistingDebugFile: true
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_OSRecoveryConfiguration/OS_gathering
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
    │              └── WIN_OSRecoveryConfiguration/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_OSRecoveryConfiguration.yml
~~~

# Remarks
-------
「オペレーティング～ 」の 時間設定はbcdedit /timeout <秒数>で0～999を指定します。999を超えて入力した場合、設定は反映されるが、OSで動作不正を起こす可能性があります。

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
