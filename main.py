import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True         

bot = commands.Bot(command_prefix="!", intents=intents)

frutas = {
    "dragon": {"loja": 3500000, "trade": 27000000},
    "dough": {"loja": 2400000, "trade": 10000000},
    "buddha": {"loja": 1200000, "trade": 3000000}
}

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def valor(ctx, fruta: str):
    fruta = fruta.lower()
    if fruta in frutas:
        dados = frutas[fruta]
        await ctx.send(
            f"📦 **{fruta.title()}**\n💰 Loja: {dados['loja']}\n🔄 Trade: {dados['trade']}"
        )
    else:
        await ctx.send("❌ Fruta não encontrada.")

@bot.command()
async def comparar(ctx, fruta1: str, fruta2: str):
    fruta1, fruta2 = fruta1.lower(), fruta2.lower()
    if fruta1 in frutas and fruta2 in frutas:
        v1, v2 = frutas[fruta1]["trade"], frutas[fruta2]["trade"]
        if v1 > v2:
            await ctx.send(f"✅ **{fruta1.title()}** vale mais que **{fruta2.title()}**.")
        elif v1 < v2:
            await ctx.send(f"❌ **{fruta1.title()}** vale menos que **{fruta2.title()}**.")
        else:
            await ctx.send(f"⚖️ As duas valem o mesmo.")
    else:
        await ctx.send("❌ Uma das frutas não foi encontrada.")

bot.run(TOKEN)
