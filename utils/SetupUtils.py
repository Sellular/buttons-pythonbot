import discord
import os
from discord.ext import commands

from utils import DiscordUtils, GeneralUtils
from views import VerificationView, WelcomeView


def importViews(bot: discord.Client):
    bot.add_view(VerificationView())


async def resetViews(bot: discord.Client):
    guildConfig = GeneralUtils.getConfig('guild')
    channels_to_clear = [
        guildConfig['add_roles_channel_id'],
        guildConfig['update_roles_channel_id'],
        guildConfig['welcome_channel_id']
    ]

    for channel_id_str in channels_to_clear:
        id_int = int(channel_id_str)
        channel = await DiscordUtils.clearChannel(id_int, bot)
        if channel:
            if channel_id_str == guildConfig['add_roles_channel_id']:
                await DiscordUtils.sendAddRoles(bot)
            elif channel_id_str == guildConfig['update_roles_channel_id']:
                await DiscordUtils.sendUpdateRoles(bot)
            elif channel_id_str == guildConfig['welcome_channel_id']:
                await DiscordUtils.sendWelcome(bot)

# async def importCogs(bot: discord.ext.discord.Client):
#     for filename in os.listdir("./cogs/commands"):
#         if filename.endswith(".py"):
#             cogName = filename[:-3]
#             await bot.load_extension("cogs.commands." + cogName)
