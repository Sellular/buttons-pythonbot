import discord
from discord.ui import View

class DoneButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Click once you've assigned your roles!", style = discord.ButtonStyle.green, custom_id='done_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        verified = guild.get_role(987249040288784389)
        await member.add_roles(verified)
        removed_role = guild.get_role(987553778662268928)
        await member.remove_roles(removed_role)
        role_producer = 989040398766850099
        role_audiophile = 989040473463193600

        try:
            if str(role_producer) in bot.role_cache[str(interaction.user.id)]:
                role_pro = guild.get_role(role_producer)
                await member.add_roles(role_pro)
            if str(role_audiophile) in bot.role_cache[str(interaction.user.id)]:
                await interaction.response.send_message('smth')
        except:
            pass
        channel = guild.get_channel(989056168192274433)
        await channel.send(f"Hey Greeters! Let's give a warm welcome to {member.mention} of user who clicked the button! Once you've been introduced to our team, click this button to gain access to the rest of the server!", view = Verification())