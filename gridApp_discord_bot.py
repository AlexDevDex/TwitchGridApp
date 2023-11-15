import os
import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    def __init__(self, token, prefix, loop=None):
        #token=t
        super().__init__(command_prefix=prefix, intents=discord.Intents.all(), loop=loop)
        self.token = token
