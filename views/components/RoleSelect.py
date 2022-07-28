import discord
from discord.ui import Select

class RoleSelect(Select):
    removeIfExist = False

    def __init__(self, placeholder: str, custom_id: str, removeIfExist: bool = False):
        self.removeIfExist = removeIfExist
        super().__init__(placeholder = placeholder, custom_id = custom_id)
    
    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        member = interaction.user
        selectedRoleID = int(self.values[0])

        await interaction.response.edit_message(view = self)
        role = discord.utils.get(guild.roles, id = selectedRoleID)

        followupPrefix = "Assigned"
        if self.removeIfExist and member.get_role(role):
            await member.remove_roles(role)
            followupPrefix = "Removed"
        else:
            await member.add_roles(role)

        await interaction.followup.send(f"{followupPrefix} role **{role.name}**.", ephemeral = True)
        
