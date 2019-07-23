import discord
from discord.ext import commands
import os
import json

config = json.loads(open("json/config.json").read())
token = config["settings"]["token"]

chamcham = commands.Bot(command_prefix = config["settings"]["prefix"])

@chamcham.command()
async def load(ctx, extension):
    if ctx.message.author.guild_permissions.administrator:
        chamcham.load_extension(f"cogs.{extension}")
        print("loaded cogs")
    else:
        print("no permission")

@chamcham.command()
async def unload(ctx, extension):  
    if ctx.message.author.guild_permissions.administrator:
        chamcham.unload_extension(f"cogs.{extension}")
        print("unloaded cogs")
    else:
        print("no permission")

@chamcham.command()
async def reload(ctx, extension):  
    if ctx.message.author.guild_permissions.administrator:
        chamcham.unload_extension(f"cogs.{extension}")
        chamcham.load_extension(f"cogs.{extension}")
        print("reloaded cogs")
    else:
        print("no permission")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        chamcham.load_extension(f"cogs.{filename[:-3]}")
        
chamcham.run(token)
