import discord
from discord.ext import commands
from numpy.random import choice

class bot_command_upgrade(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.command()
    async def upgrade(self, ctx, item : str, base : str, failstacks : int, tries : int = 1):
        embed = discord.Embed (
            titel = "upgrade chance",
            colour = discord.Colour.green()
        )
        embed.set_footer(text="Cham Cham - Version: 1.0")
        softcap_fs = 0
        pre_softcap = 0
        post_softcap = 0
        chance = 0
        if base == "duo" and (item == "armor" or item == "armour"):
            softcap_fs = 82
            base = 7.692
        elif base == "tri" and (item == "armor" or item == "armour"):
            softcap_fs = 102
            base = 6.25
        elif base == "tet" and (item == "armor" or item == "armour"):
            softcap_fs = 340
            base = 2
        elif base == "pen" and (item == "armor" or item == "armour"):
            softcap_fs = 2323
            base = 0.3
        elif base == "pri" and item == "acc":
            softcap_fs = 18
            base = 25
        elif base == "duo" and item == "acc":
            softcap_fs = 40
            base = 10
        elif base == "tri" and item == "acc":
            softcap_fs = 44
            base = 7.5
        elif base == "tet" and item == "acc":
            softcap_fs = 110
            base = 2.5
        elif base == "pen" and item == "acc":
            softcap_fs = 590
            base = 0.5
        if failstacks > softcap_fs:
            pre_softcap = base + (softcap_fs*(base/10))
            post_softcap = (failstacks-softcap_fs)*(base) 
            chance = pre_softcap+post_softcap
        else:
            chance = base + (failstacks*(base/10))
        if (chance > 90):
            chance = 90
        count = 0
        description = "Your chance to upgrade your item is: "+str(round(chance, 2))+"%\n\n"
        for x in range(tries):
            draw = choice(["Success", "Failure"], 1, p=[chance/100, (100-chance)/100])
            count += 1
            success_check = False
            if draw == "Success":
                description += "You have successfully upgraded your item!\nYou needed a total of "+str(count)+" tries."
                embed.set_thumbnail(url="https://b.catgirlsare.sexy/heVX.png")
                success_check = True
                break
        if success_check == False:
            description += "You have failed to upgrade your item ("+str(count)+" times)."
            embed.set_thumbnail(url="https://b.catgirlsare.sexy/wNlC.png")
        embed.description = description
        await ctx.send(embed = embed)

    @upgrade.error
    async def upgrade_error(self, ctx, error):
        embed = discord.Embed (
            titel = "upgrade command error",
            colour = discord.Colour.green()
        )
        embed.set_footer(text="Cham Cham - Version: 1.0")
        if isinstance(error, commands.MissingRequiredArgument):
            embed.description = "You are missing a required argument\n.upgrade [item] [base] [failstacks]"
            await ctx.send(embed = embed)

def setup(chamcham):
    chamcham.add_cog(bot_command_upgrade(chamcham))