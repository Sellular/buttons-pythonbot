import discord
from discord.ext import commands

from dao import ChannelMessageDAO
from utils import GeneralUtils
from views import RoleChooseView, RoleSubmitButtonView, WelcomeView


async def clearChannel(channel_id: int, bot: commands.Bot):
    channel = bot.get_channel(channel_id)
    if (channel):
        await channel.purge(check=lambda message: True, bulk=True)
        return channel
    return None


async def getChannelMessage(messageCode: str, channel: discord.TextChannel, bot: commands.Bot):
    message = None
    try:
        channelMessage = ChannelMessageDAO.getChannelMessageByCode(messageCode)
        if channelMessage:
            message = await channel.fetch_message(int(channelMessage.messageID))
        else:
            ChannelMessageDAO.deleteChannelMessageByCode(messageCode)
    except Exception as error:
        print(error)
    finally:
        return message

async def updateInfo(bot: commands.Bot):
    try:
        guildConfig = GeneralUtils.getConfig('guild')
        if not guildConfig:
            raise Exception("Guild config not found.")

        infoChannelId = guildConfig['info_channel_id']
        if not infoChannelId:
            raise Exception("INFO_CHANNEL_ID Not found in Guild config.")

        infoChannel = bot.get_channel(int(infoChannelId))
        if not infoChannel:
            raise Exception("Info channel not found in discord guild.")

        infoEmbed1 = discord.Embed(title="Welcome to the Rok & Roll community!")
        infoEmbed1.add_field(name="\u200b", value="If you're new here, we want to let you in on a couple of secrets that'll help you be the best Roll member that ever was. So, what do we talk about here?\n\n" +
            "****:small_blue_diamond: Our favorite music!**\n\n" + 
            "Everyone here has their unique tastes: grunge to funk, pop to indie, and everything in between.\n\n" +
            f":bnumber_1: <#{guildConfig['main_st_channel_id']}> is your go-to place for general music discussion. This is your place to start!\n" +
            f":bnumber_2: <#{guildConfig['playlists_channel_id']}> is where you can share your ~~fire mixtape~~ playlists with us! Check out the playlists already there too; you might find something you like.\n" +
            f":bnumber_3: <#{guildConfig['your_favs_channel_id']}> is for posting a new song you love, or if want to share an old, over-repeated favorite!\n" +
            f":bnumber_4: <#{guildConfig['music_irl_channel_id']}> is here for you to flex your concert experiences or your crippling vinyl addiction! Real-life photos, videos, and all real-world music go here!\n\n" +
            "**:small_blue_diamond: Making more music!**\n" +
            "We're happy to have some producers and of course, music fans, in our community. They'd love to help you master your favorite DAWs!\n\n" +
            f":bnumber_1: <#{guildConfig['show_off_channel_id']}> is for if you made something you want to share with us!\n" +
            f":bnumber_2: <#{guildConfig['ask_the_roll_channel_id']}> go here if you want some help putting the finishing touches on your song, or need other support with producing! This is your assistance hub.\n" +
            f":bnumber_3: <#{guildConfig['collab_channel_id']}> is your go-to when looking to collab with a fellow roll. When you're done, show us in the <#{guildConfig['show_off_channel_id']}> channel!\n" +
            f":bnumber_4: <#{guildConfig['equipment_channel_id']}> is here when you need equipment and hardware advice, or just want to show us that new MIDI keyboard you got! One stop here will do the trick.\n\n" +
            "**:small_blue_diamond: Your awesome speaker and headphone setups!**\n" +
            "From home theaters to the best headset you've ever had, you're sure to find the audiophiles among us.\n\n" +
            f":bnumber_1: <#{guildConfig['hifi_channel_id']}> conversations can be found here! Finish setting up a new amp? Surround setup? Show us it all!\n" +
            f":bnumber_2: <#{guildConfig['tech_recommendations_channel_id']}> can be used for some recommendations for new equipment! Wanna promote (#NotASponsor) an awesome new product? This channel has you covered.\n" +
            f":bnumber_3: <#{guildConfig['speaker_setup_channel_id']}> for all your help untangling the speaker wires. Not sure where to put the subwoofer? Ask here!")
        
        infoEmbed2 = discord.Embed(title="Cool, but like, are there things to DO?")
        infoEmbed2.add_field(name="\u200b", value="Of course! We host a variety of fun events for you all to participate in! We've got listening parties, talent shows, and everything in between. You can find any ongoing and upcoming events in the events tab! Probably obvious, we know.\n\n" +
            "**:small_blue_diamond: Weekly Debate Club!**\n" +
            "err… I mean, weekly discussion board, for all your hot takes, unpopular opinions, or general infodumps!\n\n" +
            f"Which you can find in <#{guildConfig['weekly_discussion_channel_id']}>! Come on in, share your thoughts, and enjoy the conversation!\n\n" +
            "**:small_blue_diamond: Latest new release information and reviews!**\n" +
            "We got all the latest new release information and reviews for you to kick back and read!\n\n" +
            f"Check out <#{guildConfig['whats_new_channel_id']}> for all the latest and greatest! After you're done listening (or before, we won't judge) you can head on over to <#{guildConfig['reviews_channel_id']}> to see what other people are saying! Feel free to add to pre-existing threads and keep the conversation going!")

        infoMessage1 = await getChannelMessage("infoMessage1", infoChannel, bot)
        infoMessage2 = await getChannelMessage("infoMessage2", infoChannel, bot)

        if infoMessage1:
            await infoMessage1.edit(embed=infoEmbed1)
        else:
            infoMessage1 = await infoChannel.send(embed=infoEmbed1)
            ChannelMessageDAO.insert(infoMessage1.id, "infoMessage1")

        if infoMessage2:
            await infoMessage2.edit(embed=infoEmbed2)
        else:
            infoMessage2 = await infoChannel.send(embed=infoEmbed2)
            ChannelMessageDAO.insert(infoMessage2.id, "infoMessage2")

    except Exception as error:
        print(error)

