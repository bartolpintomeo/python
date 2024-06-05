import discord
from discord.ext import commands
from requests import get
from discord.ext.tasks import loop

channel_id = 1247845738898259991
token = "MTI0Nzg1NTkxOTI5MTgyNjE4Ng.GMy5Ss.DYRvj-AIMXINsKrPqoeBVsfLrHYFNyHkRptr8I"

intents = discord.Intents.default()
intents.presences = True
intents.members = True
codicemod="mod.txt"

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    invia_quotazione.start()


@loop(hours=24) 
async def invia_quotazione():
    respond = get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-EUR")
    prezzo_attuale = float(respond.json()["data"]["buy"])
    canale = bot.get_channel(channel_id)
    testo = f"Il prezzo di 1 BTC è {prezzo_attuale} €"
    await canale.send(testo)


@bot.event
async def on_message(messaggio):
    autore = messaggio.author
    testo = messaggio.content
    canale = messaggio.channel
    if autore==bot.user:
        return
    await canale.send(f"Ciao {autore.name} ;P")
    if testo.startswith("!aggiungi"):
        codicemod = testo.split()[1]
        return
    if testo.startswith("!mostra"):
        await canale.send(codicemod)
bot.run(token)