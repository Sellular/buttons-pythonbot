import discord
from discord.ext import commands

from utils import SetupUtils, GeneralUtils

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=('!'), intents=intents)

    async def setup_hook(self) -> None:
        SetupUtils.importViews(self)        
        await SetupUtils.importCogs(self)

    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')

bot = MyClient()
botConfig = GeneralUtils.getConfig('bot')

bot.run(botConfig['token'])