from discord.ext import commands

from views import WelcomeView
from utils import GeneralUtils

class StartCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def start(self, ctx):
        try:
            guildConfig = GeneralUtils.getConfig('guild')
        except Exception as error:
            print(error)
            return
        welcome_view = WelcomeView()

        # await ctx.send("**Welcome to the Rok & Roll community!** \n" +
        #                    "If you're new here, we want to let you in on a couple of secrets that'll help you be the best Roll member that ever was.")
        # await ctx.send("**So, what do we talk about here?** \n" +
        #                    "\n" +
        #                    ":small_blue_diamond: Our favorite music! Everyone here has their unique tastes: grunge to funk, pop to indie, and everything in between.\n" +
        #                    f"- Looking for a place to start? Head over to <#{guildConfig['main_st_channel_id']}>, your go-to place for general music discussion!\n" +
        #                    f"- Share your ~~fire mixtape~~ playlists with us in <#{guildConfig['playlists_channel_id']}>! Check out the playlists already there too; you might find something you like. :slight_smile:\n" +
        #                    f"- Find a new song you love, or want to share an old, over-repeated favorite? Share it with us in <#{guildConfig['your_favs_channel_id']}>!\n" +
        #                    f"- Want to flex your concert experiences or your crippling vinyl addiction? Real life photos, videos, etc. go in <#{guildConfig['music_irl_channel_id']}>!\n" +
        #                    "\n" +
        #                    ":small_blue_diamond: Making more music! We're happy to have some producers and of course, music fans, in our community. They'd love to help you master your favorite DAWs!\n" +
        #                    f"- Made something you want to share with us? <#{guildConfig['show_off_channel_id']}> is the place for you!\n" +
        #                    f"- Want some help putting the finishing touches on your song, or need other support with producing? Get assistance in <#{guildConfig['ask_the_roll_channel_id']}>!\n" +
        #                    f"- Looking to collab with fellow rolls? Request 'em in <#{guildConfig['collab_channel_id']}>! When you're done, show us in the <#{guildConfig['show_off_channel_id']}> channel!\n" +
        #                    f"- Need equipment and hardware advice? Or just want to show us that new MIDI keyboard you got? One stop to <#{guildConfig['equipment_channel_id']}> will do the trick.")
        # await ctx.send(":small_blue_diamond: Your awesome speaker and headphone setups! From home theaters to the best headset you've ever had, you're sure to find the audiophiles among us.\n" +
        #                    f"- Finish setting up a new amp? Surround setup? HIFI conversations can be found in <#{guildConfig['hifi_channel_id']}>!\n" +
        #                    f"- Want some recommendations for new equipment? Wanna promote (#NotASponsor) an awesome new product? <#{guildConfig['tech_recommendations_channel_id']}> has you covered.\n" +
        #                    f"- Need some help untangling the speaker wires? Not sure where to put the subwoofer? Ask for assistance in <#{guildConfig['speaker_setup_channel_id']}>.")
        # await ctx.send("**Cool, but like, are there things to DO?**\n" +
        #                    ":small_blue_diamond: Of course! We host a variety of fun events for you all to participate in! We've got listening parties, talent shows, and everything in between.\n" +
        #                    "- You can find any ongoing and upcoming events in the events tab! Probably obvious, we know.\n" +
        #                    ":small_blue_diamond: We host a weekly debate club - err… I mean, weekly discussion board, for all your hot takes, unpopular opinions, or general infodumps!\n" +
        #                    f"- Which you can find in <#{guildConfig['weekly_discussion_channel_id']}>! Come on in, share your thoughts, and enjoy the conversation!\n" +
        #                    ":small_blue_diamond: We got all the latest new release information and reviews for you to kick back and read!\n" +
        #                    f"- Check out <#{guildConfig['whats_new_channel_id']}> for all the latest and greatest! After you're done listening (or before, we won't judge) you can head on over to <#{guildConfig['reviews_channel_id']}> to see what other people are saying! Feel free to add to pre-existing threads and keep the conversation going!\n" +
        #                    "**Sounds great! How do I join?**\n" +
        #                    "We're happy to hear you say that! If you haven't already, be sure to familiarize yourself with our rules over in #welcome! When you come back, click that shiny verification button below and you're ready to go!")
        view_message = await ctx.send(view=welcome_view)

def setup(bot: commands.Bot):
    bot.add_cog(StartCog(bot))