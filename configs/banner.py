from colorama import Back, Fore, Style

import time
from colorama import Back, Fore, Style
from discord.ext import commands
from configs.lib.tree import tree
import configs.config as cfg
import datetime

async def start_banner(self, bot: commands.Bot):
    rest = (Style.RESET_ALL)
    pref = f"EliteV・{datetime.datetime.now().strftime('%H:%M')}Uhr"
    pref_color = Fore.LIGHTMAGENTA_EX
    prfx = (Fore.BLACK + "[" + pref_color + pref + Fore.BLACK + "]" + rest + " ")
    
    
    
    
    print("")
    print("")
    print(prfx + f"{Fore.LIGHTRED_EX}Developer:   |    SushiiZockt" + rest)
    print(prfx + f"{Fore.LIGHTBLUE_EX}Discord:     |    https://discord.gg/WKgP564bA4" + rest)
    print(prfx + f"{Fore.MAGENTA}Bot Name:    |    {bot.user.name}" + rest)
    print(prfx + f"{Fore.LIGHTGREEN_EX}Bot-ID:      |    {bot.user.id}" + rest)
    print(prfx + f"{Fore.GREEN}Guilds:      |    {str(len(bot.guilds))}" + rest)
    synced = await tree(self)
    print(prfx + f"{Fore.YELLOW}Commands:    |    {len(synced)}" + rest)
    print("")
    print("")