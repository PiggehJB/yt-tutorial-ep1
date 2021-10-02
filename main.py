import discord
from discord.ext import commands

token = "ODkzOTY4NzE4MDYzODc4MjM1.YVjLPw.gC-rb7kmjb0ZT4uOkcWbyoemcCQ"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("The bot is online!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

bot.run(token)