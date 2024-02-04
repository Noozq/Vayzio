import discord 
from discord.ext import commands
import os
import json
import colorama
from colorama import Fore
import dotenv
from dotenv import load_dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
version = str(os.getenv("VERSION"))


def get_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
client = commands.Bot(command_prefix = get_prefix, intents=intents)
@client.event
async def on_ready():
  print(Fore.RED + 
  '''
  ██╗   ██╗ █████╗ ██╗   ██╗███████╗██╗ ██████╗ 
  ██║   ██║██╔══██╗╚██╗ ██╔╝╚══███╔╝██║██╔═══██╗
  ██║   ██║███████║ ╚████╔╝   ███╔╝ ██║██║   ██║
  ╚██╗ ██╔╝██╔══██║  ╚██╔╝   ███╔╝  ██║██║   ██║
   ╚████╔╝ ██║  ██║   ██║   ███████╗██║╚██████╔╝
    ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝ ╚═════╝ 
                                              '''
  )

@client.event
async def on_guild_join(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes[str(guild.id)] = 'v!'

  with open('config/prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
  with open('config/prefixes.json', 'r') as f:
    prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('config/prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

client.run(token)
