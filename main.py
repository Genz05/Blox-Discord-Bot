import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True         

bot = commands.Bot(command_prefix="!", intents=intents)

frutas = {
    "rocket": {"loja": 5000, "trade": 5000},
    "spin": {"loja": 7500, "trade": 7500},
    "blade": {"loja": 30000, "trade": 50000},
    "spring": {"loja": 60000, "trade": 60000},
    "bomb": {"loja": 80000, "trade": 80000},
    "smoke": {"loja": 100000, "trade": 100000},
    "spike": {"loja": 180000, "trade": 180000},
    "flame": {"loja": 250000, "trade": 250000},
    "dark": {"loja": 500000, "trade": 400000},
    "sand": {"loja": 420000, "trade": 420000},
    "ice": {"loja": 350000, "trade": 550000},
    "eagle": {"loja": 550000, "trade": 800000},
    "diamond": {"loja": 600000, "trade": 1000000},
    "rubber": {"loja": 750000, "trade": 700000},
    "ghost": {"loja": 940000, "trade": 800000},
    "light": {"loja": 650000, "trade": 800000},
    "magma": {"loja": 960000, "trade": 1150000},
    "quake": {"loja": 1000000, "trade": 1000000},
    "love": {"loja": 1300000, "trade": 1500000},
    "spider": {"loja": 1500000, "trade": 1500000},
    "sound": {"loja": 1700000, "trade": 2500000},
    "phoenix": {"loja": 1800000, "trade": 2750000},
    "creation": {"loja": 1400000, "trade": 3500000},
    "blizzard": {"loja": 2400000, "trade": 5000000},
    "buddha": {"loja": 1200000, "trade": 10000000},
    "portal": {"loja": 1900000, "trade": 15000000},
    "pain": {"loja": 2300000, "trade": 20000000},
    "rumble": {"loja": 2100000, "trade": 75000000},
    "shadow": {"loja": 2900000, "trade": 6500000},
    "venom": {"loja": 3000000, "trade": 10000000},
    "control": {"loja": 3200000, "trade": 10000000},
    "spirit": {"loja": 3400000, "trade": 10000000},
    "mammoth": {"loja": 2700000, "trade": 10000000},
    "gravity": {"loja": 2500000, "trade": 20000000},
    "t-rex": {"loja": 2700000, "trade": 20000000},
    "dough": {"loja": 2800000, "trade": 30000000},
    "leopard": {"loja": 5000000, "trade": 55000000},
    "gas": {"loja": 3200000, "trade": 75000000},
    "yeti": {"loja": 5000000, "trade": 140000000},
    "kitsune": {"loja": 8000000, "trade": 255000000},
    "eastdragon": {"loja": 15000000, "trade": 1020000000},
    "westdragon": {"loja": 15000000, "trade": 1275000000}
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
        
def calcular_valor_total(lista_frutas):
    valor_total = 0
    frutas_encontradas = []
    for fruta in lista_frutas:
        fruta_limpa = fruta.strip().lower() 
        if fruta_limpa in frutas:
            valor_total += frutas[fruta_limpa]["trade"]
            frutas_encontradas.append(fruta_limpa.title())
    return valor_total, frutas_encontradas
    
@bot.command(name="list")
async def list_frutas(ctx):
    lista_de_frutas = "Aqui estão todas as frutas disponíveis:\n\n"
    for fruta in frutas.keys():
        lista_de_frutas += f"• {fruta.title()}\n"
    
    await ctx.send(lista_de_frutas)



@bot.command(name="comparar", help="Compara o valor de até 4 frutas de cada lado de uma troca. Use o formato: !comparar (fruta1 fruta2) (fruta3 fruta4). Use '-' para espaços vazios.")
async def comparar(ctx, *args):

    entrada = " ".join(args)

 
    if entrada.count('(') != 2 or entrada.count(')') != 2:
        await ctx.send("❌ Formato de comando incorreto. Use: `!comparar (fruta1 fruta2) (fruta3 fruta4)`")
        return


    try:
        parte1_str = entrada.split(')')[0].replace('(', '').strip()
        parte2_str = entrada.split(')')[1].replace('(', '').strip()
        
  
        frutas_player1 = [f for f in parte1_str.split() if f != '-']
        frutas_player2 = [f for f in parte2_str.split() if f != '-']
    except IndexError:
        await ctx.send("❌ Erro ao processar o formato. Verifique se há espaços e parênteses corretos.")
        return

  
    valor_player1, frutas_encontradas1 = calcular_valor_total(frutas_player1)
    valor_player2, frutas_encontradas2 = calcular_valor_total(frutas_player2)

   
    lista_player1 = ", ".join(frutas_encontradas1) if frutas_encontradas1 else "Nenhuma fruta válida"
    lista_player2 = ", ".join(frutas_encontradas2) if frutas_encontradas2 else "Nenhuma fruta válida"
    

    if valor_player1 > valor_player2:
        resultado = f"✅ **Jogador 1** leva vantagem!"
    elif valor_player2 > valor_player1:
        resultado = f"❌ **Jogador 2** leva vantagem!"
    else:
        resultado = f"⚖️ A troca é justa!"

    
    mensagem_final = (
        f"**Comparação de Troca:**\n"
        f"**Lado 1 ({lista_player1}):** {valor_player1:,} Beli\n"
        f"**Lado 2 ({lista_player2}):** {valor_player2:,} Beli\n"
        f"\n"
        f"{resultado}"
    )
    
    await ctx.send(mensagem_final)

bot.run(TOKEN)
