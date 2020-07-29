# v0.3
import discord
from discord.ext import commands

# Read the token --- made to hide the token in Github --- Hi Git-user 😀
f = open("token.txt", "r")
TOKEN = f.read()

# initiate bot information
bot = commands.Bot(command_prefix='!', description='A bot to manage the "Club regie Rouen" discord guild')
bot.remove_command('help')


# Begin define bot command
@bot.command()
async def clear(ctx, value=None, *, end=None):

    channel = ctx.channel
    author = ctx.author

    if end is not None and end[-1] == '?':
        msg = '!clear(value), value argument must be an positive int'
        await author.send(msg)
    elif value == '?':
        msg = '!clear(value), value argument must be an positive int'
        await author.send(msg)
    else:

        message_history = ctx.history

        # Define display message and value depending of argument
        if value is None:
            msg = 'You did not specify how many message you wanted to delete {0}.'.format(author.mention)
            channel.send(msg)

        elif value == "all":
            msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
            value = 10000

        else:
            msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
            value = int(value) + 1

        # Delete messages
        async with ctx.channel.typing():
            async for m in message_history(limit=int(value) + 1):
                await m.delete()
            await channel.send(msg)


@bot.command()
async def react(ctx, emote):

    channel = ctx.channel

    # / Need upgrade / and comment tho
    msg = await channel.send("message")
    await msg.add_reaction(emote)


@bot.command()
async def role(ctx, role_given, person_given=None):

    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author

    # Begin parsing argument
    if person_given is None:
        person_name = author
    elif person_given[0] == '<':
        person_name = discord.utils.get(guild.members, mention=person_given)
    else:
        person_name = discord.utils.get(guild.members, name=person_given)

    if role_given[0] == '<':
        role_name = discord.utils.get(guild.roles, mention=role_given)
    else:
        role_name = discord.utils.get(guild.roles, name=role_given)
    # End parsing argument

    # Give specific role to user / Need upgrade
    await person_name.add_roles(role_name)
    msg = 'The role {0} was added to {1}'.format(role_name.mention, person_name.mention)
    await channel.send(msg)


@bot.command(pass_context=True)
async def help(ctx):

    author = ctx.author
    embedded_message = discord.Embed(
        colour=discord.Colour.green()
    )

    # Create embedded message
    embedded_message.set_author(name='Help : list of commands available')
    embedded_message.add_field(name='clear', value='Delete message. Take a positive int as argument', inline=False)
    embedded_message.add_field(name='react', value='Test to get a reaection. Take a emote as argument', inline=False)
    embedded_message.add_field(name='role', value='Give the role "Bot Testing to the author', inline=False)

    # Send embedded message
    await author.send(embed=embedded_message)


# End define bot command

# Begin define bot event
@bot.event
async def on_ready():

    bot_name = bot.user.name
    bot_id = bot.user.id
    package_version = discord.__version__
    activity = '"!help" pour savoir utiliser le bot"'
    msg = '\nLogged in as: {0} - {1}\nVersion: {2}\n'.format(bot_name, bot_id, package_version)

    # print bot info and change activity
    print(msg)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity))
    print('Successfully running')


@bot.event
async def on_command_error(ctx, error):

    channel = ctx.channel
    author = ctx.author
    msg = 'You have misstype the command or the argument ""{0}"", try to use "!help"\n' \
          'if the problem persist, contact an admin with the error code {1}'.format(error, author.mention)

    # Send error message to user
    await channel.send('error')
    await author.send(msg)


# End define bot event

# Start bot
bot.run(TOKEN)
