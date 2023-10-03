import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class interaction(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    # Venti dance gif
    @commands.slash_command(name = "dance", description = "Venti will bust a move.")
    async def danceGif(self, ctx):
        await ctx.defer()
        await ctx.respond(file=discord.File("assets/dance.gif"))
        author = ctx.author.display_name
        print(f"[SYSTEM] {author} : /dance.")
        
def setup(bot):
    bot.add_cog(interaction(bot))