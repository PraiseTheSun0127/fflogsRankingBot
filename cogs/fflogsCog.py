
from discord.ext import commands
import discord
from cogs.fflogsApi import getRanking,getZone

class FflogsCog(commands.Cog):

    def __init__(self, bot):
       
       self.bot = bot
       self.encountersList = None

    @commands.group()
    async def getRanking(self, ctx):

        if ctx.invoked_subcommand is None:
            
            await ctx.send('this command need sub command : zone & GN (guildName)')

    @getRanking.group()
    async def zone(self, ctx, zone):

        if zone is None:

            await ctx.send('The zone you specified was not found.')
        
        self.encountersList = getZone.getZone(zone)

        if self.encountersList is None:

            await ctx.send('The zone you specified was not found.')

    @zone.command()
    async def GN(self, ctx, guildName):

        result = getRanking.getRanking(self.encountersList,guildName)

        await ctx.send(f'```\n{result}\n```')

def setup(bot):
    
    bot.add_cog(FflogsCog(bot))