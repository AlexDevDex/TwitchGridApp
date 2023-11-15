from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='zgjgrcvpx1rzft4us2a4qpw3jmxl5l', prefix='?', initial_channels=['SunSh4dow'],
                         capabilities=['chat_login', 'chat_messages', 'commands', 'cheer', 'subscription'])


    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Check for cheers (bits) and subscriptions
        if message.tags.get('is_subscriber'):
            await self.handle_subscription(message)
        elif message.bits:
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
        bits = message.bits
        print(f'{username} cheered {bits} bits!')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')
    
    @commands.command()
    async def alive(self, alive: commands.Context):
        await alive.send('Bot is alive')


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.