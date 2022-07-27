from types import GenericAlias
import discord
from discord.ui import View

from utils import GeneralUtils

import asyncio

class WelcomeView(View):
    def __init__(self):
        super().__init__(timeout=None)
    # async def interaction_check(self, interaction):
    #     user = interaction.user
    #     if user.joined_at(second=15):
    #         await interaction.response.send_message("You haven't read the rules yet.", ephemeral=True)    
    #         return False
    #     return True
    @discord.ui.button(label="Click here to start!", style=discord.ButtonStyle.green, custom_id="welcome_button")
    async def callback(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user

        guildConfig = GeneralUtils.getConfig('config.ini', 'guild')
        newUserRoleId = guildConfig['new_user_role_id']

        role = discord.utils.get(interaction.guild.roles, id = int(newUserRoleId))
        await user.add_roles(role)
        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.5)

        rolesChannelId = guildConfig['roles_channel_id']
        await interaction.followup.send(f"You now have the onboarding role! Head over to the <#{rolesChannelId}> channel to pick some more!")

        self.value=False