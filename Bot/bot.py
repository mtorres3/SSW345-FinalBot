# bot.py
import os
import random, time
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected')

@client.event
async def on_message(message):

    msg = message.content.lower()
    msg = msg.split()

    if message.author == client.user:
        return

    elif "!flip" in msg:
        await message.channel.send(random.choice(['Heads', 'Tails']))

client.run(TOKEN)
