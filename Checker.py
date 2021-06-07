import requests
import json
import time
import re

print("""

███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")

codes = open("nitro.txt", "r")
for code in codes:
	result = code.replace("\n", "")
	Check = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{result}")
	GetResponse = Check.json()
	Failed = GetResponse["message"]
	if Check.status_code == 200:
		print(f"ActiveNitro: {result}")
	elif Failed == "You are being rate limited.":
		print(f"Failed: {result}")
		print("リクエストが拒否されました。")
		print("120秒間処理を一時停止します。")
	else:
		print(f"InActiveNitro: {result}")
