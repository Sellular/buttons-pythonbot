import discord
from discord.ext import commands

from utils import SetupUtils, GeneralUtils, DBUtils

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix=('!'), intents=intents)

    async def on_ready(self):
        SetupUtils.importViews(self)
        await SetupUtils.importCogs(self)
        print("Bot running with:")
        print("Username: ", self.user.name)
        print("User ID: ", self.user.id)
        print('-----')
        await SetupUtils.resetViews(self)


try:
    DBUtils.checkTables()
except (Exception) as error:
    print(error)
else:
    bot = MyClient()
    botConfig = GeneralUtils.getConfig('bot')

    bot.run(botConfig['token'])
