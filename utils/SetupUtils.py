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

        channels_to_clear = [
            addRolesChannelId,
            updateRolesChannelId
        ]

        for channel_id_str in channels_to_clear:
            id_int = int(channel_id_str)
            channel = await DiscordUtils.clearChannel(id_int, bot)
            if channel:
                if channel_id_str == guildConfig['add_roles_channel_id']:
                    await DiscordUtils.sendAddRoles(bot)
                elif channel_id_str == guildConfig['update_roles_channel_id']:
                    await DiscordUtils.sendUpdateRoles(bot)
    except Exception as error:
        print(error)


async def importCogs(bot: commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.commands." + cogName)

    for filename in os.listdir("./cogs/events"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.events." + cogName)

    for filename in os.listdir("./cogs/tasks"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            bot.load_extension("cogs.tasks." + cogName)