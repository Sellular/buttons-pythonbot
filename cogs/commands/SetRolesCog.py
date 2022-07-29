import discord
from discord.ext import commands

from utils import GeneralUtils
from views import RoleChooseView, RoleSubmitButtonView

class SetRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ['sr'])
    async def setroles(self, ctx):
        pronounArray = GeneralUtils.getPronouns()
        genreArray = GeneralUtils.getMusicGenres()
        hobbyArray = GeneralUtils.getHobbies()

        pronounChooseView = RoleChooseView(options = pronounArray, custom_id = "pronoun_select")
        genreChooseView = RoleChooseView(options = genreArray, custom_id = "genre_select")
        hobbyChooseView = RoleChooseView(options = hobbyArray, custom_id = "hobby_select")
        doneButtonView = RoleSubmitButtonView(select_views = [pronounChooseView, genreChooseView, hobbyChooseView], custom_id = "submit_button")

        await ctx.send("Pick your pronoun roles here! We've got 'em all.", view=pronounChooseView)
        await ctx.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=genreChooseView)
        await ctx.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=hobbyChooseView)
        await ctx.send('Once you have finished selecting your roles, click this button to continue your onboarding', view=doneButtonView)

        self.bot.add_view(pronounChooseView)
        self.bot.add_view(genreChooseView)
        self.bot.add_view(hobbyChooseView)
        self.bot.add_view(doneButtonView)

async def setup(bot: commands.Bot):
    await bot.add_cog(SetRolesCog(bot))