import discord
from discord.ext import commands

from utils import SetupUtils, GeneralUtils

from views import WelcomeView, PronounsView, PrononsView, GenreChooseView, GenreChoose2View, GenreChooseV2View, GenreChooseV3View, DoneButtonView, LastMSGV2View, LastMSGView, VerificationView

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=('!'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(WelcomeView())
        self.add_view(PronounsView())
        self.add_view(PrononsView())
        self.add_view(GenreChooseView())
        self.add_view(GenreChoose2View())
        self.add_view(GenreChooseV2View())
        self.add_view(GenreChooseV3View())
        self.add_view(LastMSGView())
        self.add_view(LastMSGV2View())
        self.add_view(DoneButtonView())
        self.add_view(VerificationView())

        await SetupUtils.importCogs(self)

    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", bot.user.name)
        print("User ID: ", bot.user.id)
        print('-----')

bot = MyClient()
botConfig = GeneralUtils.getConfig('config.ini', 'bot')

bot.run(botConfig['token'])