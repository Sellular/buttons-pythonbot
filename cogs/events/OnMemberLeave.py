import discord
from discord.ext import commands

from dao import LeftMemberRoleDAO

from datetime import datetime


class OnMemberLeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_leave(self, member: discord.Member):
        if member.roles:
            timestamp = datetime.utcnow()

            left_role_list = []
            for role in member.roles:
                left_role_list.append(
                    (str(member.id), str(role.id), str(timestamp)))

            try:
                LeftMemberRoleDAO.insertMany(left_role_list)
            except Exception as error:
                print(error)


def setup(bot):
    bot.add_cog(OnMemberLeaveCog(bot))
