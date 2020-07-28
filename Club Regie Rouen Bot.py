# Work with Python 3.6
import discord
from discord.ext import commands

# will get this in a object form


f = open("token.txt", "r")

TOKEN = f.read()

bot = commands.Bot(command_prefix='!')


@bot.command()
async def role(ctx):
    role_name = discord.utils.get(ctx.guild.roles, name="Bot testing")
    await ctx.author.add_roles(role_name)
    msg = 'The role {0} was added to {1}'.format(role_name.mention, ctx.author.mention)
    await ctx.send(msg)


@bot.command()
async def clear(ctx, value=-1):

    if value == -1:
        msg = 'You did not specify how many message you wanted to delete {0}.'.format(ctx.author.mention)
        ctx.send(msg)

    else:
        async with ctx.channel.typing():
            async for m in ctx.history(limit=value + 1):
                await m.delete()

            msg = '{0} messages has been deleted {1.author.mention}'.format(value, ctx)

            await ctx.send(msg)


@bot.command()
async def react(ctx, emote):

    msg = await ctx.send("message")

    await msg.add_reaction(emote)


@bot.event
async def on_ready():

    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                        name="\"!help\" pour savoir utiliser le bot"))

    print('Successfully running')

bot.run(TOKEN)
