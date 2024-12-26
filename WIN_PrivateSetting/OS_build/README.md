Ansible Role: OS-Windows2022/WIN_PrivateSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するプライバシー設定についての情報の設定を行います。

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
OS-Windows2022/WIN_PrivateSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- |
| `VAR_WIN_PrivateSetting` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`location` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「位置情報」の「このデバイスでの位置情報へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`webcam` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「カメラ」の「このデバイスのカメラへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`microphone` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「マイク」の「このデバイスでのマイクへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userNotificationListener` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「通知」の「このデバイスのユーザー通知へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userAccountInformation` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「アカウント情報」の「このデバイスのアカウント情報へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`contacts` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「連絡先」の「このデバイスでの連絡先へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appointments` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「カレンダー」の「このデバイスでのカレンダーへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`phoneCallHistory` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「通話履歴」の「このデバイスでの通話履歴へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`email` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「メール」の「このデバイスでの電子メールへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`userDataTasks` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「タスク」の「このデバイスでのタスクへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`chat` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「メッセージング」の「このデバイスでのメッセージングへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`radios` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「無線」の「このデバイスの無線を制御するためのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`bluetoothSync` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「他のデバイス」の「ペアリングされていないデバイスとの通信許可」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`appDiagnostics` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「アプリの診断」の「このデバイスのアプリの診断情報へのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`documentsLibrary` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「ドキュメント」の「このデバイスでのドキュメントライブラリへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`picturesLibrary` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「ピクチャ」の「このデバイスでの画像ライブラリへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`videosLibrary` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「ビデオ」の「このデバイスでのビデオライブラリへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`broadFileSystemAccess` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「ファイルシステム」の「このデバイスのファイルシステムへのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`phoneCall` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「電話をかける」の「このデバイスでの通話を許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`downloadsFolder` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「ダウンロード フォルダー」の「このデバイスのダウンロード フォルダーのアクセスを許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`graphicsCaptureWithoutBorder` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「スクリーンショットの境界線」の「このデバイスのスクリーンショットの境界設定を許可する」に該当<br>Allow ： オン<br>Deny ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`graphicsCaptureProgrammatic` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「設定」「プライバシー」「アプリのアクセス許可」「スクリーンショットとアプリ」の「このデバイスのさまざまなウィンドウまたはディスプレイのスクリーンショットをアプリに許可します」に該当<br>Allow ： オン<br>Deny ： オフ | 

### Example
~~~
VAR_WIN_PrivateSetting:
  appDiagnostics: Allow
  appointments: Allow
  bluetoothSync: Allow
  broadFileSystemAccess: Allow
  chat: Allow
  contacts: Allow
  documentsLibrary: Allow
  email: Allow
  location: Allow
  microphone: Allow
  phoneCallHistory: Allow
  picturesLibrary: Allow
  radios: Allow
  userAccountInformation: Allow
  userDataTasks: Allow
  userNotificationListener: Allow
  videosLibrary: Allow
  webcam: Allow
  phoneCall: Allow
  downloadsFolder: Allow
  graphicsCaptureWithoutBorder: Allow
  graphicsCaptureProgrammatic: Allow
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
    │         └── WIN_PrivateSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_PrivateSetting.yml
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
    - role: OS-Windows2022/WIN_PrivateSetting/OS_build
      VAR_WIN_PrivateSetting:
        appDiagnostics: Allow
        appointments: Allow
        bluetoothSync: Allow
        broadFileSystemAccess: Allow
        chat: Allow
        contacts: Allow
        documentsLibrary: Allow
        email: Allow
        location: Allow
        microphone: Allow
        phoneCallHistory: Allow
        picturesLibrary: Allow
        radios: Allow
        userAccountInformation: Allow
        userDataTasks: Allow
        userNotificationListener: Allow
        videosLibrary: Allow
        webcam: Allow
        phoneCall: Allow
        downloadsFolder: Allow
        graphicsCaptureWithoutBorder: Allow
        graphicsCaptureProgrammatic: Allow
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
    - role: OS-Windows2022/WIN_PrivateSetting/OS_build
      VAR_WIN_PrivateSetting:
        appDiagnostics: Allow
        appointments: Allow
        bluetoothSync: Allow
        broadFileSystemAccess: Allow
        chat: Allow
        contacts: Allow
        documentsLibrary: Allow
        email: Allow
        location: Allow
        microphone: Allow
        phoneCallHistory: Allow
        picturesLibrary: Allow
        radios: Allow
        userAccountInformation: Allow
        userDataTasks: Allow
        userNotificationListener: Allow
        videosLibrary: Allow
        webcam: Allow
        phoneCall: Allow
        downloadsFolder: Allow
        graphicsCaptureWithoutBorder: Allow
        graphicsCaptureProgrammatic: Allow
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_PrivateSetting/OS_gathering
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
    │              └── WIN_PrivateSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_PrivateSetting.yml
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
