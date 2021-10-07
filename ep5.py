import discord
from discord.colour import Colour
from discord.ext import commands
# This is optional
from colorama import Fore
# Your token
token = "ODkzOTY4NzE4MDYzODc4MjM1.YVjLPw.ME6NZRCqpscQcSGGpFBio6W5xXs"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    # If you don't want to use colorama, remove{Fore.GREEN}
    print(f"{Fore.GREEN}The bot is online!")

@bot.event
async def on_message(ctx):
    # So our bot doesn't reply to itself

    if ctx.author.id == bot.user.id:
        return

    if ctx.channel.id == 895474683120615434:
        # Defining variables
        author = ctx.author.name
        message = ctx.content
        channel = ctx.channel.id
        logging_channel = bot.get_channel(895476136287567934)
        # Make embed
        logging_embed = discord.Embed(title=f"{author}'s Message", color = Colour.blurple()).set_author(name=f"{bot.user.display_name}", icon_url=f"{bot.user.avatar_url}")
        logging_embed.add_field(name=f"Message detected!", value=f"Found in <#{channel}>\n\nMessage is: \n{message}").set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Sent by {author}")
        await logging_channel.send(embed=logging_embed)
        # Allows bot to use @bot.command() commands along with on_message event
        await bot.process_commands(ctx)

bot.run(token)
