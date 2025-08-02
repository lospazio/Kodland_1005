import discord, os, random, time
from discord.ext import commands

idee_inquinamento = [
    "Promuovere l'uso dei trasporti pubblici per ridurre le emissioni.",
    "Sensibilizzare sull'importanza del riciclo dei rifiuti.",
    "Ridurre l'uso della plastica monouso nei supermercati.",
    "Incoraggiare l'uso di energie rinnovabili come il solare e l'eolico.",
    "Più alberi per migliorare la qualità dell'aria nelle città.",
    "Campagne contro l'inquinamento dei mari da parte delle industrie.",
    "Utilizzare prodotti biodegradabili e detergenti ecologici.",
    "Educare i giovani sul rispetto per l’ambiente nelle scuole.",
    "Creare piste ciclabili sicure per ridurre il traffico urbano.",
    "Sostenere leggi più severe contro le industrie inquinanti."
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def inquinamento(ctx):
    idea = random.choice(idee_inquinamento)
    time.sleep(0.5)
    await ctx.send(idea)

@bot.command()
async def inquinamento2(ctx):
    img_name = random.choice(os.listdir("images/inquinamento"))
    with open(f'images/inquinamento/{img_name}', 'rb') as f:
            picture = discord.File(f)
    time.sleep(0.5)
    await ctx.send(file=picture)

@bot.command()
async def inquinamento3(ctx):
    with open('inquinamento.txt', 'r', encoding='utf-8') as f:
        time.sleep(0.5)
        await ctx.send(f.read())

@bot.command()
async def procedura(ctx):
    parte1 = (
        "**🧠 Procedura per risolvere l’inquinamento da plastica nei fiumi**\n\n"
        "1️⃣ **Identificazione del punto critico**\n"
        "- Mappa i tratti del fiume più colpiti (con droni o segnalazioni).\n"
        "- Registra quantità e tipo di rifiuti trovati.\n\n"
        "2️⃣ **Intervento immediato**\n"
        "- Task force con volontari, scuole e comuni per pulizia veloce.\n"
        "- Barriere galleggianti strategiche per bloccare la plastica a monte."
    )

    parte2 = (
        "3️⃣ **Prevenzione attiva**\n"
        "- Cestini intelligenti con sensori pieni.\n"
        "- Telecamere per beccare i furbetti che scaricano abusivamente.\n\n"
        "4️⃣ **Educazione mirata**\n"
        "- Campagne nelle scuole e sui social.\n"
        "- Premia chi ricicla (es. cashback ecologico).\n\n"
        "5️⃣ **Monitoraggio costante**\n"
        "- Ispezione ogni 3 mesi, con analisi dei risultati.\n"
        "- Se migliora ➜ espansione. Se peggiora ➜ più controlli."
    )

    parte3 = (
        "6️⃣ **Tecnologia a supporto**\n"
        "- AI per tracciare l'origine dei rifiuti nel fiume.\n"
        "- Robot galleggianti che raccolgono la plastica 24/7.\n\n"
        "🎯 **Risultato:** Fiume pulito, cittadini svegli, ambiente rispettato. Zero chiacchiere, solo azione. 🐟🚫♻️"
    )

    time.sleep(0.5)
    await ctx.send(parte1)
    time.sleep(1.5)
    await ctx.send(parte2)
    time.sleep(1.5)
    await ctx.send(parte3)



bot.run("IL TUO TOKEN")
