import discord
from discord.ext import commands
# Your token
token = "Token here"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

intents = discord.Intents.all()
@bot.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!")
    
@bot.event
async def on_member_join(member):
  role_name = "Member" # Your role's name, in my case it's 'Member'
  role = discord.utils.get(member.guild.roles, name=role_name)
  await member.add_roles(role)
  print(f"Role added to {member}")
  
 bot.run(token)
