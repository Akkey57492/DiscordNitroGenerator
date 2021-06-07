# DiscordNitroGenerator
Nitroコードのランダム生成ツール

# Miner.py
起動して生成個数を指定すればランダムなギフトURL用コードを生成できます。

# Checker.py
nitro.txtに保存されたコードをAPIを使用して有効か確認します。
API制限がかかると2分間チェックが一時停止します。

# Miner2.py
nitro.txtに保存されたコードをURLに変換し、Discordに送信します。
送信していって有効なものを探します。
Tokenを書き換える必要があります。
```python
client.run("ここにToken")
```
