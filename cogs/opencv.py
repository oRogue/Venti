import discord
from discord.ext import commands
import os
import dotenv
dotenv.load_dotenv()
import io
import libs.lib_opencv as openCVLib

ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT"))
GENERAL = int(os.getenv("GENERAL"))
MUSIC = int(os.getenv("MUSIC"))
TESTBENCH = int(os.getenv("TESTBENCH"))

class opencv(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    # Human face detector
    @commands.slash_command(name = "face", description = "debug")
    async def debug(self, ctx, image_url: str):
        try:
            await ctx.defer()
            img = openCVLib.faceDetection(image_url)
            with io.BytesIO(img) as file: 
                embed = discord.Embed(title="Here you go!",color=0x4a3d9a)
                file = discord.File(file , filename="image.png")
                embed.set_image(url="attachment://image.png")
                await ctx.respond(file=file, embed=embed)
                print(f"[SYSTEM] {ctx.author.display_name} : /debug.")
        except:
            await ctx.respond(f"Sorry {ctx.author.mention} please try with a direct link.")
        
def setup(bot):
    bot.add_cog(opencv(bot))