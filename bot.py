

import discord
from discord.ext import commands
from discord.ui import Button, View, Select
from discord import Intents
import asyncio


class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=('!'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(Welcome())
        self.add_view(Pronouns())
        self.add_view(Pronons())
        self.add_view(GenreChoose())
        self.add_view(GenreChoose2())
        self.add_view(GenreChooseV2())
        self.add_view(GenreChooseV3())
        self.add_view(LastMSG())
        self.add_view(LastMSGV2())
        self.add_view(DoneButton())
        self.add_view(Verification())

    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", bot.user.name)
        print("User ID: ", bot.user.id)
        print('-----')

bot = MyClient()

class Welcome(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    # async def interaction_check(self, interaction):
    #     user = interaction.user
    #     if user.joined_at(second=15):
    #         await interaction.response.send_message("You haven't read the rules yet.", ephemeral=True)    
    #         return False
    #     return True
    @discord.ui.button(label="Click here to start!", style=discord.ButtonStyle.green, custom_id="welcome_button")
    async def callback(self, interaction: discord.Interaction, button: discord.Button):
        user = interaction.user
        role = interaction.guild.get_role(987553778662268928)
        await user.add_roles(role)
        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.5)
        await interaction.followup.send(f"You now have the onboarding role! Head over to the <#987921414944350269> channel to pick some more!")

        self.value=False

class Pronouns(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        max_values=1,
        placeholder='Make selection',
        custom_id="pronoun_select",
        options=[
            discord.SelectOption(label='They/Them'),
            discord.SelectOption(label='She/Her'),
            discord.SelectOption(label='She/They'),
            discord.SelectOption(label='He/Him',),
            discord.SelectOption(label='He/They'),
            discord.SelectOption(label='Ask me'),
            discord.SelectOption(label='Any pronouns')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        # Selection
        if select.values[0] == 'He/Him':
            await interaction.response.edit_message(view=self)
            male_role = guild.get_role(891907652404248616)
            await member.add_roles(male_role)
        elif select.values[0] == 'He/They':
            await interaction.response.edit_message(view=self)
            malet_role = guild.get_role(987972562204110938)
            await member.add_roles(malet_role)
        elif select.values[0] == 'She/Her':
            await interaction.response.edit_message(view=self)
            female_role = guild.get_role(891907651720605709)
            await member.add_roles(female_role)
        elif select.values[0] == 'She/They':
            await interaction.response.edit_message(view=self)
            femalet_role = guild.get_role(987971942122397747)
            await member.add_roles(femalet_role)
        elif select.values[0] == 'They/Them':
            await interaction.response.edit_message(view=self)
            g_role = guild.get_role(891907651288580116)
            await member.add_roles(g_role)
        elif select.values[0] == 'Ask me':
            await interaction.response.edit_message(view=self)
            a_role = guild.get_role(891907650541994014)
            await member.add_roles(a_role)
        elif select.values[0] == 'Any pronouns':
            await interaction.response.edit_message(view=self)
            ask_role = guild.get_role(891910337262141500)
            await member.add_roles(ask_role)

        # Role assign message
        await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

class Pronons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        max_values=1,
        placeholder='Make selection',
        custom_id="pronon_select",
        options=[
            discord.SelectOption(label='They/Them'),
            discord.SelectOption(label='She/Her'),
            discord.SelectOption(label='She/They'),
            discord.SelectOption(label='He/Him',),
            discord.SelectOption(label='He/They'),
            discord.SelectOption(label='Ask me'),
            discord.SelectOption(label='Any pronouns')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        # Selection
        if select.values[0] == 'He/Him':
            await interaction.response.edit_message(view=self)
            male_role = guild.get_role(891907652404248616)
            if member.get_role(male_role.id):
                await member.remove_roles(male_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(male_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'He/They':
            await interaction.response.edit_message(view=self)
            malet_role = guild.get_role(987972562204110938)
            if member.get_role(malet_role.id):
                await member.remove_roles(malet_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(malet_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'She/Her':
            await interaction.response.edit_message(view=self)
            female_role = guild.get_role(891907651720605709)
            if member.get_role(female_role.id):
                await member.remove_roles(female_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(female_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'She/They':
            await interaction.response.edit_message(view=self)
            femalet_role = guild.get_role(987971942122397747)
            if member.get_role(femalet_role.id):
                await member.remove_roles(femalet_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(femalet_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'They/Them':
            await interaction.response.edit_message(view=self)
            g_role = guild.get_role(891907651288580116)
            if member.get_role(g_role.id):
                await member.remove_roles(g_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(g_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Any pronouns':
            await interaction.response.edit_message(view=self)
            a_role = guild.get_role(891907650541994014)
            if member.get_role(a_role.id):
                await member.remove_roles(a_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(a_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Ask me':
            await interaction.response.edit_message(view=self)
            ask_role = guild.get_role(891910337262141500)
            if member.get_role(ask_role.id):
                await member.remove_roles(ask_role)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(ask_role)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

class GenreChoose(discord.ui.View):
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
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
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

class GenreChoose2(discord.ui.View):
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
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
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

class GenreChooseV2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder='Make a selection',
        custom_id='genre_select_v2',
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
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user

        if select.values[0] == 'Alternative Rock':
            await interaction.response.edit_message(view=self)
            alternative_rock = guild.get_role(988255670610583603)
            if member.get_role(alternative_rock.id):
                await member.remove_roles(alternative_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(alternative_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Bluegrass':
            await interaction.response.edit_message(view=self)
            bluegrass = guild.get_role(988256949667766342)
            if member.get_role(bluegrass.id):
                await member.remove_roles(bluegrass)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(bluegrass)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Blues':
            await interaction.response.edit_message(view=self)
            blues = guild.get_role(988257041963442196)
            if member.get_role(blues.id):
                await member.remove_roles(blues)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(blues)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Christian Rock':
            await interaction.response.edit_message(view=self)
            christian_rock = guild.get_role(987971942122397747)
            if member.get_role(christian_rock.id):
                await member.remove_roles(christian_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(christian_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Classic Hip-Hop':
            await interaction.response.edit_message(view=self)
            classical_hip_hop = guild.get_role(988257181512134776)
            if member.get_role(classical_hip_hop.id):
                await member.remove_roles(classical_hip_hop)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(classical_hip_hop)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Classic Rock':
            await interaction.response.edit_message(view=self)
            classical_rock = guild.get_role(988257279285547119)
            if member.get_role(classical_rock.id):
                await member.remove_roles(classical_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(classical_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Classical':
            await interaction.response.edit_message(view=self)
            classical = guild.get_role(988257649437052948)
            if member.get_role(classical.id):
                await member.remove_roles(classical)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(classical)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Disco':
            await interaction.response.edit_message(view=self)
            disco = guild.get_role(988257743469170709)
            if member.get_role(disco.id):
                await member.remove_roles(disco)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(disco)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Dubstep':
            await interaction.response.edit_message(view=self)
            dubstep = guild.get_role(988257794559979540)
            if member.get_role(dubstep.id):
                await member.remove_roles(dubstep)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(dubstep)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'EDM':
            await interaction.response.edit_message(view=self)
            edm = guild.get_role(988257847492087879)
            if member.get_role(edm.id):
                await member.remove_roles(edm)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(edm)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Folk':
            await interaction.response.edit_message(view=self)
            folk = guild.get_role(988257882753609799)
            if member.get_role(folk.id):
                await member.remove_roles(folk)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(folk)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Funk':
            await interaction.response.edit_message(view=self)
            funk = guild.get_role(988260458169516072)
            if member.get_role(funk.id):
                await member.remove_roles(funk)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(funk)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Game Soundtrack':
            await interaction.response.edit_message(view=self)
            game_soundtrack = guild.get_role(988260475932397598)
            if member.get_role(game_soundtrack.id):
                await member.remove_roles(game_soundtrack)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(game_soundtrack)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        
        elif select.values[0] == 'House':
            await interaction.response.edit_message(view=self)
            house = guild.get_role(988260480067993620)
            if member.get_role(house.id):
                await member.remove_roles(house)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(house)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Indie':
            await interaction.response.edit_message(view=self)
            indie = guild.get_role(988260484849487952)
            if member.get_role(indie.id):
                await member.remove_roles(indie)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(indie)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Indie Rock':
            await interaction.response.edit_message(view=self)
            indie_rock = guild.get_role(988260484904005662)
            if member.get_role(indie_rock.id):
                await member.remove_roles(indie_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(indie_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Japanese Pop':
            await interaction.response.edit_message(view=self)
            japanese_pop = guild.get_role(988260484958535802)
            if member.get_role(japanese_pop.id):
                await member.remove_roles(japanese_pop)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(japanese_pop)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        
        elif select.values[0] == 'Japanese Rock':
            await interaction.response.edit_message(view=self)
            japanese_rock = guild.get_role(988260485000491059)
            if member.get_role(japanese_rock.id):
                await member.remove_roles(japanese_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(japanese_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Jazz':
            await interaction.response.edit_message(view=self)
            jazz = guild.get_role(988260487202504754)
            if member.get_role(jazz.id):
                await member.remove_roles(jazz)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(jazz)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Korean Pop':
            await interaction.response.edit_message(view=self)
            korean_pop = guild.get_role(988261063311126540)
            if member.get_role(korean_pop.id):
                await member.remove_roles(korean_pop)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(korean_pop)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Light Rock':
            await interaction.response.edit_message(view=self)
            light_rock = guild.get_role(988261069267009537)
            if member.get_role(light_rock.id):
                await member.remove_roles(light_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(light_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Liquid DnB':
            await interaction.response.edit_message(view=self)
            liquid_dnb = guild.get_role(988261070038786159)
            if member.get_role(liquid_dnb.id):
                await member.remove_roles(liquid_dnb)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(liquid_dnb)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Lofi':
            await interaction.response.edit_message(view=self)
            lofi = guild.get_role(988261078045712386)
            if member.get_role(lofi.id):
                await member.remove_roles(lofi)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(lofi)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Lounge':
            await interaction.response.edit_message(view=self)
            lounge = guild.get_role(988261078356074566)
            if member.get_role(lounge.id):
                await member.remove_roles(lounge)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(lounge)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

        elif select.values[0] == 'Math Rock':
            await interaction.response.edit_message(view=self)
            math_rock = guild.get_role(988261088778936390)
            if member.get_role(math_rock.id):
                await member.remove_roles(math_rock)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(math_rock)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

class GenreChooseV3(discord.ui.View):
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
    async def select_callback(self, interaction: discord.Interaction,  select: discord.ui.Select):
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

class LastMSG(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder = 'Make a selection',
        custom_id='last_select',
        options = [
            discord.SelectOption(label='Producer', value = 989040398766850099),
            discord.SelectOption(label='Audiophile', value = 989040473463193600)
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        bot.role_cache = {}
        bot.role_cache[f'{interaction.user.id}'] = select.values

        await interaction.response.send_message(f"Assigned role **{select.values[0]}**.", ephemeral=True)

class LastMSGV2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.select(
        placeholder = 'Make a selection',
        custom_id='last_select_v2',
        options = [
            discord.SelectOption(label='Producer'),
            discord.SelectOption(label='Audiophile')
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        
        if select.values[0] == 'Producer':
            await interaction.response.edit_message(view=self)
            producer = guild.get_role(989040398766850099)
            if member.get_role(producer.id):
                await member.remove_roles(producer)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(producer)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)
        elif select.values[0] == 'Audiophile':
            await interaction.response.edit_message(view=self)
            audioph = guild.get_role(989040473463193600)
            if member.get_role(audioph.id):
                await member.remove_roles(audioph)
                await interaction.followup.send(f"Removed role **{select.values[0]}**.", ephemeral=True)
            else:
                await member.add_roles(audioph)
                await interaction.followup.send(f"Assigned role **{select.values[0]}**.", ephemeral=True)

class DoneButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Click once you've assigned your roles!", style = discord.ButtonStyle.green, custom_id='done_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        verified = guild.get_role(987249040288784389)
        await member.add_roles(verified)
        removed_role = guild.get_role(987553778662268928)
        await member.remove_roles(removed_role)
        role_producer = 989040398766850099
        role_audiophile = 989040473463193600

        try:
            if str(role_producer) in bot.role_cache[str(interaction.user.id)]:
                role_pro = guild.get_role(role_producer)
                await member.add_roles(role_pro)
            if str(role_audiophile) in bot.role_cache[str(interaction.user.id)]:
                await interaction.response.send_message('smth')
        except:
            pass
        channel = guild.get_channel(989056168192274433)
        await channel.send(f"Hey Greeters! Let's give a warm welcome to {member.mention} of user who clicked the button! Once you've been introduced to our team, click this button to gain access to the rest of the server!", view = Verification())

class Verification(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Access the server!", style = discord.ButtonStyle.green, custom_id='verify_button')
    async def on_callback(self, interaction: discord.Interaction, button: discord.Button):
        guild = bot.get_guild(886770756262961172)
        member = interaction.user
        member_role = guild.get_role(886804525548187708)
        await interaction.response.defer(ephemeral=True, thinking=True)
        await asyncio.sleep(0.5)
        await interaction.followup.send("You now have the blues role! Enjoy your stay in our server!!")

# Welcome message
@bot.command()
async def welcome(ctx):
    view = Welcome()
    await ctx.send("**Welcome to the Rocket community!**\n\nIf you're new here, we want to let you in on a couple of secrets that'll help you be the best Rock'n member that ever was.")
    await ctx.send("**So, what do we talk about here?**\n\n:small_blue_diamond: Our favorite music! Everyone here has their unique tastes: grunge to funk, pop to indie, and everything in between.\n"+
    "- Looking for a place to start? Head over to <#886807336650420274>, your go-to place for general music discussion!\n"+
    "- Share your ~~fire mixtape~~ playlists with us in <#987236526452781127>! Check out the playlists already there too; you might find something you like. :slight_smile:\n"+
    "- Find a new song you love, or want to share an old, over-repeated favorite? Share it with us in <#987237047561519164>!\n"+
    "- Want to flex your concert experiences or your crippling vinyl addiction? Real life photos, videos, etc. go in <#987237253099167744>!\n\n"+
    ":small_blue_diamond: Making more music! We're happy to have some producers and of course, music fans, in our community. They'd love to help you master your favorite DAWs!\n"+
    "- Made something you want to share with us? <#987526774797774878> is the place for you!\n"+
    "- Want some help putting the finishing touches on your song, or need other support with producing? Get assistance in <#987526916904988682>!\n"+
    "- Looking to collab with fellow blues? Request 'em in <#987527070114541641>! When you're done, show us in the <#987526774797774878> channel!\n"+
    "- Need equipment and hardware advice? Or just want to show us that new MIDI keyboard you got? One stop to <#987527234367651850> will do the trick.")
    await ctx.send(":small_blue_diamond: Your awesome speaker and headphone setups! From home theaters to the best headset you've ever had, you're sure to find the audiophiles among us.\n"+
                            "- Finish setting up a new amp? Surround setup? HIFI conversations can be found in <#987529617302781982>!\n"+
                            "- Want some recommendations for new equipment? Wanna promote (#NotASponsor) an awesome new product? <#987529646151204955> has you covered.\n"+
                            "- Need some help untangling the speaker wires? Not sure where to put the subwoofer? Ask for assistance in <#987529675691675728>.")
    await ctx.send("**Cool, but like, are there things to DO?**\n\n"+
    ":small_blue_diamond: Of course! We host a variety of fun events for you all to participate in! We've got listening parties, talent shows, and everything in between.\n"+
    "      - You can find any ongoing and upcoming events in the events tab! Probably obvious, we know.\n"+
    ":small_blue_diamond: We host a weekly debate club - err… I mean, weekly discussion board, for all your hot takes, unpopular opinions, or general infodumps!\n"+
    "      - Which you can find in #question-of-the-week! Come on in, share your thoughts, and enjoy the conversation!\n"+
    ":small_blue_diamond: We got all the latest new release information and reviews for you to kick back and read!\n"+
    "      - Check out <#987246125138460692> for all the latest and greatest! After you're done listening (or before, we won't judge) you can head on over to <#987246068121088021> to see what other people are saying! Feel free to add to pre-existing threads and keep the conversation going!\n\n"+
    "**Sounds great! How do I join?**\n\n"+
    "We're happy to hear you say that! If you haven't already, be sure to familiarize yourself with our rules over in #welcome! When you come back, click that shiny verification button below and you're ready to go!",
    view=view)

@bot.command()
async def r(ctx):
    await ctx.send("Pick your pronoun roles here! We've got 'em all.", view=Pronouns())
    await ctx.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=GenreChoose())
    await ctx.send(view=GenreChoose2())
    await ctx.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=LastMSG())
    await ctx.send('Once you have finished selecting your roles, click this button to continue your onboarding', view=DoneButton())

@bot.command() 
async def s(ctx): 
    await ctx.send("Pick your pronoun roles here! We've got 'em all.", view=Pronons())
    await ctx.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=GenreChooseV2())
    await ctx.send(view=GenreChooseV3())
    await ctx.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=LastMSGV2())


bot.run('TOKEN')

