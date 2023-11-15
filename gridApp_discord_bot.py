import os
import discord
from discord.ext import commands
from config import DISCORD_TOKEN

class DiscordBot(commands.Bot):
    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)
        self.token = DISCORD_TOKEN