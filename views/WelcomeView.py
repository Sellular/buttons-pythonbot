import discord
from discord.ui import View

from utils import GeneralUtils

from datetime import datetime, timedelta, timezone

class WelcomeView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Click here to start!", style=discord.ButtonStyle.green, custom_id="welcome_button")
    async def callback(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user
        now = datetime.now(timezone.utc)

        if abs(now - user.joined_at) < timedelta(seconds = 30):
            await interaction.followup.send("Thanks for being excited to join our community! Please take a moment to read the above messages and try clicking this button again in a bit.")
            return
    
        guildConfig = GeneralUtils.getConfig('guild')
        onboardingRoleId = guildConfig['onboarding_role_id']

        role = discord.utils.get(interaction.guild.roles, id = int(onboardingRoleId))
        await user.add_roles(role)

        rolesChannelId = guildConfig['add_roles_channel_id']
        await interaction.followup.send(f"You now have the onboarding role! Head over to the <#{rolesChannelId}> channel to pick some more!")

        self.value=False