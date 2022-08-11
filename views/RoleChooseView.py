import discord
from discord.ui import View, Button

from views.components import RoleSelect, RemoveAllRolesButton

import asyncio


class RoleChooseView(View):
    updateMode = False
    custom_id = ""

    def __init__(self, options: list = None, custom_id: str = "", updateMode: bool = False):
        if not options:
            options = []
            
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

        if len(select.options) > 0:
            select.max_values = len(select.options)
        self.add_item(select)

        if self.updateMode:
            self.add_item(RemoveAllRolesButton(custom_id=f"{self.custom_id}{len(self.children)}_remove_button"))

    def __initSelect(self, placeholder: str):
        select = RoleSelect(placeholder=placeholder,
                            custom_id=f"{self.custom_id}{len(self.children)}", updateMode=self.updateMode)
        return select
