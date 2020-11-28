'''
Current functionality of Hippo bot

Commands:
>help : lists commands
>hippofact : gives a random hippo fact
>insult : insults your enemy
>uwuify "message" : uwuifies your message 
>jarjar : grabs a random image link to jarjar from jarjarbase.py

Special Sauce:
- Robots: responds to messages with "robot" or "robots" in it with a :norobots: emoji
- Probby: 1/10 chance of responding to messages with "probby" in it
- Collection: 1/10 change of responding to general grevious collection gif to attachments
- @A Pygmy Hippo: responds to @A Pygmy Hippo with an annoyed hippo
- Nagging : occasionally tells afora to study

'''

import discord
import hippotoken
import jarjarbase
import hippofacts
import insults
import uwuifier as uwf
import random
from discord.ext import commands



bot = commands.Bot(command_prefix='>') #define command decorator
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def help(ctx):
    await ctx.send("No one can help you now. \nBut maybe hippo can entertain you... \n>hippofact\n>insult 'name'\n>uwuify 'message'\n>jarjar")

@bot.command()
async def hippofact(ctx):
    hippoint = random.randint(0,len(hippofacts.hippofactlist)-1)
    await ctx.send(hippofacts.hippofactlist[hippoint])

@bot.command()
async def insult(ctx, arg):
    insultstring =""
    instart = insults.insultstarters[random.randint(0,len(insults.insultstarters)-1)]
    inend = insults.insultslist[random.randint(0,len(insults.insultslist)-1)]
    insultstring = instart + str(arg) + inend
    print(insultstring)
    await ctx.send(insultstring)

@bot.command()
async def jarjar(ctx):
    if (ctx.author == jarjarbase.lastjarjarer):
        await ctx.send("You have had enough Jar Jar " + str(ctx.author))
    else:
        jajaint = random.randint(0,4)
        await ctx.send(jarjarbase.jarjars[jajaint])
        jarjarbase.lastjarjarer = ctx.author

@bot.command()
async def uwuify(ctx, *, arg):
    towuwu = arg
    print (type(towuwu))

    await ctx.send(uwf.uwu(arg))

@bot.event
async def on_message(message):
    if (('robots' in message.content or 'robot' in message.content)and str(message.author) != "Hippo Bot#4735"):
        #print('fuck your robots')
        print('responding to' + str(message.author))
        
        #await message.channel.send("fuck your robots")
        await message.add_reaction("<:norobots:782011627326144525>")
        # Do stuff here
    elif (('probby' in message.content or 'Probby' in message.content) and str(message.author) != "Hippo Bot#4735"):
        triggerint = random.randint(0,9)
        if (triggerint == 1):
            await message.channel.send("Probby?!? :eyes: better fuckin secure my guarenteed habitables")
    elif (message.attachments and str(message.author) != "Hippo Bot#4735"):
        #print(message.attachments)
        triggerint = random.randint(0,9)
        if (triggerint == 1):
            await message.channel.send("https://i.imgur.com/b4Pk9yv.gif")
    elif (message.mentions):
        if (str(message.mentions[0]) == "A Pygmy Hippo#4285"):
            await message.channel.send("https://i.imgur.com/IthbwWM.jpg")
    elif (str(message.author) == "Afora#7481"):
        triggerint = random.randint(0,3)
        if (triggerint == 1):
            await message.channel.send("Hey Afora why aren't you studying?")

    await bot.process_commands(message)

bot.run(hippotoken.token)
