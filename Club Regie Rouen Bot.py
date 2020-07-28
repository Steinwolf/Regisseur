# v0.2
import discord
from discord.ext import commands

f = open("token.txt", "r")

TOKEN = f.read()

bot = commands.Bot(command_prefix='!', description='A bot to manage the "Club regie Rouen" discord guild')
bot.remove_command('help')


@bot.command()
async def clear(ctx, value=None):

    channel = ctx.channel
    author = ctx.author
    message_history = ctx.history

    if value is None:
        msg = 'You did not specify how many message you wanted to delete {0}.'.format(author.mention)
        channel.send(msg)

    elif value == "all":
        msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
        value = 10000

    else:
        msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
        value = int(value) + 1

    async with ctx.channel.typing():
        async for m in message_history(limit=int(value) + 1):
            await m.delete()
        await channel.send(msg)


@bot.command()
async def react(ctx, emote):

    channel = ctx.channel

    msg = await channel.send("message")
    await msg.add_reaction(emote)


@bot.command()
async def role(ctx):

    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    role_name = discord.utils.get(guild.roles, name="Bot testing")

    await author.add_roles(role_name)
    msg = 'The role {0} was added to {1}'.format(role_name.mention, author.mention)
    await channel.send(msg)


#Embeded help with list and details of commands
@bot.command(pass_context=True)
async def help(ctx):

    author = ctx.author
    embedded_message = discord.Embed(
        colour=discord.Colour.green()
    )

    embedded_message.set_author(name='Help : list of commands available')
    embedded_message.add_field(name='clear', value='Delete message. Take a positive int as argument', inline=False)
    embedded_message.add_field(name='react', value='Test to get a reaection. Take a emote as argument', inline=False)
    embedded_message.add_field(name='role', value='Give the role "Bot Testing toembedded_messagethe author', inline=False)

    await author.send(embed=embedded_message)


@bot.event
async def on_ready():

    bot_name = bot.user.name
    bot_id = bot.user.id
    package_version = discord.__version__
    activity = '"!help" pour savoir utiliser le bot"'
    msg = '\nLogged in as: {0} - {1}\nVersion: {2}\n'.format(bot_name, bot_id, package_version)

    print(msg)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity))
    print('Successfully running')


@bot.event
async def on_command_error(ctx, error):

    msg = 'You have misstype the command or the argument, if the problem persist,' \
          ' contact an admin with the error code {0}'.format(error)

    await ctx.send(msg)

bot.run(TOKEN)
