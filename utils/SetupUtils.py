import discord
import os
from discord.ext import commands

from utils import DiscordUtils, GeneralUtils
from views import VerificationView, WelcomeView


def importViews(bot: commands.Bot):
    bot.add_view(WelcomeView())
    bot.add_view(VerificationView())


async def resetViews(bot: commands.Bot):
    try:
        guildConfig = GeneralUtils.getConfig('guild')
        if not guildConfig:
            raise Exception("Guild config not found.")

        addRolesChannelId = guildConfig['add_roles_channel_id']
        updateRolesChannelId = guildConfig['update_roles_channel_id']

        if not addRolesChannelId:
            raise Exception("ADD_ROLES_CHANNEL_ID not found in Guild config.")

        if not updateRolesChannelId:
            raise Exception("UPDATE_ROLES_CHANNEL_ID not found in Guild config.")

        await DiscordUtils.updateAddRoles(bot)
        await DiscordUtils.updateUpdateRoles(bot)
        await DiscordUtils.updateWelcome(bot)
        await DiscordUtils.updateInfo(bot)
    except Exception as error:
        print(error)


def importCogs(bot: commands.Bot):
    # for filename in os.listdir("./cogs/commands"):
    #     if filename.endswith(".py"):
    #         cogName = filename[:-3]
    #         bot.load_extension("cogs.commands." + cogName)

    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.events." + cogName)

    for filename in os.listdir("./cogs/tasks"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.tasks." + cogName)