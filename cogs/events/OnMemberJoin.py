import discord
from discord.ext import commands

from dao import LeftMemberRoleDAO


class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        leftMemberRoles = None
        try:
            leftMemberRoles = LeftMemberRoleDAO.getLeftMemberRolesByMember(str(member.id))
            LeftMemberRoleDAO.deleteLeftMemberRolesByMember(str(member.id))
        except Exception as error:
            print(error)

        if leftMemberRoles:
            guild = member.guild

            for role in leftMemberRoles:
                guild_role = discord.utils.get(guild.roles, id=int(role.roleID))
                member.add_roles(guild_role)


def setup(bot):
    bot.add_cog(OnMemberJoin(bot))