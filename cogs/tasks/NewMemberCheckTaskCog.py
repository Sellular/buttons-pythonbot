from discord.utils import get
from discord.ext import tasks, commands

from utils import GeneralUtils

from datetime import datetime, timedelta, timezone

class NewMemberCheckTaskCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.newMemberCheck.start()
    
    def cog_unload(self):
        self.newMemberCheck.cancel()

    @tasks.loop(hours=12)
    async def newMemberCheck(self):
        try:
            guildConfig = GeneralUtils.getConfig('guild')
            if not guildConfig:
                print("Guild config not found.")
                return

            guildId = guildConfig['guild_id']
            if not guildId:
                print("GUILD_ID not found in Guild config.")
                return
            
            roleId = guildConfig['new_member_role_id']
            if not roleId:
                print("NEW_MEMBER_ROLE_ID not found in Guild config.")
                return

            guild = get(self.bot.guilds, id = int(guildConfig['guild_id']))
            if not guild:
                print(f"Guild with id: {guildConfig['guild_id']} not found")
                return

            newMemberRole = get(guild.roles, id = int(guildConfig['new_member_role_id']))
            if not newMemberRole:
                print(f"Role with id: {guildConfig['new_member_role_id']} not found")
                return

            currentTimestamp = datetime.now(timezone.utc)
            for member in newMemberRole.members:
                compareTimestamp = member.joined_at + timedelta(weeks=1)
                if compareTimestamp <= currentTimestamp:
                    await member.remove_roles(newMemberRole)
        except Exception as error:
            print(error)

    @newMemberCheck.before_loop
    async def before_membercheck(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(NewMemberCheckTaskCog(bot))