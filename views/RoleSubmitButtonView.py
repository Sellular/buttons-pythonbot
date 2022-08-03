import discord
from discord.ui import View, button

import asyncio

from utils import GeneralUtils
from views import VerificationView

class RoleSubmitButtonView(View):
    custom_id = ""
    select_views = []

    def __init__(self, select_views: list, custom_id: str):
        self.custom_id = custom_id
        self.select_views = select_views
        super().__init__(timeout = None)

    @button(label="Click once you've assigned your roles!", style = discord.ButtonStyle.green, custom_id=f'{custom_id}_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = interaction.user

        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.3) # Thinking...

        if self.select_views:
            for select_view in self.select_views:
                for select in select_view.children:
                    for value in select.values:
                        role = discord.utils.get(guild.roles, id = int(value))
                        if role:
                            await member.add_roles(role)

        guildConfig = GeneralUtils.getConfig('guild')
        member = interaction.user
        newMemberRole = discord.utils.get(guild.roles, id = int(guildConfig['new_member_role_id']))
        await member.add_roles(newMemberRole)
        channel = discord.utils.get(guild.text_channels, id = int(guildConfig['greeting_channel_id']))
        await channel.send(f"Hey Greeters! Let's give a warm welcome to {member.mention}! Once you've been introduced to our team, click this button to gain access to the rest of the server!", view = VerificationView())

        await interaction.followup.send(f"You now have the new member role! Head over to our <#{guildConfig['greeting_channel_id']}> to meet our team!", ephemeral=True)
        