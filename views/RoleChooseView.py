import discord
from discord.ui import View

from views.components import RoleSelect

class RoleChooseView(View):
    removeIfExist = False
    custom_id = ""

    def __init__(self, options: list, custom_id: str, removeIfExist: bool = False):
        self.removeIfExist = removeIfExist
        self.custom_id = custom_id
        super().__init__(timeout=None)
        self.initSelects(options)

    def initSelects(self, options: list):
        placeholder = 'Make a selection'

        select = self.initSelect(0, placeholder, self.removeIfExist)
        for option in options:
            if len(select.options) != 0 and len(select.options) % 25 == 0:
                self.add_item(select)
                select = self.initSelect(len(self.children), placeholder, self.removeIfExist)
            roleID = option['roleID']
            displayName = option['displayName']

            select.add_option(label = displayName, value = roleID)
        
        self.add_item(select)

    def initSelect(self, index, placeholder, removeIfExist):
        select = RoleSelect(placeholder = placeholder, custom_id = f"{self.custom_id}{index}", removeIfExist = removeIfExist)
        return select