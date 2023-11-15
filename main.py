from gridApp_twitch import TwitchBot
from gridApp_discord import DiscordBot
import asyncio

# Set your Twitch and Discord tokens
twitch_token = 'YOUR_TWITCH_TOKEN'
discord_token = 'YOUR_DISCORD_TOKEN'

# Set prefixes and initial channels
twitch_prefix = '!'
discord_prefix = '!'

# Set initial Twitch channels
twitch_channels = ['your_channel']

# Create instances of Twitch and Discord bots
twitch_bot = TwitchBot(token=twitch_token, prefix=twitch_prefix, initial_channels=twitch_channels)
discord_bot = DiscordBot(token=discord_token, prefix=discord_prefix)

# Run the Twitch bot
async def run_twitch():
    await twitch_bot.start()

# Run the Discord bot
async def run_discord():
    await discord_bot.start(discord_bot.token)

# Run both bots concurrently
async def main():
    await asyncio.gather(run_twitch(), run_discord())

# Run the main script
if __name__ == '__main__':
    asyncio.run(main())
