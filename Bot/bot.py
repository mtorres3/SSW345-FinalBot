# Extranneous Imports
import os
import youtube_dl
from time import *
import asyncio
from Task import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Discord.py imports
import discord
from discord.ext import commands, tasks
from discord.utils import get
bot = commands.Bot(command_prefix = '_')
client = discord.Client()
global GUILD_ID, GUILD_NAME, tasks, task_name
GUILD_NAME, GUILD_ID = "", ""

# Documentation on getting certain info
# Keep in mind ctx is not created until called
# See info function to see in action
'''
Server Name = ctx.guild.name
Server ID = ctx.guild.id
Channel name bot called in = ctx.channel.name
Channel ID bot called in = ctx.channel.id
ID of user = ctx.author
Voice channel ID of user = ctx.author.voice.channel.name
'''

# Firestore DB imports
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
ref = db.collection('Servers')

# Testing DB connection
'''
for i in ref.stream():
    print(i.to_dict()['user ids'])
'''

# Start of functions
def get_tasks(ctx, name=None):
        
# Tests successful connection to server
tasks = {}
@bot.event 
async def on_ready():
    #tasks = get_tasks()
    print("Bot online")
    for server in ref.stream():
        print(server.to_dict())
    await bot.get_channel(818916814167081030).send('notif')

@bot.command()
async def createTask(ctx, name = None, day = None, time = None, m = None):
    if name == None or day == None or time == None or m == None:
        await ctx.send('''
**Hello!** What you said raised on error.
You should format it like this:
*_createTask   "Jon's Birthday"   2000/01/10   5:13   am*
''')

    else:
        ref.document(ctx.guild.name).set({
            'Server ID' : ctx.guild.id,
            'Server Name' : ctx.guild.name
        })
        ref.document(ctx.guild.name).collection('Tasks').document(name).set(
        {
            'Channel ID': ctx.channel.id,
            'Channel Name': ctx.channel.name,
            'User ID': ctx.author.id,
            'User Name': ctx.author.name,
            'Task Name': name,
            'Completed': "No",
            'Date': {
                'Day': day,
                'Time': time,
                'AM/PM': m
            }
        })
        await ctx.send("Task: {} added :)".format(name))
    # await bot.get_channel(818916814167081030).send('hello from the other channel!')

@bot.command(pass_context = True)
async def join(ctx):
    global voice
    channel =  ctx.message.author.voice.channel #get Vchannel of the one who called balled
    voice =  get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"Joined {channel}")

@bot.command(pass_context = True)
async def leave(ctx):
    global voice
    channel =  ctx.message.author.voice.channel #get Vchannel of the one who called balled
    voice =  get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left {channel}")
    else:
        await ctx.send(f"Bot not in {channel}")

#this function works by downloading the youtube video with url provided using youtube_dl dependency
#this is then converted with FFmpeg dependency so it is in format that can be played
#this is played by saving the converted audio as "song.mp3" and then playing 
#if a .mp3 already exists it means that a song is playing, otherwise it would be deleted and remade for next audio
@bot.command(pass_context = True)
async def alarm(ctx):  #can do use input as well, input url: str as input and remove hard coded url
    #if url is None:
    url = 'https://www.youtube.com/watch?v=LzxCJzM4xLo'
    
    global voice
    voice =  get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")

        except PermissionError:
            await ctx.send("Wait for current audio to end!")
            return
        await ctx.send("Getting audio file...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            await ctx.send("Downloading audio...")
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        await ctx.send("Done converting, now playing!")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    else:
        await ctx.send(f"Bot not in a channel")

@bot.command(pass_context = True)
async def stop(ctx):
    voice =  get(bot.voice_clients, guild = ctx.guild)
    if voice is not None:
        voice.stop()
    else:
        await ctx.send("No audio playing")

@bot.command(pass_context = True)
async def pause(ctx):
    voice =  get(bot.voice_clients, guild = ctx.guild)
    if voice is not None:
        voice.pause()
    else:
        await ctx.send("No audio playing")

@bot.command()
async def ping(ctx): #command name is function name 
    await ctx.send(f'Latency: {round(bot.latency * 1000)}ms')

@bot.command()
async def startTask(ctx, name = None, num = 1):
    global task_name
    if name == None:
        task_name = None
        await ctx.send('''
**Hello!** What you said raised on error.
You should format it like this:
*_startTask  "Essay for CAL105" 4(30-min cycles) *
''')

    else:
        task_name = get_tasks(name)
        await ctx.send("Starting ", task, ' For ', num/2, ' Hours')

        try:
            asyncio.ensure_future(pomodoro(num))
        except ctx.invoke(bot.get_command('finishTask')):
            task_name.Completed = 'Yes'
            await ctx.send("Task ", name, " completed.")

async def pomodoro(ctx, num = 1):
    #Loop thru pomodoro timer 6 times
    for i in range(1, num):
        await asyncio.sleep(5)
        await ctx.send('Break Time')
        await ctx.invoke(bot.get_command('alarm'))
        await asyncio.sleep(1)
        await ctx.send("Back to work")
        await ctx.invoke(bot.get_command('alarm'))

@bot.command()
async def finishTask(ctx):
    return True
    

@bot.command()
async def showTask(ctx): #command name is function name
    global task_name
    if task_name=None:
        await ctx.send("There is no task being done right now")
    else: 
        await ctx.send("Task In Progress: "+task_name)

#here is how to invoke command from command
@bot.command()
async def invoketest(ctx):
    await ctx.send("Invoking _alarm command")
    await ctx.invoke(bot.get_command('alarm'))

@bot.command()
async def test1(ctx):
    await ctx.send("test1")
    await asyncio.sleep(5)
    await ctx.send("test1")

@bot.command()
async def test2(ctx):
    await ctx.send("test2")
    await asyncio.sleep(5)
    await ctx.send("test2")

@bot.command()
async def info(ctx):
    await ctx.send("Server Name: " + str(ctx.guild.name))
    await ctx.send("Server ID: " + str(ctx.guild.id))
    await ctx.send("Channel Name: " + str(ctx.channel.name))
    await ctx.send("Channel ID: " + str(ctx.channel.id))
    await ctx.send("User ID: " + str(ctx.author))
    await ctx.send("Voice ID: " + str(ctx.author.voice.channel.name))  


'''
@tasks.loop(seconds=5.0, count=5)
async def slow_count():
    print(slow_count.current_loop)
'''

bot.run(TOKEN)