import discord
from discord.ui import Select

class RoleSelect(Select):
    updateMode = False

    def __init__(self, placeholder: str, custom_id: str, updateMode: bool = False):
        self.updateMode = updateMode
        super().__init__(placeholder = placeholder, custom_id = custom_id)
    
    async def callback(self, interaction: discord.Interaction):
        selectedRoleID = int(self.values[0])
        guild = interaction.guild
        role = discord.utils.get(guild.roles, id = selectedRoleID)
        if self.updateMode:
            member = interaction.user
            
            await interaction.response.edit_message(view = self.view)
            
            followupPrefix = "Assigned"
            if member.get_role(role.id):
                await member.remove_roles(role)
                followupPrefix = "Removed"
            else:
                await member.add_roles(role)

            await interaction.followup.send(f"{followupPrefix} role **{role.name}**.", ephemeral = True)
        else:
            await interaction.response.send_message(f"Your roles have been saved, and you'll receive them when you finish onboarding!", ephemeral = True)