import discord
import decouple
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="markov.")

@bot.event
async def on_ready():
    print("online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def gen(ctx):
    pdict = {}

    parsed = [i.split() for i in open("raw.txt","r",errors="ignore").read().split("\n\n")]

    for l in parsed:
        for i,j in zip(l,l[1:]):
            if i in pdict:
                pdict[i] = pdict[i] + [j]
            else:
                pdict[i] = [j]

    out = ""

    e = random.choice(list(pdict.keys()))

    while e in pdict.keys():
        out += e + " "
        e = random.choice(pdict[e])

    out += e

    await ctx.send(out[:2000])

bot.run(decouple.config('TOKEN'))
