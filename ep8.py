# Tutorial here: https://www.youtube.com/watch?v=qwz5pSgFhrE

import discord
from discord.ext import commands

token = "token here"
prefix = "-"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Add roles
@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "🔴" and payload.message_id == Message ID here (not in ""):
        role = discord.utils.get(guild.roles, name="Role name here")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
# Remove roles
@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == "🔴" and payload.message_id == Message ID here (not in ''):
        role = discord.utils.get(guild.roles, name="Red")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

# Sends message with reaction
@bot.command()
async def react(ctx):
    message = "React to this message to get the red role!"
    react_messasge = await ctx.send(message)
    await react_messasge.add_reaction(emoji="🔴")

bot.run(token)
