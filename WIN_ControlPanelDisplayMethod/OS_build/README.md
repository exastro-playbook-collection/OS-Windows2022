Ansible Role: OS-Windows2022/WIN_ControlPanelDisplayMethod/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するコントロールパネルの表示方法の設定を行います。

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
OS-Windows2022/WIN_ControlPanelDisplayMethod/OS_gatheringロールを利用します。

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
| `VAR_WIN_ControlPanelDisplayMethod` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayMethod` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「システム情報」「コントロールパネル」「表示方法」のチェックボックスに該当<br>category or 既定値 ： カテゴリ<br>large ： 大きいアイコン<br>small ： 小さいアイコン<br>大文字小文字の区別がない | 

### Example
~~~
VAR_WIN_ControlPanelDisplayMethod:
  DisplayMethod: large
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
    │         └── WIN_ControlPanelDisplayMethod/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_ControlPanelDisplayMethod.yml
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
    - role: OS-Windows2022/WIN_ControlPanelDisplayMethod/OS_build
      VAR_WIN_ControlPanelDisplayMethod:
        DisplayMethod: large
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
    - role: OS-Windows2022/WIN_ControlPanelDisplayMethod/OS_build
      VAR_WIN_ControlPanelDisplayMethod:
        DisplayMethod: large
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_ControlPanelDisplayMethod/OS_gathering
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
    │              └── WIN_ControlPanelDisplayMethod/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_ControlPanelDisplayMethod.yml
~~~

# Remarks
-------
[administrator]以外の管理者がターゲットマシンにログインした場合、キー[HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel]がレジストリに存在しないため、このユーザーでのビルドの実行中にエラーが発生します。<br>
このキー[HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel]の所有者を管理者から管理者に変更することによってのみ、このキー[HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ControlPanel]が使用可能になり、このユーザーを使用して構築ロールを実行できます。<br>

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
