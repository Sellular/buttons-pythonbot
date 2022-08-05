import discord
from discord.ui import View

from utils import GeneralUtils

import asyncio

class VerificationView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Access the server!", style=discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        guild = interaction.guild
        guildConfig = GeneralUtils.getConfig('guild')
        member = interaction.user

        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.2) # Thinking...

        onboarding_role = discord.utils.get(
            guild.roles, id=int(guildConfig['onboarding_role_id']))
        if onboarding_role:
            await member.remove_roles(onboarding_role)
        else:
            await interaction.followup.send("Role not found. Contact bot developer or server admin")

        member_role = discord.utils.get(
            guild.roles, id=int(guildConfig['member_role_id']))
        if member_role:
            await member.add_roles(member_role)
            await interaction.followup.send(f"You now have the {member_role.name} role! Enjoy your stay in our server!!")
        else:
            await interaction.followup.send("Role not found. Contact bot developer or server admin")
