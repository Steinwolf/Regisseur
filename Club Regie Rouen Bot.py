# v0.3
import discord
from discord.ext import commands
from dontknowhowtonameit import file_reader as fr

# initiate bot information
bot = commands.Bot(command_prefix='!', description='A bot to manage the "Club regie Rouen" discord guild')
bot.remove_command('help')


# Begin define bot command
@bot.command()
async def clear(ctx, value):

    channel = ctx.channel
    author = ctx.author
    message_history = ctx.history

    # Define display message and value depending of argument
    if value == "all":
        msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
        value = 10000

    else:
        msg = '{0} messages has been deleted by {1}'.format(value, author.mention)
        value = int(value) + 1

    # Delete messages
    async with ctx.channel.typing():
        async for m in message_history(limit=int(value)):
            await m.delete()
        await channel.send(msg)


@bot.command()
async def lockdown(ctx, channel_given=None):

    guild = ctx.guild
    if channel_given is None:
        channel = ctx.channel
    elif channel_given[0] == '<':
        channel = discord.utils.get(guild.text_channels, mention=channel_given)
    else:
        channel = discord.utils.get(guild.text_channels, name=channel_given)
    role_locked = discord.utils.get(guild.roles, name="Membre")

    await channel.set_permissions(role_locked, send_messages=False)

    """msg = 'This channel has been lockdown by Admins. You cannot write until further ado'
    await channel.send(msg)"""



@bot.command()
async def react(ctx):

    channel = bot.get_channel(738175849592913980)
    msg = await channel.send("message")

    await msg.add_reaction('😀')
    await msg.add_reaction('😃')
    await msg.add_reaction('🙂')
    await msg.add_reaction('😊')


@bot.command()
async def role(ctx, role_given, person_given=None):

    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author

    # Begin parsing argument
    if person_given is None:
        person_name = author
    else:
        person_name = discord.utils.get(guild.members, mention=person_given)

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
async def help(ctx, command=None):

    author = ctx.author
    embedded_message = discord.Embed(
        colour=discord.Colour.green()
    )

    if command is None:

        # Create embedded message
        embedded_message.set_author(name='help : list of commands available')
        """embedded_message.add_field(name='clear', value='Delete message. Take a positive int as argument', inline=False)
        embedded_message.add_field(name='react', value='Test to get a reaction. Take a emote as argument', inline=False)
        embedded_message.add_field(name='role', value='Give the role "Bot Testing to the author', inline=False)"""
        embedded_message.add_field(name='WIP', value='Work In Progress, What did you expect ?', inline=False)
        # Send embedded message
        await author.send(embed=embedded_message)
    else:

        msg = fr.helper[command].split('?')

        # Create embedded message
        embedded_message.set_author(name='help : {0}'.format(command))
        for i in range(len(msg)):
            embedded_message.add_field(name=str(i+1), value=msg[i], inline=False)

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
    msg = 'You have misstype the command or the argument, try to use "!help"\n' \
          'if the problem persist, contact an admin with the error code ""{0}"" {1}'.format(error, author.mention)

    # Send error message to user
    await channel.send('error')
    await author.send(msg)


# Public Welcome
@bot.event
async def on_member_join(member):
    # channel bottesting
    channel = bot.get_channel(739862361506185307)
    await member.send("Bienvenue dans le club régie !")
    await channel.send('**{0}** a rejoint le club régie !'.format(member.mention))


# Mod Leave Announcement
@bot.event
async def on_member_remove(member):
    # channel bottesting
    channel = bot.get_channel(739862361506185307)
    await channel.send('**' + member.mention + '** viens de quitter le serveur du club Régie.')


@bot.event
async def on_raw_reaction_add(p):
    if p.message_id == 738179495118241798:
        msg = 'Why the fuck did you reacted with {0} beach (always kid friendly)'.format(p.emoji)
        await p.member.send(msg)


@bot.event
async def on_raw_reaction_remove(p):

    guild = bot.get_guild(p.guild_id)
    member = guild.get_member(p.user_id)

    if p.message_id == 738179495118241798:
        msg = 'Why the fuck did you REMOVED IT ???'
        await member.send(msg)


# End define bot event

# Start bot
bot.run(fr.TOKEN)
