import discord

from utils import SetupUtils, GeneralUtils, DBUtils

# commands.Bot if commands are needed
class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        # command_prefix=('!'),
        super().__init__(intents=intents)

    async def setup_hook(self) -> None:
        SetupUtils.importViews(self)
        # await SetupUtils.importCogs(self)

    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')
        await SetupUtils.resetViews(self)

DBUtils.checkTables()

bot = MyClient()
botConfig = GeneralUtils.getConfig('bot')

bot.run(botConfig['token'])
