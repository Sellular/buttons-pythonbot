import discord
from discord.ui import View, Select

class GenreChoose2View(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder='Make a selection',
        custom_id='genre2_select',
        options=[
            discord.SelectOption(label='Metal'),
            discord.SelectOption(label='Modern Country'),
            discord.SelectOption(label='Modern Hip-Hop'),
            discord.SelectOption(label='Modern Rock',),
            discord.SelectOption(label='Musicals'),
            discord.SelectOption(label='Neuro DnB'),
            discord.SelectOption(label='Pop (10s & now)'),
            discord.SelectOption(label='Pop (20s)'),
            discord.SelectOption(label='Pop (90s)'),
            discord.SelectOption(label='Pop (80s)'),
            discord.SelectOption(label='Pop (70s)'),
            discord.SelectOption(label='Pop (60s)'),
            discord.SelectOption(label='Post-Rock'),
            discord.SelectOption(label='Swing'),
            discord.SelectOption(label='Synthwave'),
            discord.SelectOption(label='Trap'),
            discord.SelectOption(label='Rock')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction,  select: Select):
        bot = interaction.client
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        if select.values[0] == 'Metal':
            await interaction.response.edit_message(view=self)
            metal = guild.get_role(988263282332799036)
            await member.add_roles(metal)

        elif select.values[0] == 'Modern Country':
            await interaction.response.edit_message(view=self)
            moden_country = guild.get_role(988263379967836180)
            await member.add_roles(moden_country)

        elif select.values[0] == 'Modern Hip-Hop':
            await interaction.response.edit_message(view=self)
            modern_hip_hop = guild.get_role(988263474398363678)
            await member.add_roles(modern_hip_hop)

        elif select.values[0] == 'Modern Rock':
            await interaction.response.edit_message(view=self)
            modern_rock = guild.get_role(988263575116197918)
            await member.add_roles(modern_rock)

        elif select.values[0] == 'Musicals':
            await interaction.response.edit_message(view=self)
            musicals = guild.get_role(988263644917821480)
            await member.add_roles(musicals)

        elif select.values[0] == 'Neuro DnB':
            await interaction.response.edit_message(view=self)
            neuro_dnb = guild.get_role(988263710768369734)
            await member.add_roles(neuro_dnb)

        elif select.values[0] == 'Pop (10s & now)':
            await interaction.response.edit_message(view=self)
            pop_10 = guild.get_role(988263843681697864)
            await member.add_roles(pop_10)

        elif select.values[0] == 'Pop (20s)':
            await interaction.response.edit_message(view=self)
            pop_20 = guild.get_role(988263965614284930)
            await member.add_roles(pop_20)

        elif select.values[0] == 'Pop (90s)':
            await interaction.response.edit_message(view=self)
            pop_90 = guild.get_role(988264021121699870)
            await member.add_roles(pop_90)

        elif select.values[0] == 'Pop (80s)':
            await interaction.response.edit_message(view=self)
            pop_80s = guild.get_role(988264093905453077)
            await member.add_roles(pop_80s)

        elif select.values[0] == 'Pop (70s)':
            await interaction.response.edit_message(view=self)
            pop_70 = guild.get_role(988264175950254140)
            await member.add_roles(pop_70)

        elif select.values[0] == 'Pop (60s)':
            await interaction.response.edit_message(view=self)
            pop_60 = guild.get_role(988264263544082473)
            await member.add_roles(pop_60)

        elif select.values[0] == 'Post-Rock':
            await interaction.response.edit_message(view=self)
            post_rock = guild.get_role(988261089210953789)
            await member.add_roles(post_rock)
        
        elif select.values[0] == 'Swing':
            await interaction.response.edit_message(view=self)
            swing = guild.get_role(988256941916692550)
            await member.add_roles(swing)

        elif select.values[0] == 'Synthwave':
            await interaction.response.edit_message(view=self)
            synthwave = guild.get_role(988264328295743558)
            await member.add_roles(synthwave)

        elif select.values[0] == 'Trap':
            await interaction.response.edit_message(view=self)
            trap = guild.get_role(988264418720747540)
            await member.add_roles(trap)

        elif select.values[0] == 'Rock':
            await interaction.response.edit_message(view=self)
            rock = guild.get_role(988264452161961995)
            await member.add_roles(rock)

        await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)