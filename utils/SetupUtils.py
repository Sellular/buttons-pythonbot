import discord, os
from discord.ext import commands

from views import WelcomeView, PronounsView, PrononsView, GenreChooseView, GenreChoose2View, GenreChooseV2View, GenreChooseV3View, DoneButtonView, LastMSGV2View, LastMSGView, VerificationView

def setupBot():
    description = 'An administration bot'

    intents = discord.Intents.default()
    intents.guild_messages = True
    intents.members = True
    intents.bans = True

    return commands.Bot(command_prefix=('-', '='), intents=intents, description=description)

def importViews(bot: discord.ext.commands.Bot):
    bot.add_view(WelcomeView())
    bot.add_view(PronounsView())
    bot.add_view(PrononsView())
    bot.add_view(GenreChooseView())
    bot.add_view(GenreChoose2View())
    bot.add_view(GenreChooseV2View())
    bot.add_view(GenreChooseV3View())
    bot.add_view(LastMSGView())
    bot.add_view(LastMSGV2View())
    bot.add_view(DoneButtonView())
    bot.add_view(VerificationView())

async def importCogs(bot: discord.ext.commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            await bot.load_extension("cogs.commands." + cogName)

    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            await bot.load_extension("cogs.events." + cogName)