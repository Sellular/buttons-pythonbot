import discord
from discord.ui import View

from views.components import RoleSelect

class RoleChooseView(View):
    updateMode = False
    custom_id = ""

    def __init__(self, options: list, custom_id: str, updateMode: bool = False):
        self.updateMode = updateMode
        self.custom_id = custom_id
        super().__init__(timeout=None)
        self.initSelects(options)
        

    def initSelects(self, options: list):
        placeholder = 'Make a selection'

        select = self.initSelect(0, placeholder, self.updateMode)
        for option in options:
            if len(select.options) != 0 and len(select.options) % 25 == 0:
                self.add_item(select)
                select = self.initSelect(len(self.children), placeholder, self.updateMode)
            roleID = option['roleID']
            displayName = option['displayName']

            select.add_option(label = displayName, value = roleID)
        
        self.add_item(select)

    def initSelect(self, index, placeholder, updateMode):
        select = RoleSelect(placeholder = placeholder, custom_id = f"{self.custom_id}{index}", updateMode = updateMode)
        return select       
