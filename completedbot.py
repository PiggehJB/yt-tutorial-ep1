import discord
from discord.colour import Color
from discord.ext import commands, tasks
from colorama import Fore
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
import os
# Your token

token = os.getenv('token')
prefix = "-"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!")
    pipreminder.start()

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, kick_member:discord.Member,*, reason=None):
    if kick_member == bot.user:
        await ctx.send("You can't kick me :angry:")

    elif kick_member.top_role >= ctx.author.top_role:
        await ctx.send("This person's role is higher or equal to yours!")

    else:
        await kick_member.kick(reason=reason)
        

@kick.error
async def kick_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("You don't have permissions to kick this member")

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        pass
    else:
        full = ctx.content
        if "pip" in full:
            await ctx.channel.send("If you're having any issues with pip, check out <#895483227244994641>")
        else:
            pass
        if ".gg" in full:
            await ctx.delete()
            await ctx.channel.send("Server invites aren't allowed here! {}".format(ctx.author.mention))
    await bot.process_commands(ctx)

counter = 0
@tasks.loop(hours=3)
async def pipreminder():
    global counter
    # ID = Whatever channel u want (this sends auto message into channel every 3 hours, but doesn't stack [No duplication])
    channel = bot.get_channel(894746091382272000)
    messages = await channel.history(limit=2).flatten()

    for msg in messages:
        if msg.author == bot.user:
            counter +=1
    if counter >= 1:
        print(f"{Fore.RED}Duplicate detected, ignoring new message request\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
        counter = 0
    else:
        await channel.send("If you're having any issues with pip, check out <#895483227244994641>\n`Automated Message`")
        print(f"{Fore.GREEN}Sent pip reminder to {Fore.MAGENTA}{channel}\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")

@bot.event
async def on_member_join(member):
    
    # Welcome message channel id
    wlc_channel = bot.get_channel(898420446125490186)
    
    # Role we want to add automatically
    wlc_role = "Member"
    role = discord.utils.get(member.guild.roles, name=wlc_role)
    await member.add_roles(role)

   
    embed = discord.Embed(title=f"Welcome {member.name}!", color = discord.colour.Color.from_rgb(255,192,203)).set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.add_field(name="Thank you for joining the server!", value=f"If you have any questions please check out <#895483227244994641> before asking in any support channels, also, please read\
    your code before asking, it saves ours and your time. If you're having an error with any code from a video, please ask in <#894746091382272000> -- Thank you :)", inline=True)
    embed.set_footer(icon_url=f"{member.guild.icon_url}", text=f"The server now has {member.guild.member_count} members!\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await wlc_channel.send(embed=embed)
    msg = await wlc_channel.send(f"{member.mention}")
    await msg.delete()

@bot.event
async def on_member_remove(member):
    # Leave message channel id
    wlc_channel = bot.get_channel(898420446125490186)
    embed = discord.Embed(title=f"{member.name} Left", color=Color.red()).set_author(name=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.add_field(name=f"Goodbye {member.name}", value="Goodbye! Sorry to see you go :sob:")
    embed.set_footer(icon_url=f"{member.guild.icon_url}", text=f"The server now has {member.guild.member_count} members!\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await wlc_channel.send(embed=embed)

bot.run(token)
