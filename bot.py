import discord
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print("online")

client.run(config('TOKEN'))
