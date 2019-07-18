import discord
from discord.ext import commands
import json

config = json.loads(open("json/config.json").read())
region = config["settings"]["region"]

class bot_command_timetable(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.command()
    async def timetable(self, ctx):
        embed = discord.Embed (
            titel = "Timetable",
            colour = discord.Colour.green()
        )
        if region == "eu":
            embed.set_image(url="https://b.catgirlsare.sexy/0iCz.png")
            await ctx.send(embed=embed)
        elif region == "kr":
            embed.set_image(url="https://b.catgirlsare.sexy/6Hb4.png")
            await ctx.send(embed=embed)
        elif region == "mena":
            embed.set_image(url="https://b.catgirlsare.sexy/x40R.png")
            await ctx.send(embed=embed)
        elif region == "jp":
            embed.set_image(url="https://b.catgirlsare.sexy/bUyb.png")
            await ctx.send(embed=embed)
        elif region == "ru":
            embed.set_image(url="https://b.catgirlsare.sexy/ifJa.png")
            await ctx.send(embed=embed)
        elif region == "na":
            embed.set_image(url="https://b.catgirlsare.sexy/ua1S.png")
            await ctx.send(embed=embed)
        elif region == "th":
            embed.set_image(url="https://b.catgirlsare.sexy/d04Y.png")
            await ctx.send(embed=embed)
        elif region == "sea":
            embed.set_image(url="https://b.catgirlsare.sexy/j3MA.png")
            await ctx.send(embed=embed)
        elif region == "sa":
            embed.set_image(url="https://b.catgirlsare.sexy/kOLY.png")
            await ctx.send(embed=embed)
        elif region == "tw":
            embed.set_image(url="https://b.catgirlsare.sexy/4976.png")
            await ctx.send(embed=embed)
        elif region == "xbox-na":
            embed.set_image(url="https://b.catgirlsare.sexy/9nY9.png")
            await ctx.send(embed=embed)
        elif region == "xbox-eu":
            embed.set_image(url="https://b.catgirlsare.sexy/1mQd.png")
            await ctx.send(embed=embed)
        else:
            embed.description = "I couldn't find a timetable for your region, maybe you have a typo in your config file?"
            await ctx.send(embed=embed)

def setup(chamcham):
    chamcham.add_cog(bot_command_timetable(chamcham))