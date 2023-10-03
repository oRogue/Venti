import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class poll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    # Command
    @commands.slash_command(name = "poll", description = "Make a poll")
    
    async def poll(self, ctx, question, option1, option2, option3='', option4=''):
        member = ctx.author
        embed = discord.Embed(
        title=question, # Poll Question
        color=discord.Colour.brand_green(),
    )
        embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**") # put options here

        embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
        embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
        embed.add_field(name="Poll Creator", value=member.mention, inline=True)
    
        embed.set_author(name="Venti", icon_url="https://i.imgur.com/Rpe6rb3.jpg")
        embed.set_thumbnail(url=str(member.display_avatar.url))
    
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(poll(bot))