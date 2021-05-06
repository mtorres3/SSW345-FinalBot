# SSW345 Final Report

## Problem

  Throughout our experience here at Stevens, we have definitely learned one thing: That time management is difficult. Whether it be trying to alot a good amount of time to complete a homework assignment or a final project, staying focused and productive isn't as easy as it may seem. To tackle this problem, our team has developed a Focus Bot for discord servers. With our bot, staying on task while still maintaining your productivity levels is a breeze. The features we have implemented assure that the user will have ample time to rest while still alotting a good chunk of time to getting a single task completed. This will keep the user focused and more likely to maintain their energy throughout the duration of their assignment.

## Features

The primary features we include in our bot are:
* Pomodoro Timer: To allow the user to maintain their productivity level throughout the duration of their assignment
* Create Task: To store future assignments into the database as a makeshift 'to-do' list
* Start Task: To start the pomodoro timer on a specific task
* Finish Task: To end the pomodoro timer and mark the task off of the 'to-do' list
* Show Task: Shows task currently being worked on
* Show schedule: Show all tasks added to the database from one server

Extra features include:
* Alarm: An alarm to alert the user of when its time for a break at the end of the pomodoro timer
* Pause/Stop: To end the alarm after you've returned from your 5 minute break (or alarm will automatically end after 5 seconds)
* Ping: To see user's ping on the server
* GetQuote: Displays an inspirational quote to the user
* Reminder: Sends user a reminder message 15 minutes before the task scheduled time
* Help: Show list of commands

## Reflection

The entire process of making the bot has been an enjoyable process. The group started out with a very simple idea and continued to tack on improvement after improvement. At the end of the sprints we ended up with a bot exceeding our expectations and leaving us hungry to continue its development.  
We utilized several organization and design methods which helped us throughout the whole process. Using Trello and Github Projects allowed us to delegate tasks amongst the team members. This meant that we had effective work distribution and were able to divide and conquer this beast of a bot. On top of that, we truly saw the benefits of github during this project. Additional applications such as Github Desktop made continuous development a breeze. Pushing, Fetching, Pulling, Commiting, Merging, etc. you name it, we learnt it and understand it after working on this project. Alongside these technologies we also dividied out development into two sprints, partly due to that being the requirement of the develpoment proess, and partly out of it being organic. When the team got together, out of sheer exctiement we grinding and came up with somethe begining stages of the bot. AFter a short break, we recouped our spirits and began the deveopment once again. This method of writing code in short interbals has allowed us to crack at certaain aspects of the project and make incremental progress on the whole! 
In terms of technicals, we really sharpened our python skills, which is a language some of the team has not touched in a while. On top of that we really solidified our understanding of API's. We made our bot for discord, and utilized discord.py often.  
>
> discord.py is a modern, easy to use, feature-rich, and async ready API wrapper for Discord.
>
We were exposed to API's from the start by nature of making a discord bot. 
On top of these, we also learnt some cool knowledge about machines and audio. We are able to play sound via a bot command. It was really interesting and fun learning how to download videos/audio and "compiling" that audio into something the computer can use. It is akin to a D/A converter where the binary representing the audio is converted into an analog signal such that it can oscillate a diaphram, thus producing sound on the user's machine! 


## Limitations and Future Plans

### Limitations
While FocusBot has met our expectations and has proved to be an invaluable asset for our groupwork, it is limited in a few aspects.
* First, FocusBot does not yet delete tasks from the database. 
* Second, FocusBot does not convert user time to UTC. The user must get the UTC via a bot command (which does an API call). 
* Third, FocusBot is not deployed! It does not have a remote environment configured for it yet.

But wait there's more! 

### Future Plans
Gregg's A-Team plans to continue development of FocusBot. As noted earlier, this bot has proven to be useful for our own separate projects. Some of the future tasks are:
* Get FocusBot to delete tasks properly from dB
* Get FocusBot to automatically get user timezone and convert to UTC so user does not need to input UTC time
* Get FocusBot deployed on a remote environment!

Aside from fixing the limitations, Gregg's A-Team hopes to find this bot being used around many different servers so that others can get use from it just as we have!

## [Link to Screencast](https://www.youtube.com/watch?v=VHnZ4IphOXo)
