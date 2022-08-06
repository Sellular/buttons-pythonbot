import discord
from discord.ui import View, Button

from views.components import RoleSelect
from utils import GeneralUtils


class RoleChooseView(View):
    updateMode = False
    custom_id = ""

    def __init__(self, options: list, custom_id: str, updateMode: bool = False):
        self.updateMode = updateMode
        self.custom_id = custom_id
        self.options = options

        super().__init__(timeout=None)
        self.initSelects(options)

    def initSelects(self, options: list):
        placeholder = 'Make a selection'

        select = self.initSelect(placeholder)
        for option in options:
            if len(select.options) != 0 and len(select.options) % 25 == 0:
                select.max_values = 25
                self.add_item(select)
                select = self.initSelect(placeholder)
            roleID = option['roleID']
            displayName = option['displayName']

            select.add_option(label=displayName, value=str(roleID))

        select.max_values = len(select.options)
        self.add_item(select)

        if self.updateMode:
            button = Button(label=f"Remove All Above Roles", style=discord.ButtonStyle.red,
                            custom_id=f"{self.custom_id}{len(self.children)}_remove_button", emoji="🗑️")

            async def callback(self, interaction: discord.Interaction):
                if self.options:
                    member = interaction.user
                    for role in self.options:
                        removeRole = discord.utils.get(
                            member.guild.roles, id=role['roleID'])
                        if removeRole:
                            await member.remove_roles(removeRole)

            button.callback = callback
            self.add_item(button)

    def initSelect(self, placeholder: str):
        select = RoleSelect(placeholder=placeholder,
                            custom_id=f"{self.custom_id}{len(self.children)}", updateMode=self.updateMode)
        return select
