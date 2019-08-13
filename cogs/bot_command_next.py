import discord
from discord.ext import commands
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

config = json.loads(open("json/config.json").read())

region = config["settings"]["region"]
boss_name_list = ["Karanda", "Kzarka", "Offin", "Kutum", "Nouver", "Garmoth", "Quint", "Muraka", "Vell"]

chrome_path = config["settings"]["chrome_path"]
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_path, options = chrome_options)
url = "https://bdobosstimer.com/?&server="+region

driver.get(url)

class bot_command_next(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.command()
    async def next(self, ctx):
        embed = discord.Embed (
            titel = "Next Boss",
            colour = discord.Colour.green()
        )
        embed.set_footer(text="Cham Cham - Version: 1.0")
        i = 0
        boss_one = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text
        boss_two = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text
        for x in boss_name_list:
            if boss_two == x:
                embed.description = f"{boss_one}"
                embed.set_thumbnail(url="https://bdobosstimer.com/img/bosses/"+boss_one.lower()+".png")
                await ctx.send(embed=embed)
                embed.description = f"{boss_two}"
                embed.set_thumbnail(url="https://bdobosstimer.com/img/bosses/"+boss_two.lower()+".png")
                await ctx.send(embed=embed)
            else:
                i += 1
        if i == 9:
            embed.description = f"{boss_one}"
            embed.set_thumbnail(url="https://bdobosstimer.com/img/bosses/"+boss_one.lower()+".png")
            await ctx.send(embed=embed)
            i = 0

def setup(chamcham):
    chamcham.add_cog(bot_command_next(chamcham))