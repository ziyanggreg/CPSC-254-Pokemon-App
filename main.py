import discord
import requests
import json

from discord.ext.commands import Bot
from discord.ext import commands
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="--",case_insensitive=True,intents=intents)
bot.remove_command("help")
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith("!pokemon"):
        card = Card.find(message.content[9:])
        await message.channel.send(card.images.large)

client.run('MTA0MjE2OTAzMjQ4MjIzNDM4OA.GEt-rO.uRti9mH9aez0kEg75FHJgEGXXpmfqAcWdjJO_4')
