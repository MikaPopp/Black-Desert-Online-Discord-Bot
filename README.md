# Black Desert Online Discord Bot
![Image of Yaktocat](https://b.catgirlsare.sexy/FuOZ.png)

## Table of Contents:
1. About
2. Features
3. Setup
4. Miscellaneous

## 1. About

You might wonder why I made such a Discord bot, since there are many sites where you can information about boses, their spawn time and even the whole spawn timetable. When I played Black Desert Online I always went away from keyboard and wanted mobile notifications without wasting much of my data or battery life and with Discord having notifications when someone gets mentioned I got the perfect solution.

Since this bot is open source you can use it how you want, just make sure to not violate the Discord Api Guidelines. Other than that this bot is based on the Discord.py rewrite branch, feel free to check the official [**Documentation**](https://discordpy.readthedocs.io/en/latest/api.html) for more informaton.

## 2. Features

### Built-in:

**Events:** | **Description:**
----------- | ----------------
Selfrole: | Choose for which boss you want to get notifications
World boss announcements: | Notifies you 45, 30, 15, 5 and 1 minute before a boss spawns
Bot status time: | The bot status shows the time left for the next boss
Channel name to timezone: | Sets the name of a channel to the region timezone 

**Commands¹:** | **Description:**
-------------- | ----------------
next: | Returns the next boss that will spawn
timetable: | shows you the spawn table for your region
marketgain²: | calculate the silver gain; with or without Valuepack                                                                     
upgrade³: | calculate the upgrade chance & simulates an upgrade

¹ : The prefix is defined in the config fil, see more at the Setup section   
² : syntax: marketgain [amount of silvers] [y/yes or n/no]  
³ : syntax: upgrade [type of gear] [base] [failstacks] [optional: tries]

### Planned:

**Commands:** | **Description:**
------------- | ----------------
help: | Add a custom help command
express: | Express installation command; create channel and set permissions
loot: | Shows you the loot table for the chosen boss
market: | Search for items on the marketplace

If there is anything you want to be added to the bot, just hit me up or advanced users can fork it and maybe created it, so i can just implement it.

## 3. Setup

1. Clone this [**repository**](https://github.com/MikaPopp/BDO_Boss_Timer_Discord)
2. install **Google Chrome/Chromium** and download the corresponding [**ChromeDriver**](http://chromedriver.chromium.org/)
3. Install following Dependencies:
	1. [**discord.py**](https://pypi.org/project/discord.py/)
	2. [**selenium**](https://pypi.org/project/selenium/)
	3. [**pytz**](https://pypi.org/project/pytz/)
	4. [**numpy**](https://pypi.org/project/numpy/)
4. Edit the **config.json** file in the **json** folder
5. Have fun with the bot

## 4. Miscellaneous
Well there is not much left to say, except thank you for using it or just checking it out, the bot was tested on several different operating systems such as:
* Windows 10
* MacOS Mojave 10.14.5
* Ubuntu Server 18.04.2 LTS

If there are any questions or you need help, feel free to contact me. 
