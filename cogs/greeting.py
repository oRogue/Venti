import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class greeting(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    # Command
    @commands.slash_command(name = "hello", description = "Give Venti a greeting!")
    async def hello(self, ctx):
        await ctx.respond(f"Hello {ctx.author.display_name}!")
        
    # Event
    @commands.Cog.listener() #  @bot.event
    async def on_member_join(self, member):
        channel = member.guild.get_channel(ANNOUNCEMENT)
        embed = discord.Embed(color=0x4a3d9a)
        embed.add_field(name="**Welcome!**", value=f"{member.name} has joined {member.guild.name} ❤️", inline=False)
        file = discord.File("assets/introduction.gif", filename="introduction.gif")
        embed.set_image(url="attachment://introduction.gif")
        await channel.send(file=file, embed=embed)
        print(f"[SYSTEM] {member.name} joined the server.")
        
def setup(bot):
    bot.add_cog(greeting(bot))