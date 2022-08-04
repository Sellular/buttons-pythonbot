import discord
from discord.ui import Select

import asyncio


class RoleSelect(Select):
    updateMode = False

    def __init__(self, placeholder: str, custom_id: str, updateMode: bool = False):
        self.updateMode = updateMode
        super().__init__(placeholder=placeholder, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        message_id = interaction.message.id
        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.2)  # Thinking...
        if self.updateMode:
            member = interaction.user
            guild = interaction.guild

            await interaction.followup.edit_message(message_id=message_id, view=self.view)

            assignedRoles = []
            removedRoles = []
            for value in self.values:
                role = discord.utils.get(guild.roles, id=int(value))
                if role:
                    if member.get_role(role.id):
                        await member.remove_roles(role)
                        removedRoles.append(role.name)
                    else:
                        await member.add_roles(role)
                        assignedRoles.append(role.name)

            if len(assignedRoles) > 0:
                rolesStr = ', '.join(assignedRoles)
                await interaction.followup.send(f"Assigned role{'s' if len(assignedRoles) > 1 else ''}: {rolesStr}")
            if len(removedRoles) > 0:
                rolesStr = ', '.join(removedRoles)
                await interaction.followup.send(f"Removed role{'s' if len(removedRoles) > 1 else ''}: {rolesStr}")
        else:
            await interaction.followup.send(f"Your roles have been saved, and you'll receive them when you finish onboarding!", ephemeral=True)
