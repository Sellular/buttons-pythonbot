import discord
from discord.ui import View, Select

class LastMSGV2View(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder = 'Make a selection',
        custom_id='last_select_v2',
        options = [
            discord.SelectOption(label='Producer'),
            discord.SelectOption(label='Audiophile')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: Select):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        
        if select.values[0] == 'Producer':
            await interaction.response.edit_message(view=self)
            producer = guild.get_role(989040398766850099)
            if member.get_role(producer.id):
                await member.remove_roles(producer)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(producer)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Audiophile':
            await interaction.response.edit_message(view=self)
            audioph = guild.get_role(989040473463193600)
            if member.get_role(audioph.id):
                await member.remove_roles(audioph)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(audioph)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)