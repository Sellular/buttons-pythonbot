import discord

from utils import GeneralUtils
from views import RoleChooseView, RoleSubmitButtonView


async def clearChannel(channel_id: int, bot: discord.Client):
    channel = bot.get_channel(channel_id)
    if (channel):
        await channel.purge(check=lambda message: True, bulk=True)
        return channel
    return None


async def sendAddRoles(bot: discord.Client):
    await __sendRoles(bot, False)


async def sendUpdateRoles(bot: discord.Client):
    await __sendRoles(bot, True)


async def __sendRoles(bot: discord.Client, updateMode: bool):
    guildConfig = None
    try:
        guildConfig = GeneralUtils.getConfig('guild')
    except Exception as error:
        print(error)
        return
    channel = bot.get_channel(
        int(guildConfig[f'{"update" if updateMode else "add"}_roles_channel_id']))
    if channel:
        pronounArray = GeneralUtils.getPronouns()
        genreArray = GeneralUtils.getMusicGenres()
        hobbyArray = GeneralUtils.getHobbies()
        notificationArray = GeneralUtils.getNotifications()

        pronounChooseView = RoleChooseView(
            options=pronounArray, custom_id=f"{'update_' if updateMode else ''}pronoun_select", updateMode=updateMode)
        genreChooseView = RoleChooseView(
            options=genreArray, custom_id=f"{'update_' if updateMode else ''}genre_select", updateMode=updateMode)
        hobbyChooseView = RoleChooseView(
            options=hobbyArray, custom_id=f"{'update_' if updateMode else ''}hobby_select", updateMode=updateMode)
        notificationChooseView = RoleChooseView(
            options=notificationArray, custom_id=f"{'update_' if updateMode else ''}notification_select", updateMode=updateMode)

        await channel.send("Pick your pronoun roles here! We've got 'em all.", view=pronounChooseView)
        await channel.send("Choose your genre preferences! Don't see your favs? You can suggest it in <#962242442193670204>.", view=genreChooseView)
        await channel.send('Do you like making music? Are you interested in things like beat loops and DAWs? Then the __producer__ role is for you! Are you interested in speaker setups? Do you own/want a high quality DAC and some high impedance headphones? Then the __audiophile__ role is for you!', view=hobbyChooseView)
        await channel.send('Want to get notified about the latest events? Want to know about the newest releases in the music world? Notification roles are all here!', view=notificationChooseView)
        if not updateMode:
            doneButtonView = RoleSubmitButtonView(select_views=[
                pronounChooseView, genreChooseView, notificationChooseView, hobbyChooseView], custom_id="submit_button")
            await channel.send('Once you have finished selecting your roles, click this button to continue your onboarding', view=doneButtonView)
        else:
            await channel.send("Roles channel not found. Contact the bot developer or server administrator.", ephemeral=True)
