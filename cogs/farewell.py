import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class farewell(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.slash_command(name = "goodbye", description = "Give Venti a farewell!")
    async def hello(self, ctx):
        await ctx.respond(f"Bye bye {ctx.author.display_name}!")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.get_channel(ANNOUNCEMENT)
        embed = discord.Embed(color=0x4a3d9a)
        embed.add_field(name="**Goodbye!**", value=f"{member.name} has left {member.guild.name} 💔", inline=False)
        file = discord.File("assets/exit.gif", filename="exit.gif")
        embed.set_image(url="attachment://exit.gif")
        await channel.send(file=file, embed=embed)
        print(f"[SYSTEM] {member.name} left the server.")
        
def setup(bot):
    bot.add_cog(farewell(bot))