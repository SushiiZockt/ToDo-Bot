#Made by SushiiZockt with ❤️

import discord
from discord.ext import commands, tasks

import os
from dotenv import load_dotenv

import configs.config as cfg
from configs.banner import start_banner

load_dotenv()


class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix=commands.when_mentioned_or(cfg.command_prefix), intents=intents)
        
    async def setup_hook(self) -> None:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
            
    async def on_ready(self):
        await start_banner(self=self, bot=bot)

bot = Client()
bot.run(os.getenv('TOKEN'))