import discord
from discord.ext import commands

class bot_command_marketgain(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.command()
    async def marketgain(self, ctx, sell_price : int, valuepack : str):
        embed = discord.Embed (
            titel = "Market money gain",
            colour = discord.Colour.green()
        )
        embed.set_thumbnail(url="https://b.catgirlsare.sexy/Yb6M.jpg")
        embed.set_footer(text="Cham Cham - Version: 1.0")
        if valuepack == "y" or valuepack == "yes":
            money_gain = sell_price*0.845
            embed.description = "You will gain a total amount of: "+str(money_gain)+" Silvers"
            await ctx.send(embed=embed)
        elif valuepack == "n" or valuepack == "no":
            money_gain = sell_price*0.65
            embed.description = "You will gain a total amount of: "+str(money_gain)+" Silvers"
            await ctx.send(embed=embed)
        else: 
            embed.description = """You seem to have used a wrong parameter for the valuepack, 
            check the help command for more information"""
            await ctx.send(embed=embed)

def setup(chamcham):
    chamcham.add_cog(bot_command_marketgain(chamcham))