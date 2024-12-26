Ansible Role: OS-Windows2022/WIN_InternetOption/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するインターネットオプションでセキュリティ（SSL 3.0、TLS 1.0、TLS 1.1、TLS 1.2、TLS 1.3）の設定を行います。

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
OS-Windows2022/WIN_InternetOption/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。<br>
<br>
「値変更可能列」について<br>
  〇：値が変更できる変数<br>

| Name     | 値変更可能 | Description | 
| -------- | :-----------: | ----------- | 
| `VAR_WIN_InternetOption` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SecureProtocols` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「コントロール パネル」「すべてのコントロール パネル項目」「インターネット オプション」「詳細設定」「SSL 3.0を使用する/TLS 1.0を使用する/TLS 1.1の使用/TLS 1.2の使用/TLS 1.3の使用」に該当<br>0： すべて選択しない<br>32： 「SSL 3.0を使用する」を選択する<br>128： 「TLS 1.0を使用する」を選択する<br>512： 「TLS 1.1の使用」を選択する<br>2048： 「TLS 1.2の使用」を選択する<br>8192 ： 「TLS 1.3の使用」を選択する<br>160： 「SSL 3.0を使用する,TLS 1.0を使用する」を選択する<br>544： 「SSL 3.0を使用する,TLS 1.1の使用」を選択する<br>2080： 「SSL 3.0を使用する,TLS 1.2の使用」を選択する<br>8224： 「SSL 3.0を使用する,TLS 1.3の使用」を選択する<br>640： 「TLS 1.0を使用する,TLS 1.1の使用」を選択する<br>2176： 「TLS 1.0を使用する,TLS 1.2の使用」を選択する<br>8320： 「TLS 1.0を使用する,TLS 1.3の使用」を選択する<br>2560： 「TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8704： 「TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10240： 「TLS 1.2の使用,TLS 1.3の使用」を選択する<br>672： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用」を選択する<br>2208： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.2の使用」を選択する<br>8352： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.3の使用」を選択する<br>2592： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8736： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10272： 「SSL 3.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>2688： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8832： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10368： 「TLS 1.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10752： 「TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>2720： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用」を選択する<br>8864： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.3の使用」を選択する<br>10400： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10784： 「SSL 3.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10880： 「TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」を選択する<br>10912： 「SSL 3.0を使用する,TLS 1.0を使用する,TLS 1.1の使用,TLS 1.2の使用,TLS 1.3の使用」すべてを選択する | 

### Example
~~~
VAR_WIN_InternetOption:
  SecureProtocols: 2048
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
    │         └── WIN_InternetOption/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      check.yml
    │                   │      build_WIN_InternetOption.yml
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
    - role: OS-Windows2022/WIN_InternetOption/OS_build
      VAR_WIN_InternetOption:
        SecureProtocols: 2048
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
    - role: OS-Windows2022/WIN_InternetOption/OS_build
      VAR_WIN_InternetOption:
        SecureProtocols: 2048
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_InternetOption/OS_gathering
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
    │              └── WIN_InternetOption/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_InternetOption.yml
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
