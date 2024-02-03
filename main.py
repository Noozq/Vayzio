import discord 
from discord.ext import commands
import os
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix = get_prefix, intents=intents)

client.run(token)