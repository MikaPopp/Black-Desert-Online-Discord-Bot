import discord
from discord.ext import commands
import os
import json

config = json.loads(open("json/config.json").read())
token = config["settings"]["token"]

chamcham = commands.Bot(command_prefix = config["settings"]["prefix"])

#@chamcham.command()
#async def load(ctx, extension):
#    chamcham.load_extension(f"cogs.{extension}")
#    print("loaded cogs")

#@chamcham.command()
#async def unload(ctx, extension):
#    chamcham.unload_extension(f"cogs.{extension}")
#    print("unloaded cogs")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        chamcham.load_extension(f"cogs.{filename[:-3]}")
        
chamcham.run(token)
