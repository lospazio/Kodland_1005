import discord, os, random
from discord.ext import commands

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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def leggi(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def scrittura(ctx):
    await ctx.send("Cosa vuoi scrivere nel file?")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)
        with open('text.txt', 'w', encoding='utf-8') as f:
            f.write(msg.content)
        await ctx.send("Testo salvato con successo!")
    except:
        await ctx.send("Non hai scritto nulla in tempo.")

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/memes/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animali(ctx):
    img_name = random.choice(os.listdir("images/animali"))
    with open(f'images/animali/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def anime(ctx):
    img_name = random.choice(os.listdir("images/anime"))
    with open(f'images/anime/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("IL TUO TOKEN")
