import discord
from discord.ui import View, Select

class GenreChooseV3View(View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder='Make a selection',
        custom_id='genre_select_v3',
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
            if member.get_role(metal.id):
                await member.remove_roles(metal)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(metal)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Modern Country':
            await interaction.response.edit_message(view=self)
            moden_country = guild.get_role(988263379967836180)
            if member.get_role(moden_country.id):
                await member.remove_roles(moden_country)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(moden_country)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Modern Hip-Hop':
            await interaction.response.edit_message(view=self)
            modern_hip_hop = guild.get_role(988263474398363678)
            if member.get_role(modern_hip_hop.id):
                await member.remove_roles(modern_hip_hop)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(modern_hip_hop)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Modern Rock':
            await interaction.response.edit_message(view=self)
            modern_rock = guild.get_role(988263575116197918)
            if member.get_role(modern_rock.id):
                await member.remove_roles(modern_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(modern_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Musicals':
            await interaction.response.edit_message(view=self)
            musicals = guild.get_role(988263644917821480)
            if member.get_role(musicals.id):
                await member.remove_roles(musicals)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(musicals)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Neuro DnB':
            await interaction.response.edit_message(view=self)
            neuro_dnb = guild.get_role(988263710768369734)
            if member.get_role(neuro_dnb.id):
                await member.remove_roles(neuro_dnb)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(neuro_dnb)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (10s & now)':
            await interaction.response.edit_message(view=self)
            pop_10 = guild.get_role(988263843681697864)
            if member.get_role(pop_10.id):
                await member.remove_roles(pop_10)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_10)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (20s)':
            await interaction.response.edit_message(view=self)
            pop_20 = guild.get_role(988263965614284930)
            if member.get_role(pop_20.id):
                await member.remove_roles(pop_20)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_20)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (90s)':
            await interaction.response.edit_message(view=self)
            pop_90 = guild.get_role(988264021121699870)
            if member.get_role(pop_90.id):
                await member.remove_roles(pop_90)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_90)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (80s)':
            await interaction.response.edit_message(view=self)
            pop_80s = guild.get_role(988264093905453077)
            if member.get_role(pop_80s.id):
                await member.remove_roles(pop_80s)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_80s)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (70s)':
            await interaction.response.edit_message(view=self)
            pop_70 = guild.get_role(988264175950254140)
            if member.get_role(pop_70.id):
                await member.remove_roles(pop_70)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_70)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Pop (60s)':
            await interaction.response.edit_message(view=self)
            pop_60 = guild.get_role(988264263544082473)
            if member.get_role(pop_60.id):
                await member.remove_roles(pop_60)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(pop_60)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Post-Rock':
            await interaction.response.edit_message(view=self)
            post_rock = guild.get_role(988261089210953789)
            if member.get_role(post_rock.id):
                await member.remove_roles(post_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(post_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        
        elif select.values[0] == 'Swing':
            await interaction.response.edit_message(view=self)
            swing = guild.get_role(988256941916692550)
            if member.get_role(swing.id):
                await member.remove_roles(swing)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(swing)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Synthwave':
            await interaction.response.edit_message(view=self)
            synthwave = guild.get_role(988264328295743558)
            if member.get_role(synthwave.id):
                await member.remove_roles(synthwave)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(synthwave)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Trap':
            await interaction.response.edit_message(view=self)
            trap = guild.get_role(988264418720747540)
            if member.get_role(trap.id):
                await member.remove_roles(trap)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(trap)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Rock':
            await interaction.response.edit_message(view=self)
            rock = guild.get_role(988264452161961995)
            if member.get_role(rock.id):
                await member.remove_roles(rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)