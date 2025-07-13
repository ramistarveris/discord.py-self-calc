discordのS*elf botで自分を計算機化するものです<br>
数字や記号は全部全角に対応しています<br>
プレフィックスの後にスペースがあってもなくても反応します<br>
evalを使用していますがほぼ悪意のあるコードが実行されることはないと思います

## 実行例: 
`prefix = "!"`<br>
### 例 ①
- コマンド:
    - !(114514+114514)*(114*(51+4)-1+145+14)+(114*514+(-(1-14)*5*14+1+1+45+14)) 
- 送信される文字:
    - 1472251551

### 例 ②
- コマンド: 
    - ! 1551 + 114141＊４１*412 
- 送信される文字:
    - 1928071323

## 設定:
### prefix (コマンドの文頭)
`python.py`<br>
ファイルの8行目に設定があります
デフォルトには ! が設定されていますが "" の中の文字を変更することで別のプレフィックスに変更することができます。
```py
7   #設定
8   prefix = "!"
```
### オーナー設定①
`python.py`<br>
ファイルの10行目に設定があります<br>
`True` で有効
`False` で無効
```py
9   # オーナーのみが使用できるどうか
10  owner_only = True
```
### オーナー設定②
`python.py`<br>
ファイルの12行目に設定があります<br>
自分のDiscordのIDを貼り付けてください（コマンドを実行する側）
```py
11    # オーナーのユーザーID（オーナーのみが使用できる場合のみ有効）
12    owner_id = 123456789012345678
```

### TOKEN
`.env`<br>
.env という名前のファイルの一行目に
```env
TOKEN=
```
という文字列があります<br>
= の横にアカウントのトークンを貼り付けてください<br>
例:
```env
TOKEN=Y0U4Re41dI0t.AhAHhAhhAhAAHha
```
トークン取得方法は各自で調べてね

## 実行環境
[Python 3.12.4](https://www.python.org/downloads/release/python-3124/)<br>
[discord.py-self   2.0.1](https://discordpy-self.readthedocs.io/en/latest/intro.html)<br>

```
python3 -m pip install -U discord.py-self
```
```
python3 -m venv bot-env
```
