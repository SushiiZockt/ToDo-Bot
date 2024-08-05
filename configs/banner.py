#Made by SushiiZockt with ❤️
import discord
from discord.ext import commands

import datetime
from colorama import Back, Fore, Style
import asyncio

from configs.lib.tree import tree
import configs.config as cfg


async def start_banner(self, bot: commands.Bot):
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.CustomActivity(name=cfg.bot_status))
    reset = (Style.RESET_ALL)
    prfx = (Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + f"{cfg.projekt_name} ・{datetime.datetime.now().strftime('%H:%M')}Uhr" + Fore.LIGHTBLACK_EX + "]" + reset + " ")
    
    zeile = f"{Fore.LIGHTBLACK_EX}| {reset}"
    green = Fore.LIGHTGREEN_EX
    blue = Fore.LIGHTCYAN_EX
    time = datetime.datetime.now().strftime('%d.%m.%Y um %H%M%S Uhr')
    #print(time)
    print(prfx + "Loading...")
    await asyncio.sleep(3)
    print(prfx + f"Loading Commands... {Fore.LIGHTRED_EX}(You can use the bot also the commands)" + reset)

    synced = await tree(self)
    print("")
    print(f"{Fore.LIGHTBLACK_EX}[]=============[{green} Discord Bot {Fore.LIGHTBLACK_EX}]=============[]")
    infos = [
        (""),
        (f"{Fore.LIGHTRED_EX}Information:"),
        (""),
        (f"  {green}Developer: {blue}SushiiZockt"),
        (f"  {green}Discord: {blue}https://discord.gg/WKgP564bA4"),
        (f"  {green}Time: {blue}{datetime.datetime.now().strftime('%d.%m.%Y um %H:%M:%S Uhr')}"),
        (""),
        (f"{Fore.LIGHTRED_EX}Bot Infos:"),
        (""),
        (f"  {green}Name: {blue}{bot.user.name}"),
        (f"  {green}Version: {blue}{cfg.projekt_version}"),
        (f"  {green}ID: {blue}{bot.user.id}"),
        (f"  {green}Guilds: {blue}{len(bot.guilds)}"),
        (f"  {green}Commands: {blue} {len(synced)}"),
        ("")
    ]
    
    
    for text in infos:
        print(zeile + text + reset)
    
    print(f"{Fore.LIGHTBLACK_EX}[]=========================================[]" + reset)
    print("")
    print(prfx + f"{blue}Bot is fully started, have fun 😁" + reset)