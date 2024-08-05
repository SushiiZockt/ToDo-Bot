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


class test_command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    @app_commands.command(name="test", description="Command ist für Sascha")


    async def command_test(self, interaction: discord.Interaction]):
        await interaction.response.send_message(embed=cfg.wait_embed(), ephemeral=True, delete_after=10)
        if not int(interaction.user.id) == int(cfg.admin_id):
            await interaction.edit_original_response(embed=cfg.error_embed(f"Nur <@{cfg.admin_id}> kann diesen Command verwenden"))
            return 
        
        
        
        
        
        
        await interaction.edit_original_response(embed=cfg.done_embed(f"Fertig"))
                
    



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(test_command(bot))