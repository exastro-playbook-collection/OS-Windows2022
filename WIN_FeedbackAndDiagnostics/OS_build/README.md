Ansible Role: OS-Windows2022/WIN_FeedbackAndDiagnostics/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するフィードバックと診断設定を行います。

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
OS-Windows2022/WIN_FeedbackAndDiagnostics/OS_gatheringロールを利用します。

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
| `VAR_WIN_FeedbackAndDiagnostics` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FeedbackFrequency` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windowsの設定」「プライバシー」「診断&フィードバック」「フィードバックの間隔」「フィードバックを求められる頻度」のチェックボックスに該当<br>1：自動（推奨）<br>2：常時<br>3：1日1回<br>4：週に１回<br>5：常にオフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AllowTelemetry` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windowsの設定」「プライバシー」「診断&フィードバック」「必须とオプションの诊断データを送信する」のチェックボックスに該当<br>1:オフ<br>3:オン | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ExperiencesAdjust` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「Windowsの設定」「プライバシー」「診断&フィードバック」「エクスペリエンス調整」のチェックボックスに該当<br>0:オフ<br>1:オン | 

### Example
~~~
VAR_WIN_FeedbackAndDiagnostics:
  AllowTelemetry: 1
  FeedbackFrequency: 1
  ExperiencesAdjust: 1
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
    │         └── WIN_FeedbackAndDiagnostics/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_AllowTelemetry.yml
    │                   │      build_ExperiencesAdjust.yml
    │                   │      build_FeedbackFrequency.yml
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
    - role: OS-Windows2022/WIN_FeedbackAndDiagnostics/OS_build
      VAR_WIN_FeedbackAndDiagnostics:
        AllowTelemetry: 1
        FeedbackFrequency: 1
        ExperiencesAdjust: 1
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
    - role: OS-Windows2022/WIN_FeedbackAndDiagnostics/OS_build
      VAR_WIN_FeedbackAndDiagnostics:
        AllowTelemetry: 1
        FeedbackFrequency: 1
        ExperiencesAdjust: 1
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_FeedbackAndDiagnostics/OS_gathering
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
    │              └── WIN_FeedbackAndDiagnostics/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_FeedbackAndDiagnostics.yml
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
