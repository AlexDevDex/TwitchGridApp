from dotenv import load_dotenv
import os
from gridApp_twitch_bot import TwitchBot
from gridApp_discord_bot import DiscordBot
from config import TWITCH_CHANNELS
import asyncio
import keyboard

exit_program = False  # Variable to signal program termination

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

async def handle_exit():
    global exit_program
    print("Received exit signal. Cleaning up...")
    exit_program = True

# Run the Twitch bot
async def run_twitch():
    # Create an instance of TwitchBot with the default event loop
    twitch_bot = TwitchBot(token=twitch_token, prefix=twitch_prefix, initial_channels=twitch_channels)

    try:
        # Start the Twitch bot
        await twitch_bot.start()
    finally:
        # Close the Twitch bot and its connection
        await twitch_bot.close()

# Run the Discord bot
async def run_discord():
    # Create an instance of DiscordBot with the default event loop
    discord_bot = DiscordBot(token=discord_token, prefix=discord_prefix)

    try:
        # Start the Discord bot
        await discord_bot.start(discord_bot.token)
    finally:
        # Close the Discord bot and its connection
        await discord_bot.close()

async def main():
    global exit_program

    loop = asyncio.get_event_loop()

    # Register the signal handler for Ctrl+C using keyboard module
    keyboard.add_hotkey('ctrl+c', lambda: loop.create_task(handle_exit()))

    try:
        task_twitch = loop.create_task(run_twitch())
        task_discord = loop.create_task(run_discord())

        await asyncio.gather(task_twitch, task_discord)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Explicitly cancel tasks
        if 'task_twitch' in locals():
            task_twitch.cancel()
            try:
                await task_twitch
            except asyncio.CancelledError:
                pass

        if 'task_discord' in locals():
            task_discord.cancel()
            try:
                await task_discord
            except asyncio.CancelledError:
                pass

        # Close the event loop
        await asyncio.gather(*asyncio.all_tasks())
        loop.stop()
        loop.close()

        print("Exiting the program.")

if __name__ == '__main__':
    asyncio.run(main())
    print("Program should have stopped. Let's pray it did.")
