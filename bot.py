import discord
import decouple
from discord.ext import commands

bot = commands.Bot(command_prefix="markov.")

@bot.event
async def on_ready():
    print("online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(decouple.config('TOKEN'))
