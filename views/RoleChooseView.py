import discord
from discord.ui import View, Button

from views.components import RoleSelect

import asyncio


class RoleChooseView(View):
    updateMode = False
    custom_id = ""

    def __init__(self, options: list, custom_id: str, updateMode: bool = False):
        self.updateMode = updateMode
        self.custom_id = custom_id
        self.options = options

        super().__init__(timeout=None)
        self.__initSelects(options)

    def __initSelects(self, options: list):
        placeholder = 'Make a selection'

        select = self.__initSelect(placeholder)
        for option in options:
            if len(select.options) != 0 and len(select.options) % 25 == 0:
                select.max_values = 25
                self.add_item(select)
                select = self.__initSelect(placeholder)
            roleID = option['roleID']
            displayName = option['displayName']

            select.add_option(label=displayName, value=str(roleID))

        select.max_values = len(select.options)
        self.add_item(select)

        if self.updateMode:
            button = Button(label=f"Remove All Above Roles", style=discord.ButtonStyle.red,
                            custom_id=f"{self.custom_id}{len(self.children)}_remove_button", emoji="🗑️")

            async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.defer(ephemeral=True)
                await asyncio.sleep(0.2)  # Thinking...
                if self.options:
                    member = interaction.user
                    for role in self.options:
                        removeRole = discord.utils.get(
                            member.guild.roles, id=role['roleID'])
                        if removeRole:
                            await member.remove_roles(removeRole)
                    await interaction.followup.send("All roles in that dropdown have been removed.", ephemeral=True)

            button.callback = callback
            self.add_item(button)

    def __initSelect(self, placeholder: str):
        select = RoleSelect(placeholder=placeholder,
                            custom_id=f"{self.custom_id}{len(self.children)}", updateMode=self.updateMode)
        return select
