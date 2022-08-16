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
        
        try:
            if view.options:
                member = interaction.user

                removedRoles = []
                for role in view.options:
                    removeRole = discord.utils.get(
                        member.guild.roles, id=role['roleID'])
                    if removeRole:
                        await member.remove_roles(removeRole)
                        removedRoles.append(removeRole.name)
                
                if removedRoles:
                    rolesStr = ', '.join(removedRoles)
                    await interaction.followup.send(f"Removed role{'s' if len(removedRoles) > 1 else ''}: {rolesStr}", ephemeral=True)
                else:
                    await interaction.followup.send("You had no roles to remove from the dropdown.")
        except Exception as error:
            print(error)
            await interaction.followup.send("Error removing roles. Contact the bot developer or server admin.")