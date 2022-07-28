import discord
from discord.ext import commands

from views import PronounsView, GenreChooseView, DoneButtonView, LastMSGView

class rCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def r(self, ctx):
        await ctx.send("Pick your pronoun roles here! We've got 'em all.", view=PronounsView())
        await ctx.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=GenreChooseView())
        await ctx.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=LastMSGView())
        await ctx.send('Once you have finished selecting your roles, click this button to continue your onboarding', view=DoneButtonView())

async def setup(bot: commands.Bot):
    await bot.add_cog(rCog(bot))