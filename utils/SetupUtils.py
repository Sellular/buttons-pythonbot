import discord, os
from discord.ext import commands

from views import VerificationView, WelcomeView

def importViews(bot: commands.Bot):
    bot.add_view(VerificationView())
    bot.add_view(WelcomeView())

async def importCogs(bot: discord.ext.commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            await bot.load_extension("cogs.commands." + cogName)