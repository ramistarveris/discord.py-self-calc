import os
from dotenv import load_dotenv
import discord

# 設定:
prefix = "!"

load_dotenv()
token = os.getenv("TOKEN")

client = discord.Client()

replace_table = str.maketrans({
    "０": "0", "１": "1", "２": "2", "３": "3", "４": "4",
    "５": "5", "６": "6", "７": "7", "８": "8", "９": "9",
    "＋": "+", "－": "-", "ー": "-", "＊": "*", "／": "/",
    "÷": "/", "×": "*", "＾": "**", "（": "(", "）": ")",
    "！": "!", "　": " ",
})

@client.event
async def on_ready():
    print(f"logged as {client.user} ({client.user.id})")

@client.event
async def on_message(message):
    content = message.content.translate(replace_table).strip()
    if content.startswith(prefix):
        expression = content[1:].strip()
        if not expression:
            return
        try:
            result = eval(expression, {"__builtins__": None}, {})
            await message.channel.send(str(result))
        except:
            pass

client.run(token)
