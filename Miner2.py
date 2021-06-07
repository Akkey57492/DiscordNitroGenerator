import discord
import asyncio

client = discord.Client()

chid = input("ChannelID: ")

@client.event
async def on_ready():
	print("""

	███╗░░██╗██╗████████╗██████╗░░█████╗░  ░█████╗░░█████╗░██████╗░███████╗  ░██████╗░███████╗███╗░░██╗
	████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔════╝████╗░██║
	██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
	██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
	██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚█████╔╝╚█████╔╝██████╔╝███████╗  ╚██████╔╝███████╗██║░╚███║
	╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
	""")
	codes = open("nitro.txt", "r")
	for code in codes:
		result = code.replace("\n", "")
		channel = await client.fetch_channel(int(chid))
		await asyncio.sleep(1)
		await channel.send(f"https://discord.gift/{result}")
	
@client.event
async def on_message(message):
	if message.content == "!stop":
		exit()

client.run("Token")