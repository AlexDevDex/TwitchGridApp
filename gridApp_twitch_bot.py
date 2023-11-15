import os
from twitchio.ext import commands

class TwitchBot(commands.Bot):
    def __init__(self, token, prefix, initial_channels, loop=None):
        # Initialise our Bot with our access token, prefix, and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable that returns a list of strings...
        super().__init__(token=token, prefix=prefix, initial_channels=initial_channels,
                         capabilities=['chat_login', 'chat_messages', 'commands', 'cheer', 'subscription'], loop=loop)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now, we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to the console...
        print(message.content)

        # Check for cheers (bits) and subscriptions
        if message.tags.get('is_subscriber'):
            await self.handle_subscription(message)
        elif getattr(message, 'bits', 0):
            await self.handle_cheer(message)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    async def handle_subscription(self, message):
        # Handle subscription events here
        username = message.author.name
        print(f'{username} has subscribed!')

    async def handle_cheer(self, message):
        # Handle cheer events here
        username = message.author.name

        # Check for bits in the message tags
        bits = message.tags.get('bits')
    
        if bits:
            print(f'{username} cheered {bits} bits!')
        else:
            print(f'{username} sent a message without bits.')


    async def close(self):  # Add this method
        await super().close()
        if self._connection:
            await self._connection._close()

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello; we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'I\'m afraid I can\'t do that, {ctx.author.name}!')

    @commands.command()
    async def alive(self, alive: commands.Context):
        await alive.send('Bot is alive')