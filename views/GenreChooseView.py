import discord
from discord.ui import View

from utils import GeneralUtils
from views.components import RoleSelect

class GenreChooseView(View):
    removeIfExist = False

    def __init__(self, removeIfExist: bool = False):
        self.removeIfExist = removeIfExist
        super().__init__(timeout=None)
        self.initSelects()

    def initSelects(self):
        placeholder = 'Make a selection'

        genreArray = GeneralUtils.getMusicGenres()
        genreSelect = self.initSelect(0, placeholder, self.removeIfExist)
        for genreObject in genreArray:
            if len(genreSelect.options) != 0 and len(genreSelect.options) % 25 == 0:
                self.add_item(genreSelect)
                genreSelect = self.initSelect(len(self.children), placeholder, self.removeIfExist)
            roleID = genreObject['roleID']
            displayName = genreObject['displayName']

            genreSelect.add_option(label = displayName, value = roleID)
        
        self.add_item(genreSelect)

    def initSelect(self, index, placeholder, removeIfExist):
        select = RoleSelect(placeholder = placeholder, custom_id = f"genre_select{index}", removeIfExist = removeIfExist)
        return select