import discord
from discord.ext import commands

class bot_command_timetable(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.command()
    async def timetable(self, ctx):
        embed = discord.Embed (
            titel = "Timetable",
            colour = discord.Colour.green()
        )
        embed.set_image(url="https://b.catgirlsare.sexy/7quZ.jpg")
        await ctx.send(embed=embed)

def setup(chamcham):
    chamcham.add_cog(bot_command_timetable(chamcham))