import discord
from discord.ui import Button

import asyncio


class RemoveAllRolesButton(Button):
    def __init__(self, custom_id):
        super().__init__(label=f"Remove All Above Roles", style=discord.ButtonStyle.red,
                         custom_id=custom_id, emoji="🗑️")

    async def callback(self, interaction: discord.Interaction):
        view = self.view
        await interaction.response.defer(ephemeral=True, invisible=False)
        await asyncio.sleep(0.2)  # Thinking...
        if view.options:
            member = interaction.user
            for role in view.options:
                removeRole = discord.utils.get(
                    member.guild.roles, id=role['roleID'])
                if removeRole:
                    await member.remove_roles(removeRole)
            await interaction.followup.send("All roles in that dropdown have been removed.", ephemeral=True)
