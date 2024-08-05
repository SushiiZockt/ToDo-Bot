import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import MISSING
import datetime
from discord.ui import Button, Modal, View, TextInput
import configs.config as cfg
from colorama import Fore

import os
import json


class help_command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    @app_commands.command(name="help", description="Command ist für Sascha")

    async def command_test(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=cfg.wait_embed(), ephemeral=True)
        embed = discord.Embed(
            
        )
                
    



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(help_command(bot))