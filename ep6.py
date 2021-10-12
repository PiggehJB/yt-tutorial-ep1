import discord
from discord.ext import commands
from colorama import Fore
from discord.ext.commands import has_permissions, MissingPermissions

# Your token
token = "ODk3NjAwNjAxNzY3MTYxODg2.YWYBtA.EFOjb3LP0ywm517OGtYxN2exPKY"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!")

# -kick @member (optional) reason

@bot.command()
@has_permissions(kick_members=True)
async def kick(message, kick_member:discord.Member,*, reason=None):
    if kick_member == bot.user:
        await message.send("You can't kick me :angry:")

    elif kick_member.top_role >= message.author.top_role:
        await message.send("This person's role is higher or equal to yours!")

    else:
        await kick_member.kick(reason=reason)
        

@kick.error
async def kick_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("You don't have permissions to kick this member")

bot.run(token)
