from dotenv import load_dotenv
import os
from gridApp_twitch_bot import TwitchBot
from gridApp_discord_bot import DiscordBot
from config import TWITCH_CHANNELS
import asyncio

# Load environment variables from .env file
load_dotenv()

# Access environment variables
twitch_token = os.getenv('TWITCH_TOKEN')
discord_token = os.getenv('DISCORD_TOKEN')

# Set prefixes and initial channels
twitch_prefix = '?'
discord_prefix = '?'

# Set initial Twitch channels
twitch_channels = TWITCH_CHANNELS

# Run the Twitch bot
async def run_twitch():
    # Create a new event loop for this task
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Create an instance of TwitchBot with the specified loop
    twitch_bot = TwitchBot(token=twitch_token, prefix=twitch_prefix, initial_channels=twitch_channels, loop=loop)
    
    # Start the Twitch bot
    await twitch_bot.start()

# Run the Discord bot
async def run_discord():
    # Create a new event loop for this task
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Create an instance of DiscordBot with the specified loop
    discord_bot = DiscordBot(token=discord_token, prefix=discord_prefix, loop=loop)
    
    # Start the Discord bot
    await discord_bot.start(discord_bot.token)

# Run both bots on the same asyncio event loop
async def main():
    # Create a common event loop for both tasks
    loop = asyncio.get_event_loop()

    try:
        task_twitch = loop.create_task(run_twitch())
        task_discord = loop.create_task(run_discord())

        await asyncio.gather(task_twitch, task_discord)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the event loop
        loop.close()

# Run the main script
if __name__ == '__main__':
    asyncio.run(main())