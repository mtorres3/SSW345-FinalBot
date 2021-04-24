# Extranneous Imports
import os
import youtube_dl
from time import *
import asyncio

# Discord.py imports
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext import tasks
bot = commands.Bot(command_prefix = '_')

# Firestore DB imports
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
ref = db.collection('Servers')

# Testing DB connection
# for i in ref.stream():
#     print(i.to_dict()['user ids'])

@bot.event 
async def on_ready():
    print("Bot online")

@bot.command()
async def update_tasks(ctx):
    '''
    Should be used to grab tasks from database
    '''
    pass

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
async def startTask(ctx):
    global taskTimer
    taskTimer = True
    while(taskTimer == True):
        for i in range(1,6):
            sleep(25*60)
            await ctx.send('Break Time')
            await ctx.invoke(bot.get_command('alarm'))
            sleep(5*60)
            await ctx.send("Back to work")
            await ctx.invoke(bot.get_command('alarm'))

@bot.command()
async def finishTask(ctx):
    taskTimer = False
    #Mark task as complete in db
    await ctx.send("Task '{task}' completed!")

@bot.command()
async def showTask(ctx): #command name is function name
    #GET Task from database
    await ctx.send("(TASK NAME) is currently being executed") #Replace the send with task name once that is built 


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


'''
@tasks.loop(seconds=5.0, count=5)
async def slow_count():
    print(slow_count.current_loop)
'''

# @bot.command(pass_context = True)
# async def create(ctx, name, time):
#     current_task = Task(name, time)
#     db/pathreference.add(current_task)
#     await ctx.send(f'Task: {name} created.')


#jon
bot.run('ODMwNDYzNTM3MjkzNDI2Njk4.YHHDcA.0AS68ZQeQBbt1_pabVArWfqlrfc')

