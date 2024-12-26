Ansible Role: OS-Windows2022/WIN_VisualEffects/OS_build
=======================================================
# Description
本ロールは、Windows Server 2022に関する視覚効果とデータ実行防止の情報の設定を行います。

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
OS-Windows2022/WIN_VisualEffects/OS_gatheringロールを利用します。

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
| `VAR_WIN_VisualEffects` | 
| &nbsp;&nbsp;&nbsp;&nbsp;`visual_type` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 視覚効果の設定のタイプ（レベル）を指定する<br>0 or 既定値： コンピューターに応じて最適なものを自動的に選択する<br>1： デザインを優先する<br>2： パフォーマンスを優先する<br>3： カスタマイズ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`custom_value` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | カスタマイズで視覚効果項目の設定<br>visual_type = 3 の場合、この項目は必須である。下記のサブプロジェクトのデフォルト値はnoである。値の大文字小文字の区別がない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`window_animation` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Windows 内のアニメーション コントロールと要素<br> yes: 有効<br>no: 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`IconsOnly` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | アイコンの代わりに縮小版を表示する<br> no: 有効<br>yes: 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ListviewAlphaSelect` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 半透明の「選択」ツールを表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ListviewShadow` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | デスクトップのアイコン名に影を付ける<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`TaskbarAnimations` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | タスク バーでアニメーションを表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MinAnimate` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ウィンドウを最大化や最小化するときにアニメーションで表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`EnableAeroPeek` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | プレビューを有効にする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AlwaysHibernateThumbnails` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | タスク バーの縮小版のプレビューを保存する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`FontSmoothing` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | スクリーン フォントの縁を滑らかにする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DragFullWindows` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ドラッグ中にウィンドウの内容を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`smooth` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | リスト ボックスを滑らかにスクロールする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`slide` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | コンポ ボックスをスライドして開く<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`menu_view` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | メニューをフェードまたはスライドして表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mouse_shadows` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | マウス ポインターの下に影を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`fade_view` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ヒントをフェードまたはスライドで表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`fade_menu` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | メニュー項目をクリック後にフェードアウトする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`window_shadows` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | ウィンドウの下に影を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;`DataExecutionPrevention` | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;〇&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | データ実行防止 タブ<br>2: 重要なWindowsのプログラムおよびサービスについてのみ有効にする<br>3:次に選択するものを除くすべてのプログラムおよびサービスについてDEPを有効にする |

### Example
~~~
VAR_WIN_VisualEffects:
  DataExecutionPrevention: 3
  visual_type: 3
  custom_value:
    window_animation: 'yes'
    IconsOnly: 'no'
    window_shadows: 'no'
    MinAnimate: 'yes'
    slide: 'yes'
    FontSmoothing: 'no'
    TaskbarAnimations: 'no'
    AlwaysHibernateThumbnails: 'no'
    ListviewShadow: 'no'
    DragFullWindows: 'no'
    fade_view: 'yes'
    EnableAeroPeek: 'no'
    mouse_shadows: 'no'
    menu_view: 'yes'
    fade_menu: 'no'
    smooth: 'yes'
    ListviewAlphaSelect: 'no'
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
    │         └── WIN_VisualEffects/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      check.yml
    │                   │      main.yml
    │                   │      modify.yml
    │                   │      modify_custom.yml
    │                   │      modify_DataExecutionPrevention.yml
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
    - role: OS-Windows2022/WIN_VisualEffects/OS_build
      VAR_WIN_VisualEffects:
        DataExecutionPrevention: 3
        visual_type: 3
        custom_value:
          window_animation: 'yes'
          IconsOnly: 'no'
          window_shadows: 'no'
          MinAnimate: 'yes'
          slide: 'yes'
          FontSmoothing: 'no'
          TaskbarAnimations: 'no'
          AlwaysHibernateThumbnails: 'no'
          ListviewShadow: 'no'
          DragFullWindows: 'no'
          fade_view: 'yes'
          EnableAeroPeek: 'no'
          mouse_shadows: 'no'
          menu_view: 'yes'
          fade_menu: 'no'
          smooth: 'yes'
          ListviewAlphaSelect: 'no'
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
    - role: OS-Windows2022/WIN_VisualEffects/OS_build
      VAR_WIN_VisualEffects:
        DataExecutionPrevention: 3
        visual_type: 3
        custom_value:
          window_animation: 'yes'
          IconsOnly: 'no'
          window_shadows: 'no'
          MinAnimate: 'yes'
          slide: 'yes'
          FontSmoothing: 'no'
          TaskbarAnimations: 'no'
          AlwaysHibernateThumbnails: 'no'
          ListviewShadow: 'no'
          DragFullWindows: 'no'
          fade_view: 'yes'
          EnableAeroPeek: 'no'
          mouse_shadows: 'no'
          menu_view: 'yes'
          fade_menu: 'no'
          smooth: 'yes'
          ListviewAlphaSelect: 'no'
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2022/WIN_VisualEffects/OS_gathering
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
    │              └── WIN_VisualEffects/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_VisualEffects.yml
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2024 NEC Corporation

# Author Information
------------------
NEC Corporation
