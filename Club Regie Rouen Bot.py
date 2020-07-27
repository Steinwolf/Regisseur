# Work with Python 3.6
import discord
from discord.ext import commands

# will get this in a object form


f = open("token.txt", "r")

TOKEN = f.read()

bot = commands.Bot(command_prefix='!')


@bot.command()
async def role(ctx, role=None, personne=None):

    if role is None:

        msg = '{0.author.mention} please state a role.'.format(ctx)
        await ctx.send(msg)

    else:
        role_exist = False

        for f in ctx.guild.roles:
            if role == f:
                role_exist = True

        if role_exist is False:

            msg = '{0.author.mention} the role you mentionned doesn\'t exist. Please try again'.format(ctx)
            await ctx.send(msg)
        else:
            if personne is None:
                await ctx.author.add_roles(role)
                msg = 'The role : "{0}" has been accorded to {1}'.format(role, ctx.author)
                await ctx.send(msg)
            else:
                await personne.add_roles(role)
                msg = 'The role : "{0}" has been accorded to {1}'.format(role, personne)
                await ctx.send(msg)



    """if message.content.startswith('!help'):
        msg = 'Hello, i am currently in development, but i will be ready sooner or later (probably later)' \
              ' i will be back to you {0.author.mention}'.format(message)
        await message.author.send(msg)

    if message.content.startswith("!role"):

        role = discord.utils.get(message.guild.roles, name="Bot testing")
        await message.channel.send(role)
        await message.author.add_roles(role)

    if message.content.startswith("!clear"):

        breaking = message.content.split(" ")

        if len(breaking) < 2:
            msg = 'Can you tell me how many message must i delete {0.author.mention}'.format(message)
            await message.channel.send(msg)
        else:
            value = int(breaking[1])
            async with message.channel.typing():
                async for m in message.channel.history(limit=value+1):
                    await m.delete()

                msg = '{0} messages has been deleted {1.author.mention}'.format(value, message)

                await message.channel.send(msg)
"""
    """if message.content.startswith("!react"):

        breaking = message.content.split(" ")

        e = breaking[1]

        msg = await message.channel.send("message")

        await msg.add_reaction(e)

        await message.channel.send(msg.reaction)"""


@bot.event
async def on_ready():

    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name="\"!help\" pour savoir utiliser le bot"))

    print('Successfully running')

bot.run(TOKEN)
