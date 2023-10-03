# Libraries
import discord
import os
import dotenv
dotenv.load_dotenv() # Loads .env file
import wavelink

# .env keys
TOKEN = str(os.getenv("TOKEN")) # API Token
ANNOUNCEMENT = int(os.getenv("ANNOUNCEMENT")) # Channel ID
GENERAL = int(os.getenv("GENERAL")) # Channel ID
MUSIC = int(os.getenv("MUSIC")) # Channel ID
TESTBENCH = int(os.getenv("TESTBENCH")) # Test channel on personal server
RIOT = str(os.getenv("RIOT")) # Riot API key

# Bot Initialization
bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Blowing the winds~")) # Bot Profile
    print("[SYSTEM] Bot has logged in as {0.user}".format(bot))
    bot.loop.create_task(connect_nodes())

    
# async def connect_nodes():
#     await bot.wait_until_ready()
#     await wavelink.NodePool.create_node(
#         bot=bot,
#         host='lava1.horizxon.studio',
#         port=80,
#         password='horizxon.studio',
#         # https=True
#     )
    
async def connect_nodes():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(
        bot=bot,
        host='54.38.198.24',
        port='88',
        password='stonemusicgay',
        # https=True
    )
    
@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"[SYSTEM] Node {node.identifier} is ready")

# Intializing & Loading cogs
initial_extensions= []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN)