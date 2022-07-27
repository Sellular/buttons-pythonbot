import discord
from discord.ui import View, Select

class LastMSGView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder = 'Make a selection',
        custom_id='last_select',
        options = [
            discord.SelectOption(label='Producer', value = 989040398766850099),
            discord.SelectOption(label='Audiophile', value = 989040473463193600)
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: Select):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        bot.role_cache = {}
        bot.role_cache[f'{interaction.user.id}'] = select.values

        await interaction.response.send_message(f"Assigned role **{select.values[0]}**.", ephemeral=True)