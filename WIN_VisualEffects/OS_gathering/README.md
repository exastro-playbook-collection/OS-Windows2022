Ansible Role: OS-Windows2022/WIN_VisualEffects/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2022に関する視覚効果とデータ実行防止の情報の取得を行います。

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

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_VisualEffects/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        └── command/
                               ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_VisualEffects.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_VisualEffects.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_VisualEffects` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`visual_type` | 視覚効果の設定のタイプ（レベル）を指定する<br>0 or 既定値： コンピューターに応じて最適なものを自動的に選択する<br>1： デザインを優先する<br>2： パフォーマンスを優先する<br>3： カスタマイズ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`custom_value` | カスタマイズで視覚効果項目の設定<br>visual_type = 3 の場合、この項目は必須である。下記のサブプロジェクトのデフォルト値はnoである。値の大文字小文字の区別がない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`window_animation` | Windows 内のアニメーション コントロールと要素<br> yes: 有効<br>no: 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`IconsOnly` | アイコンの代わりに縮小版を表示する<br> no: 有効<br>yes: 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ListviewAlphaSelect` | 半透明の「選択」ツールを表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ListviewShadow` | デスクトップのアイコン名に影を付ける<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`TaskbarAnimations` | タスク バーでアニメーションを表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MinAnimate` | ウィンドウを最大化や最小化するときにアニメーションで表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`EnableAeroPeek` | プレビューを有効にする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AlwaysHibernateThumbnails` | タスク バーの縮小版のプレビューを保存する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`FontSmoothing` | スクリーン フォントの縁を滑らかにする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DragFullWindows` | ドラッグ中にウィンドウの内容を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`smooth` | リスト ボックスを滑らかにスクロールする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`slide` | コンポ ボックスをスライドして開く<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`menu_view` | メニューをフェードまたはスライドして表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mouse_shadows` | マウス ポインターの下に影を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`fade_view` | ヒントをフェードまたはスライドで表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`fade_menu` | メニュー項目をクリック後にフェードアウトする<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`window_shadows` | ウィンドウの下に影を表示する<br> yes: 有効<br>no: 無効 |
| &nbsp;&nbsp;&nbsp;&nbsp;`DataExecutionPrevention` | データ実行防止 タブ<br>2: 重要なWindowsのプログラムおよびサービスについてのみ有効にする<br>3:次に選択するものを除くすべてのプログラムおよびサービスについてDEPを有効にする |

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

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2022
    │         └── WIN_VisualEffects/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition.yml
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
    - role: OS-Windows2022/WIN_VisualEffects/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_VisualEffects/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_VisualEffects.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

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

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_VisualEffects.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
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
