import discord
from discord.ext import commands

from utils import GeneralUtils
from views import RoleChooseView

class UpdateRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ['ur']) 
    async def updateroles(self, ctx): 
        pronounArray = GeneralUtils.getPronouns()
        genreArray = GeneralUtils.getMusicGenres()
        hobbyArray = GeneralUtils.getHobbies()

        pronounsView = RoleChooseView(options = pronounArray, custom_id = "update_pronoun_select", removeIfExist=True)
        genreChooseView = RoleChooseView(options = genreArray, custom_id = "update_genre_select", removeIfExist=True)
        hobbyChooseView = RoleChooseView(options = hobbyArray, custom_id = 'update_hobby_select', removeIfExist=True)

        await ctx.send("Pick your pronoun roles here! We've got 'em all.", view=pronounsView)
        await ctx.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=genreChooseView)
        await ctx.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=hobbyChooseView)

        self.bot.add_view(pronounsView)
        self.bot.add_view(genreChooseView)
        self.bot.add_view(hobbyChooseView)

async def setup(bot: commands.Bot):
    await bot.add_cog(UpdateRolesCog(bot))