Ansible Role: OS-Windows2022/WIN_DirOption/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関するフフォルダオプション設定を行います。

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
OS-Windows2022/WIN_DirOption/OS_gatheringロールを利用します。

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
| `VAR_WIN_DirOption` |
| &nbsp;&nbsp;&nbsp;&nbsp;`HiddenCheckedValue` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「ファイルとフォルダーの表示」方式を変更できるかどうかのフラグ<br>1 : 「ファイルとフォルダーの表示」 は変更可能<br>0 : 「ファイルとフォルダーの表示」 は変更できない、「隠しファイル、隠しフォルダー及び隠しドライブを表示しない」を選択される |
| &nbsp;&nbsp;&nbsp;&nbsp;`Hidden` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「フォルダオプション」「表示」「詳細設定」「ファイルとフォルダーの表示」のチェックボックスに該当<br>1 ： 隠しファイル、隠しフォルダー及び隠しドライブを表示する<br>2 ： 隠しファイル、隠しフォルダー及び隠しドライブを表示しない |
| &nbsp;&nbsp;&nbsp;&nbsp;`HideFileExt` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 「フォルダオプション」「表示」「詳細設定」「登録されている拡張子は表示しない」のチェックボックスに該当<br>0 ： 登録されている拡張子は表示する<br>1 ： 登録されている拡張子は表示しない |

### Example
~~~
VAR_WIN_DirOption:
  Hidden: 2
  HiddenCheckedValue: 1
  HideFileExt: 0
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
    │         └── WIN_DirOption/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_DirOption.yml
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
    - role: OS-Windows2022/WIN_DirOption/OS_build
      VAR_WIN_DirOption:
        Hidden: 2
        HiddenCheckedValue: 1
        HideFileExt: 0
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
    - role: OS-Windows2022/WIN_DirOption/OS_build
      VAR_WIN_DirOption:
        Hidden: 2
        HiddenCheckedValue: 1
        HideFileExt: 0
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_DirOption/OS_gathering
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
    │              └── WIN_DirOption/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_DirOption.yml
~~~

# Remarks
-------
- この設定は、hostsファイルで指定されたユーザーにのみ適用され、他のユーザーには影響しません。<br>
- HiddenCheckedValueとHiddenの組み合わせは下記の四つがあります。<br>

| 項番 | HiddenCheckedValue|Hidden | 「フォルダーオプション」GUI画面 | ファイルとフォルダーの表示効果 |
| -------- | :-----------: | ----------- | ----------- | ----------- |
| 1| 1 | 1 | 「ファイルとフォルダーの表示」オプションが有効であり、「隠しファイル、隠しフォルダー及び隠しドライブを表示する」がチェックされます。 | 隠しファイル、隠しフォルダー及び隠しドライブを表示します |
| 2 | 1 |2 | ファイルとフォルダーの表示」オプションが有効であり、「隠しファイル、隠しフォルダー及び隠しドライブを表示しない」がチェックされます。 | 隠しファイル、隠しフォルダー及び隠しドライブを表示しません |
| 3※ | 0 | 1 | 「ファイルとフォルダーの表示」オプションが有効であるが、オプションが何も設定しません。 | 隠しファイル、隠しフォルダー及び隠しドライブを表示します |
| 4 | 0 | 2 | ファイルとフォルダーの表示」オプションが有効であり、「隠しファイル、隠しフォルダー及び隠しドライブを表示しない」がチェックされます。 | 隠しファイル、隠しフォルダー及び隠しドライブを表示しません |

※上記の組み合わせ３について、OS仕様で「フォルダーオプション」GUI画面の表示情報と「ファイルとフォルダー」の表示効果が不一致でありますので、このケースを設定しないでください。<br>

# License
-------

# Copyright
---------
Copyright (c) 2023 NEC Corporation

# Author Information
------------------
NEC Corporation
