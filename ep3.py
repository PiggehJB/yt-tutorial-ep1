import discord
from discord.ext import commands

token = "ODkzOTY4NzE4MDYzODc4MjM1.YVjLPw.kL-nmJSGmvm1NkCxb5CH2cqzbpQ"
prefix = "-"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"The bot is online!")

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(put your channel id integer here)
    print(f"{member} has joined!")
    await welcome_channel.send(f"{member.mention} has joined the server! Thank you")
    try:
        await member.send(f"Hey {member.display_name}! Thank you for joining the server")
    except:
        await welcome_channel.send(f"{member.mention} I can't dm you, but thank you for joining!")

@bot.event
async def on_member_remove(member):
    print(f"{member} has left!")
    leave_channel = bot.get_channel(put your channel id integer here)
    await leave_channel.send(f"{member.mention} has left the server :sob:")

    try:
        await member.send(f"Hey {member.display_name}! goodbye")
    except:
        await leave_channel.send(f"{member.mention} I can't dm you, but goodbye")
        
"""
on_member_ban
on_member_join
on_member_remove
on_member_unban
on_member_update
"""

bot.run(token)
