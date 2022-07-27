import discord
from discord.ui import View

import asyncio

class VerificationView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Access the server!", style = discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        member_role = guild.get_role(886804525548187708)
        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.5)
        await interaction.followup.send("You now have the blues role! Enjoy your stay in our server!!")