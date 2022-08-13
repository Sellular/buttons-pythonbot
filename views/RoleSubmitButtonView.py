import discord
from discord.ui import View, button

import asyncio

from utils import GeneralUtils
from views import VerificationView
from dao import OnboardingRoleDAO


class RoleSubmitButtonView(View):
    custom_id = ""
    select_views = []

    def __init__(self, select_views: list = None, custom_id: str = ""):
        if not select_views:
            select_views = []
            
        self.custom_id = custom_id
        self.select_views = select_views
        super().__init__(timeout=None)

    @button(label="Click once you've assigned your roles!", style=discord.ButtonStyle.green, custom_id=f'{custom_id}_button')
    async def on_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user

        await interaction.response.defer(ephemeral=True)
        await asyncio.sleep(0.2)  # Thinking...

        try:
            role_list = []
            if self.select_views:
                for select_view in self.select_views:
                    for select in select_view.children:
                        for value in select.values:
                            role = discord.utils.get(guild.roles, id=int(value))
                            if role:
                                role_list.append((member.id, role.id))
            OnboardingRoleDAO.insertMany(role_list)

            guildConfig = GeneralUtils.getConfig('guild')

            if not guildConfig:
                raise Exception("Guild config not found.")

            newMemberRole = discord.utils.get(
                guild.roles, id=int(guildConfig['new_member_role_id']))

            if not newMemberRole:
                raise Exception("NEW_MEMBER_ROLE_ID not found in Guild config.")

            channel = discord.utils.get(guild.text_channels, id=int(
                guildConfig['greeting_channel_id']))

            if not channel:
                raise Exception("GREETING_CHANNEL_ID not found in")

            await member.add_roles(newMemberRole)

            verification_view = VerificationView()
            interaction.client.add_view(verification_view)

            await channel.send(f"Hey Greeters! Let's give a warm welcome to {member.mention}! Once you've been introduced to our team, click this button to gain access to the rest of the server!", view=verification_view)

            await interaction.followup.send(f"You now have the new member role! Head over to our <#{guildConfig['greeting_channel_id']}> to meet our team!", ephemeral=True)

        except (Exception) as error:
            print(error)
            await interaction.followup.send("Error while saving roles. Contact bot developer or server admin", ephemeral=True)
     