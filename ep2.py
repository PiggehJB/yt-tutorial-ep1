import discord
from discord.colour import Colour
from discord.ext import commands
token = "ODkzOTY4NzE4MDYzODc4MjM1.YVjLPw.PGo_-SRsC7F1P0DnuuGzCSHTQoE"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f"The bot is online!")

@bot.command()
async def embed(ctx, channel:discord.TextChannel, user:discord.Member):
    my_fav_color = discord.colour.Color.from_rgb(255, 255, 255)
    myembed = discord.Embed(title="My Title!", color = my_fav_color).set_author(name="Tutorial bot")
    myembed.add_field(name="Heading", value="my small value text", inline=True)
    myembed.add_field(name="Heading 2", value="My second small text value", inline=True)
    myembed.set_footer(text=f"Sent by {user.display_name}")
    await channel.send(embed=myembed)
    await user.send(embed=myembed)


bot.run(token)
