import discord
from discord.ext import commands

from views import WelcomeView

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def welcome(self, ctx):
        view = WelcomeView()
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

async def setup(bot: commands.Bot):
    await bot.add_cog(WelcomeCog(bot))