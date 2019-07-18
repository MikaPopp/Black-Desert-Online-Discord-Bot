import discord
from discord.ext import commands, tasks
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pytz
from datetime import datetime

config = json.loads(open("json/config.json").read())

guild_id = config["settings"]["guild_id"]
selfrole_channel_name = config["settings"]["selfrole_channel_name"]
boss_announcements_channel_name = config["settings"]["boss_announcements_channel_name"]
cest_time_channel_id = config["settings"]["cest_time_channel_id"]
emoji_list = ["🐦", "🐗", "🌳", "🐛", "🐉", "🐲", "👺", "👹", "🐳"]
role_name_list = ["Karanda", "Kzarka", "Offin", "Kutum", "Nouver", "Garmoth", "Quint", "Muraka", "Vell"]

chrome_path = config["settings"]["chrome_path"]
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_path, options = chrome_options)
url = "https://bdobosstimer.com/?&server="+config["settings"]["region"]

driver.get(url)

class bot_events(commands.Cog):

    def __init__(self, chamcham):
        self.chamcham = chamcham

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cham Cham is ready!")
        await self.chamcham.change_presence(status = discord.Status.do_not_disturb)
        await self.chamcham.change_presence(activity=discord.Game(name = "test"))
        self.check_boss_time.start()
        self.set_cest_channel_name.start()
        embed = discord.Embed (
            colour = discord.Colour.green()
        )
        embed.set_footer(text="Cham Cham - Version: 1.0")
        embed.set_image(url="https://www.blackdesertfoundry.com/wp-content/uploads/2015/08/%EC%9A%A96.jpg")
        selfrole_channel = discord.utils.get(self.chamcham.get_all_channels(), name=selfrole_channel_name)
        embed.description = f"""Getting a role is pretty simple, click on an emoji to get the corresponding role.\n
                                Karanda = {emoji_list[0]}\n
                                Kzarka = {emoji_list[1]}\n
                                Offin = {emoji_list[2]}\n
                                Kutum = {emoji_list[3]}\n
                                Nouver = {emoji_list[4]}\n
                                Garmoth = {emoji_list[5]}\n
                                Quint = {emoji_list[6]}\n
                                Muraka = {emoji_list[7]}\n
                                Vell = {emoji_list[8]}"""
        react_message = await selfrole_channel.send(embed=embed)
        for emoji in emoji_list:
            await react_message.add_reaction(emoji)

    @tasks.loop(seconds = 60)
    async def set_cest_channel_name(self):
        tz = pytz.timezone('Europe/Berlin')
        berlin_now = datetime.now(tz).strftime("%A, %H:%M (CEST)")
        guild = self.chamcham.get_guild(guild_id)
        cest_channel = discord.utils.get(self.chamcham.get_all_channels(), id=cest_time_channel_id)
        await cest_channel.edit(name=berlin_now)

    @tasks.loop(seconds = 60)
    async def check_boss_time(self):
        embed = discord.Embed (
            colour = discord.Colour.green()
        )
        embed.set_footer(text="Cham Cham - Version: 1.0")
        boss_announcements_channel = discord.utils.get(self.chamcham.get_all_channels(), name="boss-announcements")
        i = 0
        if "01:00:00" <= WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "10:00:00":
            time = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text
            time_minute = int(time[3]+time[4])
            time_minute_in_h = int(time_minute*100/60)
            await self.chamcham.change_presence(activity=discord.Game(name = "Boss in: "+time[1]+"."+str(time_minute_in_h)+"h"))
        elif "00:01:00" <= WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "00:59:59":
            time = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text
            await self.chamcham.change_presence(activity=discord.Game(name = "Boss in: "+time[3]+time[4]+"mins"))
        elif WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "00:00:59":
            await self.chamcham.change_presence(activity=discord.Game(name = "Boss in: now/dead"))
        try:
            guild = self.chamcham.get_guild(guild_id)
            if "00:15:00" <= WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "00:16:00":
                for x in role_name_list:
                    if WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text == x:
                        await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention} & {discord.utils.get(guild.roles, name = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text).mention}""")
                        embed.description = "Settle your horses, bosses will spawn in 15 minutes"
                        await boss_announcements_channel.send(embed=embed)
                    else:
                        i += 1
                if i == 9:
                    await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention}""")
                    embed.description = "Settle your horses, boss will spawn in 15 minutes"
                    await boss_announcements_channel.send(embed=embed)
                    i = 0
            elif "00:05:00" <= WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "00:06:00":
                for x in role_name_list:
                    if WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text == x:
                        await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention} & {discord.utils.get(guild.roles, name = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text).mention}""")
                        embed.description = "Prepare yourself and your buffs, bosses will spawn in 5 minutes"
                        await boss_announcements_channel.send(embed=embed)
                    else:
                        i += 1
                if i == 9:
                    await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention}""")
                    embed.description = "Prepare yourself and your buffs, boss will spawn in 5 minutes"
                    await boss_announcements_channel.send(embed=embed)
                    i = 0    
            elif WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "timer"))).text <= "00:01:00":
                for x in role_name_list:
                    if WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text == x:
                        await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention} & {discord.utils.get(guild.roles, name = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname1"))).text).mention}""")
                        embed.description = "Bosses will spawn any second"
                        await boss_announcements_channel.send(embed=embed)
                    else:
                        i += 1
                if i == 9:
                    await boss_announcements_channel.send(f"""{discord.utils.get(guild.roles, name=WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "bossname0"))).text).mention}""")
                    embed.description = "Boss will spawn any second"
                    await boss_announcements_channel.send(embed=embed)
                    i = 0 
                await asyncio.sleep(240)
                driver.refresh
        except Exception:
            driver.refresh
            pass

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        guild = self.chamcham.get_guild(guild_id)
        selfrole_channel = discord.utils.get(self.chamcham.get_all_channels(), name=selfrole_channel_name)
        selfrole_channel_id = selfrole_channel.id
        karanda_role = discord.utils.get(guild.roles, name = role_name_list[0])
        kzarka_role = discord.utils.get(guild.roles, name = role_name_list[1])
        offin_role = discord.utils.get(guild.roles, name = role_name_list[2])
        kutum_role = discord.utils.get(guild.roles, name = role_name_list[3])
        nouver_role = discord.utils.get(guild.roles, name = role_name_list[4])
        garmoth_role = discord.utils.get(guild.roles, name = role_name_list[5])
        quint_role = discord.utils.get(guild.roles, name = role_name_list[6])
        muraka_role = discord.utils.get(guild.roles, name = role_name_list[7])
        vell_role = discord.utils.get(guild.roles, name = role_name_list[8])
        if reaction.message.channel.id != selfrole_channel_id:
            return
        elif str(reaction.emoji) == emoji_list[0]:
            await user.add_roles(karanda_role)
        elif str(reaction.emoji) == emoji_list[1]:
            await user.add_roles(kzarka_role)
        elif str(reaction.emoji) == emoji_list[2]:
            await user.add_roles(offin_role)
        elif str(reaction.emoji) == emoji_list[3]:
            await user.add_roles(kutum_role)
        elif str(reaction.emoji) == emoji_list[4]:
            await user.add_roles(nouver_role)
        elif str(reaction.emoji) == emoji_list[5]:
            await user.add_roles(garmoth_role)
        elif str(reaction.emoji) == emoji_list[6]:
            await user.add_roles(quint_role)
        elif str(reaction.emoji) == emoji_list[7]:
            await user.add_roles(muraka_role)
        elif str(reaction.emoji) == emoji_list[8]:
            await user.add_roles(vell_role)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        guild = self.chamcham.get_guild(guild_id)
        selfrole_channel = discord.utils.get(self.chamcham.get_all_channels(), name=selfrole_channel_name)
        selfrole_channel_id = selfrole_channel.id
        karanda_role = discord.utils.get(guild.roles, name = role_name_list[0])
        kzarka_role = discord.utils.get(guild.roles, name = role_name_list[1])
        offin_role = discord.utils.get(guild.roles, name = role_name_list[2])
        kutum_role = discord.utils.get(guild.roles, name = role_name_list[3])
        nouver_role = discord.utils.get(guild.roles, name = role_name_list[4])
        garmoth_role = discord.utils.get(guild.roles, name = role_name_list[5])
        quint_role = discord.utils.get(guild.roles, name = role_name_list[6])
        muraka_role = discord.utils.get(guild.roles, name = role_name_list[7])
        vell_role = discord.utils.get(guild.roles, name = role_name_list[8])
        if reaction.message.channel.id != selfrole_channel_id:
            return
        elif str(reaction.emoji) == emoji_list[0]:
            await user.remove_roles(karanda_role)
        elif str(reaction.emoji) == emoji_list[1]:
            await user.remove_roles(kzarka_role)
        elif str(reaction.emoji) == emoji_list[2]:
            await user.remove_roles(offin_role)
        elif str(reaction.emoji) == emoji_list[3]:
            await user.remove_roles(kutum_role)
        elif str(reaction.emoji) == emoji_list[4]:
            await user.remove_roles(nouver_role)
        elif str(reaction.emoji) == emoji_list[5]:
            await user.remove_roles(garmoth_role)
        elif str(reaction.emoji) == emoji_list[6]:
            await user.remove_roles(quint_role)
        elif str(reaction.emoji) == emoji_list[7]:
            await user.remove_roles(muraka_role)
        elif str(reaction.emoji) == emoji_list[8]:
            await user.remove_roles(vell_role)

def setup(chamcham):
    chamcham.add_cog(bot_events(chamcham))