import discord
from discord.ui import View, Select

class PrononsView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        max_values=1,
        placeholder='Make selection',
        custom_id="pronon_select",
        options=[
            discord.SelectOption(label='They/Them'),
            discord.SelectOption(label='She/Her'),
            discord.SelectOption(label='She/They'),
            discord.SelectOption(label='He/Him',),
            discord.SelectOption(label='He/They'),
            discord.SelectOption(label='Ask me'),
            discord.SelectOption(label='Any pronouns')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction,  select: Select):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        # Selection
        if select.values[0] == 'He/Him':
            await interaction.response.edit_message(view=self)
            male_role = guild.get_role(891907652404248616)
            if member.get_role(male_role.id):
                await member.remove_roles(male_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(male_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'He/They':
            await interaction.response.edit_message(view=self)
            malet_role = guild.get_role(987972562204110938)
            if member.get_role(malet_role.id):
                await member.remove_roles(malet_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(malet_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'She/Her':
            await interaction.response.edit_message(view=self)
            female_role = guild.get_role(891907651720605709)
            if member.get_role(female_role.id):
                await member.remove_roles(female_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(female_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'She/They':
            await interaction.response.edit_message(view=self)
            femalet_role = guild.get_role(987971942122397747)
            if member.get_role(femalet_role.id):
                await member.remove_roles(femalet_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(femalet_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'They/Them':
            await interaction.response.edit_message(view=self)
            g_role = guild.get_role(891907651288580116)
            if member.get_role(g_role.id):
                await member.remove_roles(g_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(g_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Any pronouns':
            await interaction.response.edit_message(view=self)
            a_role = guild.get_role(891907650541994014)
            if member.get_role(a_role.id):
                await member.remove_roles(a_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(a_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Ask me':
            await interaction.response.edit_message(view=self)
            ask_role = guild.get_role(891910337262141500)
            if member.get_role(ask_role.id):
                await member.remove_roles(ask_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(ask_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)