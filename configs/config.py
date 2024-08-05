#Made by SushiiZockt with ❤️
import discord, datetime
from colorama import Fore, Back, Style



projekt_name = 'Todo'
projekt_version = '1.0.0'
command_prefix = 'dfsd'

bot_status = "/help"


admin_id = 571039644490268673 #SushiiZockt




def console_message(msg: str = "Error"):
    reset = Style.RESET_ALL
    prfx = (Fore.LIGHTBLACK_EX + "[" + Fore.LIGHTGREEN_EX + f"{projekt_name} ・{datetime.datetime.now().strftime('%H:%M')}Uhr" + Fore.LIGHTBLACK_EX + "]" + reset + " ")