async def updateWelcome(bot: commands.Bot):
    try:
        guildConfig = GeneralUtils.getConfig('guild')
        if not guildConfig:
            raise Exception("Guild config not found.")

        welcomeChannelId = guildConfig['welcome_channel_id']
        if not welcomeChannelId:
            raise Exception("WELCOME_CHANNEL_ID Not found in Guild config.")

        welcomeChannel = bot.get_channel(int(welcomeChannelId))
        if not welcomeChannel:
            raise Exception("Welcome channel not found in discord guild.")

        welcomeDialog1 = "%s" % ("**Welcome to the Rok & Roll community!** \n\n" +
            "If you're new here, we want to let you in on a couple of secrets that'll help you be the best Roll member that ever was.\n")
        welcomeDialog2 = "%s" % ("**So, what do we talk about here?** \n" +
            "\n" +
            ":small_blue_diamond: Our favorite music! Everyone here has their unique tastes: grunge to funk, pop to indie, and everything in between.\n" +
            f"   - Looking for a place to start? Head over to <#{guildConfig['main_st_channel_id']}>, your go-to place for general music discussion!\n" +
            f"   - Share your ~~fire mixtape~~ playlists with us in <#{guildConfig['playlists_channel_id']}>! Check out the playlists already there too; you might find something you like. :slight_smile:\n" +
            f"   - Find a new song you love, or want to share an old, over-repeated favorite? Share it with us in <#{guildConfig['your_favs_channel_id']}>!\n" +
            f"   - Want to flex your concert experiences or your crippling vinyl addiction? Real life photos, videos, etc. go in <#{guildConfig['music_irl_channel_id']}>!\n" +
            "\n" +
            ":small_blue_diamond: Making more music! We're happy to have some producers and of course, music fans, in our community. They'd love to help you master your favorite DAWs!\n" +
            f"   - Made something you want to share with us? <#{guildConfig['show_off_channel_id']}> is the place for you!\n" +
            f"   - Want some help putting the finishing touches on your song, or need other support with producing? Get assistance in <#{guildConfig['ask_the_roll_channel_id']}>!\n" +
            f"   - Looking to collab with a fellow roll? Request 'em in <#{guildConfig['collab_channel_id']}>! When you're done, show us in the <#{guildConfig['show_off_channel_id']}> channel!\n" +
            f"   - Need equipment and hardware advice? Or just want to show us that new MIDI keyboard you got? One stop to <#{guildConfig['equipment_channel_id']}> will do the trick.\n")
        welcomeDialog3 = "%s" % ("**:small_blue_diamond: Your awesome speaker and headphone setups! From home theaters to the best headset you've ever had, you're sure to find the audiophiles among us.\n" +
            f"   - Finish setting up a new amp? Surround setup? HIFI conversations can be found in <#{guildConfig['hifi_channel_id']}>!\n" +
            f"   - Want some recommendations for new equipment? Wanna promote (#NotASponsor) an awesome new product? <#{guildConfig['tech_recommendations_channel_id']}> has you covered.\n" +
            f"   - Need some help untangling the speaker wires? Not sure where to put the subwoofer? Ask for assistance in <#{guildConfig['speaker_setup_channel_id']}>.")
        welcomeDialog4 = "%s" % ("**Cool, but like, are there things to DO?**\n" +
            "\n" +
            ":small_blue_diamond: Of course! We host a variety of fun events for you all to participate in! We've got listening parties, talent shows, and everything in between.\n" +
            "    - You can find any ongoing and upcoming events in the events tab! Probably obvious, we know.\n" +
            "\n" +
            ":small_blue_diamond: We host a weekly debate club - err… I mean, weekly discussion board, for all your hot takes, unpopular opinions, or general infodumps!\n" +
            f"   - Which you can find in <#{guildConfig['weekly_discussion_channel_id']}>! Come on in, share your thoughts, and enjoy the conversation!\n" +
            "\n" +
            ":small_blue_diamond: We got all the latest new release information and reviews for you to kick back and read!\n" +
            f"   - Check out <#{guildConfig['whats_new_channel_id']}> for all the latest and greatest! After you're done listening (or before, we won't judge) you can head on over to <#{guildConfig['reviews_channel_id']}> to see what other people are saying! Feel free to add to pre-existing threads and keep the conversation going!\n" +
            "\n" +
            "**Sounds great! How do I join?**\n" +
            "\n" +
            "We're happy to hear you say that! If you haven't already, be sure to familiarize yourself with our rules over in #welcome! When you come back, click that shiny verification button below and you're ready to go!")

        welcomeView = WelcomeView()

        welcomeMessage1 = await getChannelMessage("welcomeMessage1", welcomeChannel, bot)
        welcomeMessage2 = await getChannelMessage("welcomeMessage2", welcomeChannel, bot)
        welcomeMessage3 = await getChannelMessage("welcomeMessage3", welcomeChannel, bot)
        welcomeMessage4 = await getChannelMessage("welcomeMessage4", welcomeChannel, bot)

        if welcomeMessage1:
            await welcomeMessage1.edit(content=welcomeDialog1)
        else:
            welcomeMessage1 = await welcomeChannel.send(content=welcomeDialog1)
            ChannelMessageDAO.insert(welcomeMessage1.id, "welcomeMessage1")

        if welcomeMessage2:
            await welcomeMessage2.edit(content=welcomeDialog2)
        else:
            welcomeMessage2 = await welcomeChannel.send(content=welcomeDialog2)
            ChannelMessageDAO.insert(welcomeMessage2.id, "welcomeMessage2")

        if welcomeMessage3:
            await welcomeMessage3.edit(content=welcomeDialog3)
        else:
            welcomeMessage3 = await welcomeChannel.send(content=welcomeDialog3)
            ChannelMessageDAO.insert(welcomeMessage3.id, "welcomeMessage3")

        if welcomeMessage4:
            await welcomeMessage4.edit(content=welcomeDialog4)
        else:
            welcomeMessage4 = await welcomeChannel.send(content=welcomeDialog4, view=welcomeView)
            ChannelMessageDAO.insert(welcomeMessage4.id, "welcomeMessage4")


    except Exception as error:
        print(error)
        return


