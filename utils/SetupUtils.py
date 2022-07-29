import discord, os

async def importCogs(bot: discord.ext.commands.Bot):
    for filename in os.listdir("./cogs/commands"):
        if filename.endswith(".py"):
            cogName = filename[:-3]
            await bot.load_extension("cogs.commands." + cogName)