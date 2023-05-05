import os
import asyncio
import discord
import requests
import json
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment variables (api_key)
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")

class DagothfyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.counter = 1
        self.lock = asyncio.Lock()

    @commands.command()
    async def dagothfy(self, ctx, *, message: str):
        # Make a request to the ElevenLabs API
        headers = {
            'accept': 'audio/mpeg',
            'xi-api-key': API_KEY,
            'Content-Type': 'application/json',
        }
        params = (
            ('optimize_streaming_latency', '0'),
        )
        data = {
            "text": message,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.75
            }
        }
        print(data)
       # Post request to ElevenLabs API 
        response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/7WaDHWbmBszduB93zwUm', headers=headers, params=params, data=json.dumps(data))

        if response.status_code == 200:
            # Save the resulting MP3 file
            with open(f'dagothfy_{self.counter}.mp3', "wb") as f:
                f.write(response.content)

            # Send the MP3 file as a reply to the requester
            await ctx.reply(file=discord.File(f'dagothfy_{self.counter}.mp3'))
        else:
            # Handle errors from the API
            await ctx.send(f"Error: {response.status_code} - {response.text}")

        # Increment the counter and reset to 1 after 10
        self.counter = (self.counter % 10) + 1

def setup(bot):
    bot.add_cog(DagothfyCog(bot))
