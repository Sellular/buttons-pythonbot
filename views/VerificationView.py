import discord
from discord.ui import View

from utils import GeneralUtils

import asyncio

class VerificationView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Access the server!", style = discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        bot = interaction.client
        guild = interaction.guild
        guildConfig = GeneralUtils.getConfig('guild')
        member = interaction.user
        member_role = discord.utils.get(guild.roles, id = int(guildConfig['new_member_role_id']))
        if member_role:
            await member.add_roles(member_role)
            await interaction.response.defer(ephemeral=True, thinking=True)
            await asyncio.sleep(0.5)
            await interaction.followup.send("You now have the new member role! Enjoy your stay in our server!!")
        else:
            await interaction.response.send_message("Role not found. Contact bot developer or server admin")