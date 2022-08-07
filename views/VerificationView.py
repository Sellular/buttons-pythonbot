import discord
from discord.ui import View

from utils import GeneralUtils
from dao import OnboardingRoleDAO

import asyncio


class VerificationView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Access the server!", style=discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        guild = interaction.guild
        guildConfig = GeneralUtils.getConfig('guild')
        member = interaction.user

        await interaction.response.defer(ephemeral=True)
        await asyncio.sleep(0.2)  # Thinking...

        additional_roles = None
        try:
            additional_roles = OnboardingRoleDAO.getOnboardingRolesByMember(str(member.id))
            OnboardingRoleDAO.deleteOnboardingRolesByMember(str(member.id))
        except (Exception) as error:
            print(error)
            await interaction.followup.send("Error during verification. Contact bot developer or server admin")
        else:
            if additional_roles:
                for role in additional_roles:
                    add_role = discord.utils.get(guild.roles, id=int(role.roleID))
                    await member.add_roles(add_role)

            onboarding_role = discord.utils.get(
                guild.roles, id=int(guildConfig['onboarding_role_id']))
            if onboarding_role:
                await member.remove_roles(onboarding_role)
            else:
                await interaction.followup.send("Role not found. Contact bot developer or server admin")

            member_role = discord.utils.get(guild.roles, id=int(guildConfig['member_role_id']))
            if member_role:
                await member.add_roles(member_role)
                await interaction.followup.send(f"You now have the {member_role.name} role! Enjoy your stay in our server!!")
            else:
                await interaction.followup.send("Role not found. Contact bot developer or server admin")
