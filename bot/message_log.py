import discord
import json
import os
from discord.ext import commands

TOKEN = 'NTIwNTkxMDA3MjQzNDM2MDQy.Du2hAw.CQmLPikGINx_yOAG98VR2w_FuB8'
os.chdir(r'C:\\Users\\CSA\\PycharmProjects\\bot')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    with open("messages.txt", "a") as messages:
        messages.write(str('{}:{}'.format(author, content)) + "\n")


client.run(TOKEN)
