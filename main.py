import discord
from discord.ext.commands import Bot
from discord.ext import commands
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
        await message.channel.send('pong')
    # await Bot.process_commands(message)

client.run('MTA0MjE2OTAzMjQ4MjIzNDM4OA.G2mD0i.xoTKaR5_EfbwNlTtbgbjeb_5dVlm1altycl3f4')

# import discord
# import os
# from discord.ext import commands
# from discord.ext.commands import Bot

# case_insensitive=True

# client = discord.Client(intents=discord.Intents.default())
# bot = commands.Bot(
#   command_prefix="!",
#   intents=discord.Intents(members=True, messages=True, guilds=True)
# )

# @client.event
# async def on_ready():
#     print('logged in as {0.user}!'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

# bot = Bot("!")

# @bot.command(name="ping", description= "Find out!")
# async def ping(ctx):
#   await ctx.send("Pong!")
# client.run(os.getenv('TOKEN'))


