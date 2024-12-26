Ansible Role: OS-Windows2022/WIN_Defender/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するWindowsDefender設定についての情報の設定を行います。

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
OS-Windows2022/WIN_Defender/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- |
| `VAR_WIN_Defender` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableRealtimeMonitoring` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「リアルタイム保護」に該当<br>false ： オン<br>true ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MAPSReporting` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「クラウド提供の保護」に該当<br>2 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SubmitSamplesConsent` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「サンプルの自動送信」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`EnableControlledFolderAccess` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ランサムウェアの防止」の「ランサムウェア防止の管理」「コントロールされたフォルダーアクセス」に該当<br>1 ： オン<br>0 ： オフ<br>※ OSのビルドバージョンによって取得/反映が行えない場合があります | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableEnhancedNotifications` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」の「情報提供の通知を受け取る」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SummaryNotificationDisabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「最近のアクティビティとスキャン結果」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NoActionNotificationDisabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「脅威が見つかりましたが、直ちに対処する必要性はありません」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FilesBlockedNotificationDisabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ウィルスと驚異の防止に関する通知」「情報提供の通知を受け取る」の「ファイルまたはアクティビティがブロックされています」のチェックボックスに該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallPublicProfileNotice` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「ドメイン ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallStandardProfileNotice` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「プライベート ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FireWallDomainProfileNotice` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」「設定の管理」「通知」「通知設定の変更」「ファイアウォールとネットワーク保護の通知」の「パブリック ファイアウォール」に該当<br>0 ： オン<br>1 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SmartScreenEnabled` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「アプリとブラウザーコントロール」の「アプリとファイルの確認」に該当<br>Warn ： オン<br>Off ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BlockApps` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「アプリとブラウザー　コントロール」「評価ベースの保護設定」「望ましくない可能性のあるアプリのブロック」「アプリをブロックする」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BlockDownloads` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windows セキュリティ」「ウィルスと驚異の防止」「ウィルスと驚異の防止の設定」の「設定の管理」「アプリとブラウザー　コントロール」「評価ベースの保護設定」「望ましくない可能性のあるアプリのブロック」「ダウンロードをブロックする」に該当<br>1 ： オン<br>0 ： オフ | 

### Example
~~~
VAR_WIN_Defender:
  DisableEnhancedNotifications: 0
  DisableRealtimeMonitoring: false
  EnableControlledFolderAccess: 0
  FilesBlockedNotificationDisabled: 0
  FireWallDomainProfileNotice: 1
  FireWallPublicProfileNotice: 1
  FireWallStandardProfileNotice: 1
  MAPSReporting: 2
  NoActionNotificationDisabled: 0
  SmartScreenEnabled: 'Off'
  SubmitSamplesConsent: 1
  SummaryNotificationDisabled: 0
  BlockApps: 0
  BlockDownloads: 0
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
    │         └── WIN_Defender/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_Defender.yml
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
    - role: OS-Windows2022/WIN_Defender/OS_build
      VAR_WIN_Defender:
        DisableEnhancedNotifications: 0
        DisableRealtimeMonitoring: false
        EnableControlledFolderAccess: 0
        FilesBlockedNotificationDisabled: 0
        FireWallDomainProfileNotice: 1
        FireWallPublicProfileNotice: 1
        FireWallStandardProfileNotice: 1
        MAPSReporting: 2
        NoActionNotificationDisabled: 0
        SmartScreenEnabled: 'Off'
        SubmitSamplesConsent: 1
        SummaryNotificationDisabled: 0
        BlockApps: 0
        BlockDownloads: 0
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
    - role: OS-Windows2022/WIN_Defender/OS_build
      VAR_WIN_Defender:
        DisableEnhancedNotifications: 0
        DisableRealtimeMonitoring: false
        EnableControlledFolderAccess: 0
        FilesBlockedNotificationDisabled: 0
        FireWallDomainProfileNotice: 1
        FireWallPublicProfileNotice: 1
        FireWallStandardProfileNotice: 1
        MAPSReporting: 2
        NoActionNotificationDisabled: 0
        SmartScreenEnabled: 'Off'
        SubmitSamplesConsent: 1
        SummaryNotificationDisabled: 0
        BlockApps: 0
        BlockDownloads: 0
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_Defender/OS_gathering
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
    │              └── WIN_Defender/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_Defender.yml
~~~

# Remarks
-------
Windows Defenderをインストールしていない場合は、本ロール実行時にエラーとなるため実行しないでください。<br>
<br>
パラメタ値がnullで設定を実行した際に、設定変更されたことを表すメッセージ「changed」が出力されますが、OSの動作としてはレジストリキーが存在しない場合と同等になります。<br>
本ロールの実行により値を変更したくない場合は、入力パラメタから値がnullのパラメタを手動で削除してください。<br>
<br>
変数説明に該当する内容は、OSエディションによって、内容が変わる場合があります。<br>
参考リンク：https://azuread.net/archives/11651、Microsoft Defender for Endpoint (MDE) を利用しているクライアントデバイスのために、設定不可。対応不要。<br>

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
