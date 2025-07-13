import os
import ast
import operator
from dotenv import load_dotenv
import discord

# 設定:
prefix = ";"

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

allowed_ops = { ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg, ast.UAdd: operator.pos, }

def safe_eval(expr: str):
    node = ast.parse(expr, mode='eval')

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        elif isinstance(n, ast.Constant):
            if isinstance(n.value, (int, float)):
                return n.value
        elif isinstance(n, ast.BinOp):
            if type(n.op) in allowed_ops:
                return allowed_ops[type(n.op)](_eval(n.left), _eval(n.right))
        elif isinstance(n, ast.UnaryOp):
            if type(n.op) in allowed_ops:
                return allowed_ops[type(n.op)](_eval(n.operand))
        raise ValueError("Invalid expression")

    return _eval(node)

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
            result = safe_eval(expression)
            await message.channel.send(str(result))
        except Exception as e:
            await message.channel.send(e)

client.run(token)
