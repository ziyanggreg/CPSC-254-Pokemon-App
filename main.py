import discord
from discord.ext.commands import Bot
from discord.ext import commands
from pokemontcgsdk import Card
# import os

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

    if message.author == client.user:
        return
        
    if message.content == "ping":
        print("pong")
        card = Card.find('xy1-1')
        await message.channel.send(card.name)

client.run('MTA0MjE2OTAzMjQ4MjIzNDM4OA.Gzx9cU.mMhL6oyS3JQY7-vr6HV6uJSJKorPXsLn5lwTBU')