async def updateAddRoles(bot: commands.Bot):
    await __updateRoles(bot, False)


async def updateUpdateRoles(bot: commands.Bot):
    await __updateRoles(bot, True)


async def __updateRoles(bot: commands.Bot, updateMode: bool):
    guildConfig = None
    try:
        guildConfig = GeneralUtils.getConfig('guild')

        if not guildConfig:
            raise Exception("Guild config not found.")
        
        role_channel_id = guildConfig[f'{"update" if updateMode else "add"}_roles_channel_id']
        if not role_channel_id:
            raise Exception("Role channel id not found in Guild config.")

        channel = bot.get_channel(int(role_channel_id))
        if not channel:
            raise Exception("Role channel not found in discord Guild.")
        pronounArray = GeneralUtils.getPronouns()
        genreArray = GeneralUtils.getMusicGenres()
        hobbyArray = GeneralUtils.getHobbies()
        notificationArray = GeneralUtils.getNotifications()

        prefix = 'update_' if updateMode else ''

        pronounChooseView = RoleChooseView(
            options=pronounArray, custom_id=f"{prefix}pronoun_select", updateMode=updateMode)
        genreChooseView = RoleChooseView(
            options=genreArray, custom_id=f"{prefix}genre_select", updateMode=updateMode)
        hobbyChooseView = RoleChooseView(
            options=hobbyArray, custom_id=f"{prefix}hobby_select", updateMode=updateMode)
        notificationChooseView = RoleChooseView(
            options=notificationArray, custom_id=f"{prefix}notification_select", updateMode=updateMode)

        pronounsMessage = await getChannelMessage(f"{prefix}pronouns", channel, bot)
        genresMessage = await getChannelMessage(f"{prefix}genres", channel, bot)
        hobbiesMessage = await getChannelMessage(f"{prefix}hobbies", channel, bot)
        notificationsMessage = await getChannelMessage(
            f"{prefix}notifications", channel, bot)

        pronounsDialog = "Pick your pronoun roles here! We've got 'em all.!!!!!!!!!!!!"
        genresDialog = f"Choose your genre preferences! Don't see your favs? You can suggest it in <#{guildConfig['server_feedback_channel_id']}>."
        hobbiesDialog = 'Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!'
        notificationsDialog = 'Want to get notified about the latest events? Want to know about the newest releases in the music world? Notification roles are all here!'

        if pronounsMessage:
            await pronounsMessage.edit(content=pronounsDialog,
                                view=pronounChooseView)
        else:
            pronounsMessage = await channel.send(content=pronounsDialog, view=pronounChooseView)
            ChannelMessageDAO.insert(pronounsMessage.id, f"{prefix}pronouns")

        if genresMessage:
            await genresMessage.edit(content=genresDialog, view=genreChooseView)
        else:
            genresMessage = await channel.send(content=genresDialog, view=genreChooseView)
            ChannelMessageDAO.insert(genresMessage.id, f"{prefix}genres")

        if hobbiesMessage:
            await hobbiesMessage.edit(content=hobbiesDialog, view=hobbyChooseView)
        else:
            hobbiesMessage = await channel.send(content=hobbiesDialog, view=hobbyChooseView)
            ChannelMessageDAO.insert(hobbiesMessage.id, f"{prefix}hobbies")

        if notificationsMessage:
            await notificationsMessage.edit(
                content=notificationsDialog, view=notificationChooseView)
        else:
            notificationsMessage = await channel.send(content=notificationsDialog, view=notificationChooseView)
            ChannelMessageDAO.insert(
                notificationsMessage.id, f"{prefix}notifications")

        if not updateMode:
            submitMessage = await getChannelMessage("submit", channel, bot)
            submitDialog = 'Once you have finished selecting your roles, click this button to continue your onboarding'
            doneButtonView = RoleSubmitButtonView(select_views=[
                pronounChooseView, genreChooseView, notificationChooseView, hobbyChooseView], custom_id="submit_button")

            if submitMessage:
                await submitMessage.edit(content=submitDialog, view=doneButtonView)
            else:
                submitMessage = await channel.send(content=submitDialog, view=doneButtonView)
                ChannelMessageDAO.insert(submitMessage.id, "submit")
    except Exception as error:
        print(error)