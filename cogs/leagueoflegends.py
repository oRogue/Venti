import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()
import libs.utils as utils

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class leagueoflegends(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    # Display LOL SEA Profile    
    @commands.slash_command(name = "profile", description = "Display summoner profile for SG region")
    async def profileSG(self, ctx, username: str):
        try:
            await ctx.defer()
            name = utils.clearNameSpaces(username)
            summoner = utils.getProfile("sg", name)
            summonerRanking = utils.getRanks("sg", summoner[3])
            embed = discord.Embed(title=summoner[0], description=summoner[1], color=0xFFD500)
            embed.set_thumbnail(url=summoner[2])
            
            # Solo/Duo
            try:
                tmp = f"{summonerRanking[1]} {summonerRanking[2]} • LP: {summonerRanking[3]} • Wins: {summonerRanking[4]} • Losses: {summonerRanking[5]}"
                embed.add_field(name="Ranked Solo/Duo", value=tmp, inline=False)
            except:
                embed.add_field(name="Not found", value="This player does not have any Ranked Solo/Duo stats.", inline=False)
            
            # Flex
            try:
                tmp = f"{summonerRanking[7]} {summonerRanking[8]} • LP: {summonerRanking[9]} • Wins: {summonerRanking[10]} • Losses: {summonerRanking[11]}"
                embed.add_field(name="Ranked Flex", value=tmp, inline=False)
            except:
                embed.add_field(name="Not found", value="This player does not have any Ranked Flex stats.", inline=False)
            
            await ctx.respond(embed=embed)
            print(f"[SYSTEM] {ctx.author.display_name} : /profile.")
        except:
            await ctx.respond(f"Sorry {ctx.author.mention} but I could not find that profile.")
        
def setup(bot):
    bot.add_cog(leagueoflegends(bot))