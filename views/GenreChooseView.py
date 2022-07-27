import discord
from discord.ui import View, Select

class GenreChooseView(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder='Make a selection',
        custom_id='genre_select',
        options=[
            discord.SelectOption(label='Alternative Rock'),
            discord.SelectOption(label='Bluegrass'),
            discord.SelectOption(label='Blues'),
            discord.SelectOption(label='Christian Rock',),
            discord.SelectOption(label='Classic Hip-Hop'),
            discord.SelectOption(label='Classic Rock'),
            discord.SelectOption(label='Classical'),
            discord.SelectOption(label='Disco'),
            discord.SelectOption(label='Dubstep'),
            discord.SelectOption(label='EDM'),
            discord.SelectOption(label='Folk'),
            discord.SelectOption(label='Funk'),
            discord.SelectOption(label='Game Soundtrack'),
            discord.SelectOption(label='House'),
            discord.SelectOption(label='Indie'),
            discord.SelectOption(label='Indie Rock'),
            discord.SelectOption(label='Japanese Pop'),
            discord.SelectOption(label='Japanese Rock'),
            discord.SelectOption(label='Jazz'),
            discord.SelectOption(label='Korean Pop'),
            discord.SelectOption(label='Light Rock'),
            discord.SelectOption(label='Liquid DnB'),
            discord.SelectOption(label='Lofi'),
            discord.SelectOption(label='Lounge'),
            discord.SelectOption(label='Math Rock'),
        ]
    )
    async def select_callback(self, interaction: discord.Interaction,  select: Select):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        if select.values[0] == 'Alternative Rock':
            await interaction.response.edit_message(view=self)
            alternative_rock = guild.get_role(988255670610583603)
            await member.add_roles(alternative_rock)

        elif select.values[0] == 'Bluegrass':
            await interaction.response.edit_message(view=self)
            bluegrass = guild.get_role(988256949667766342)
            await member.add_roles(bluegrass)

        elif select.values[0] == 'Blues':
            await interaction.response.edit_message(view=self)
            blues = guild.get_role(988257041963442196)
            await member.add_roles(blues)

        elif select.values[0] == 'Christian Rock':
            await interaction.response.edit_message(view=self)
            christian_rock = guild.get_role(987971942122397747)
            await member.add_roles(christian_rock)

        elif select.values[0] == 'Classic Hip-Hop':
            await interaction.response.edit_message(view=self)
            classical_hip_hop = guild.get_role(988257181512134776)
            await member.add_roles(classical_hip_hop)

        elif select.values[0] == 'Classic Rock':
            await interaction.response.edit_message(view=self)
            classical_rock = guild.get_role(988257279285547119)
            await member.add_roles(classical_rock)

        elif select.values[0] == 'Classical':
            await interaction.response.edit_message(view=self)
            classical = guild.get_role(988257649437052948)
            await member.add_roles(classical)

        elif select.values[0] == 'Disco':
            await interaction.response.edit_message(view=self)
            disco = guild.get_role(988257743469170709)
            await member.add_roles(disco)

        elif select.values[0] == 'Dubstep':
            await interaction.response.edit_message(view=self)
            dubstep = guild.get_role(988257794559979540)
            await member.add_roles(dubstep)

        elif select.values[0] == 'EDM':
            await interaction.response.edit_message(view=self)
            edm = guild.get_role(988257847492087879)
            await member.add_roles(edm)

        elif select.values[0] == 'Folk':
            await interaction.response.edit_message(view=self)
            folk = guild.get_role(988257882753609799)
            await member.add_roles(folk)

        elif select.values[0] == 'Funk':
            await interaction.response.edit_message(view=self)
            funk = guild.get_role(988260458169516072)
            await member.add_roles(funk)

        elif select.values[0] == 'Game Soundtrack':
            await interaction.response.edit_message(view=self)
            game_soundtrack = guild.get_role(988260475932397598)
            await member.add_roles(game_soundtrack)
        
        elif select.values[0] == 'House':
            await interaction.response.edit_message(view=self)
            house = guild.get_role(988260480067993620)
            await member.add_roles(house)

        elif select.values[0] == 'Indie':
            await interaction.response.edit_message(view=self)
            indie = guild.get_role(988260484849487952)
            await member.add_roles(indie)

        elif select.values[0] == 'Indie Rock':
            await interaction.response.edit_message(view=self)
            indie_rock = guild.get_role(988260484904005662)
            await member.add_roles(indie_rock)

        elif select.values[0] == 'Japanese Pop':
            await interaction.response.edit_message(view=self)
            japanese_pop = guild.get_role(988260484958535802)
            await member.add_roles(japanese_pop)
        
        elif select.values[0] == 'Japanese Rock':
            await interaction.response.edit_message(view=self)
            japanese_rock = guild.get_role(988260485000491059)
            await member.add_roles(japanese_rock)

        elif select.values[0] == 'Jazz':
            await interaction.response.edit_message(view=self)
            jazz = guild.get_role(988260487202504754)
            await member.add_roles(jazz)

        elif select.values[0] == 'Korean Pop':
            await interaction.response.edit_message(view=self)
            korean_pop = guild.get_role(988261063311126540)
            await member.add_roles(korean_pop)

        elif select.values[0] == 'Light Rock':
            await interaction.response.edit_message(view=self)
            light_rock = guild.get_role(988261069267009537)
            await member.add_roles(light_rock)

        elif select.values[0] == 'Liquid DnB':
            await interaction.response.edit_message(view=self)
            liquid_dnb = guild.get_role(988261070038786159)
            await member.add_roles(liquid_dnb)

        elif select.values[0] == 'Lofi':
            await interaction.response.edit_message(view=self)
            lofi = guild.get_role(988261078045712386)
            await member.add_roles(lofi)

        elif select.values[0] == 'Lounge':
            await interaction.response.edit_message(view=self)
            lounge = guild.get_role(988261078356074566)
            await member.add_roles(lounge)

        elif select.values[0] == 'Math Rock':
            await interaction.response.edit_message(view=self)
            math_rock = guild.get_role(988261088778936390)
            await member.add_roles(math_rock)

        await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)