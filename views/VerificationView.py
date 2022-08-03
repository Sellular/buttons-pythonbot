import discord
from discord.ui import View

from utils import GeneralUtils

class VerificationView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Access the server!", style = discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        guild = interaction.guild
        guildConfig = GeneralUtils.getConfig('guild')
        member = interaction.user
        member_role = discord.utils.get(guild.roles, id = int(guildConfig['member_role_id']))
        if member_role:
            await member.add_roles(member_role)
            await interaction.response.defer(ephemeral=True, thinking=True)
        else:
            await interaction.response.send_message("Role not found. Contact bot developer or server admin")