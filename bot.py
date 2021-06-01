import discord
import decouple

client = discord.Client()

@client.event
async def on_ready():
    print("online")

client.run(decouple.config('TOKEN'))
