# Work with Python 3.6
import discord
f = open("token.txt", "r")

TOKEN = f.read()

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
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

    """if message.content.startswith("!react"):

        breaking = message.content.split(" ")

        e = breaking[1]

        msg = await message.channel.send("message")

        await msg.add_reaction(e)

        await message.channel.send(msg.reaction)"""



@client.event
async def on_ready():

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                           name="\"!help\" pour savoir utiliser le bot"))

    print('Logged in as ' + client.user.name)

client.run(TOKEN)
