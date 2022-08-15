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

        await interaction.response.defer(ephemeral=True, invisible=False)
        await asyncio.sleep(0.2)  # Thinking...
        try:
            guildConfig = GeneralUtils.getConfig('guild')
            if not guildConfig:
                raise Exception("Guild config not found")
            member = interaction.user

            additional_roles = OnboardingRoleDAO.getOnboardingRolesByMember(str(member.id))
            OnboardingRoleDAO.deleteOnboardingRolesByMember(str(member.id))

            if additional_roles:
                for role in additional_roles:
                    add_role = discord.utils.get(guild.roles, id=int(role.roleID))
                    await member.add_roles(add_role)

            member_role = discord.utils.get(guild.roles, id=int(guildConfig['member_role_id']))
            if not member_role:
                raise Exception("MEMBER_ROLE_ID not found in Guild config.")

            await member.add_roles(member_role)
            await interaction.followup.send(f"You now have the {member_role.name} role! Enjoy your stay in our server!!", ephemeral=True)
        except Exception as error:
            print(error)
            await interaction.followup.send("Error during verification. Contact the bot developer or server admin.", ephemeral=True)