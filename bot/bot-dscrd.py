import discord
from discord.ext import commands
import random
import os

TOKEN = 'NTIwNTkxMDA3MjQzNDM2MDQy.Du2hAw.CQmLPikGINx_yOAG98VR2w_FuB8'
client = commands.Bot(command_prefix='!')
os.chdir(r'C:\Users\CSA\PycharmProjects\bot')


# Replies
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!guess'):

            if message.content.startswith('!guess'):
                await client.send_message(message.channel, 'Guess a number between 1 to 10')

                def guess_check(m):
                    return m.content.isdigit()
                guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
                answer = random.randint(1, 10)
                if guess is None:
                    fmt = 'Sorry, you took too long. It was {}.'
                    await client.send_message(message.channel, fmt.format(answer))
                    return
                if int(guess.content) == answer:
                    await client.send_message(message.channel, 'You are right!')
                else:
                    await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))

    elif message.content.startswith('!hello'):

            if message.content.startswith('!hello'):
                msg = 'Hello {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)

    elif message.content.startswith('!ping'):
        msg = '{0.author.mention} pong!'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!status'):
        msg = 'Servers are online  {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!shop'):
        msg = 'To buy more money, head to our shop: www.shop.com {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


client.run(TOKEN)
client = commands.Bot(command_prefix='!')
os.chdir(r'C:\Users\CSA\PycharmProjects\P3.6CommieBot')

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member: discord.Member):
    # Says when a member joined.
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    # Says if a user is cool.
    # In reality this just checks if a subcommand is being invoked.

    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    # Is the bot cool?
    await bot.say('Yes, the bot is cool.')

bot.run(TOKEN)
