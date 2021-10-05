import discord
from discord.ext import commands, tasks
from colorama import Fore
# Your token
token = "ODkzOTY4NzE4MDYzODc4MjM1.YVjLPw.puNFh3WcyigmwSRaSWDQQkC9eYk"
prefix = "-"

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!")
    myloop.start()

index = 0
channel_ids = [channel ids here]

# your interval per loop
@tasks.loop(seconds=5)
async def myloop():
    global index
    while True:
        if index >= len(channel_ids):
            index = 0
            print(f"{Fore.YELLOW}Done sending messages, repeating in 5 seconds...")
            break
        output_channel = bot.get_channel(channel_ids[index])
        try:
            await output_channel.send("Automated message")
            print(f"{Fore.BLUE}Sent a message to {output_channel}")
        except:
            print(f"{Fore.RED}Couldn't send message to the channel")
        index+=1

bot.run(token)
