import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment variables (token)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Define intents
intents = Intents.default()
intents.message_content = True

# Create a new bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Load the Crowder cog
bot.load_extension("dagothfy_cog")

# Run the bot
bot.run(TOKEN)
