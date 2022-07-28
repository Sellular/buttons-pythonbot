import discord, os
from discord.ext import commands

from views import WelcomeView, PronounsView, PrononsView, GenreChooseView, DoneButtonView, LastMSGV2View, LastMSGView, VerificationView

def importViews(bot: discord.ext.commands.Bot):
    bot.add_view(WelcomeView())
    bot.add_view(PronounsView())
    bot.add_view(PrononsView())
    bot.add_view(GenreChooseView())
    bot.add_view(LastMSGView())
    bot.add_view(LastMSGV2View())
    bot.add_view(DoneButtonView())
    bot.add_view(VerificationView())

async def importCogs(bot: discord.ext.commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            await bot.load_extension("cogs.commands." + cogName)