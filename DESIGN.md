**[Problem Statement]:**

WHY: The problem is that teams often collaborate and communicate via discord channels yet fail to effectively schedule and attend meetings. There is no centralized scheduler/alert bot for that server. This means there exists a failure vector whereby a teammate may forget about a meeting, or set an alert for the wrong time, particularly for those in a different time zone. Without the ability to offset recurring tasks to a bot, there is always a chance for human error, which could hamper an entire groups project for an unknown amount of time. 

WHAT: A problem immediately surfaces for any collaborative effort on discord. Teammates do not have the ability to create a universal event on the platform they are in. On top of that, teammates are unable to have automated reminders sent. There is also no way to create recurring meetings, something that becomes a greater problem the longer the time period for those recurring meetings is.


**[Bot Description]:**

Our Focus Bot is used to keep users in a Discord server on task about projects or obligations. Focus Bot will allow for easier organization amongst users who have multiple things on their schedules, such as meetings or deadlines. This bot comes from our group’s specific needs, as we often work together on multiple projects across multiple classes. Keeping up with all these assignments is often difficult to just remember off the top of your head, or to remain on task. What better way to solve this issue than to have a bot create reminders for you? 
Focus Bot will be able to have a “conversation” with users by sending them messages based off previously passed arguments which could include the name, time, and date of the task at hand. Once loaded onto the server, the users will be prompted to choose a time-zone so that scheduling for Focus Bot will become more effective, instead of basing it off the server-side time-zone. From there, users will then be able to set up reminders for tasks, deadlines, or reoccurring meetings. Focus Bot will then send a message at that specified time and tag all users. Once a task has started, Focus Bot will send a reminder every 25 minutes for task workers to take a break, then to get back on task 5 minutes later. If we had to describe our bot in one tagline, it would be **FOCUS**.


**[Use Case]: Scheduling a event**

  Preconditions - Must have the discord bot added to a server.
  
  Main Flow - User will enter a command to open their schedule and create a task (S1). Bot will display open time slots for the next week (S2). The user will
  specify a task name, time, and day (S3). Bot will display the created task (S4).
  
  Subflow -
  (S1): User provides a /create command
  (S2): Bot displays schedule availability in a '<day>: <hours available>' format
  (S3): User enters data in a '<task name>, <day>, <time>' format
  (S4): Bot will display '<task name> created for <day> at <time>!'
  
  Alternative Flow - 
  (E1): User enters a time where there is a task conflict.

**[Use Case 2]: Start a task**

  Preconditions - Must have the discord bot added to a server.
  
  Main Flow - User will enter a bot command to inform the bot that they're starting a task (S1). After 25 minutes, the bot will notify the user to take a break
  (S2). After another 5 minutes, the bot will notify the user to return to the task (S3). This cycle repeats until the user enters the command to finish their task
  (S4).
  
  Subflow -
  (S1): User will enter /starttask to begin
  (S2): Bot will send a 'Time to take a break!' message after 25 min
  (S3): Bot will send a 'Time to get back to work!' message after another 5 min
  (S4): Cycle continues until user enters /finishtask
  
  Alternative Flow -
  (E1): User doesn't end task (ends after 6 hours)


**[Design Sketches]:**



**[Architecture Design]:**

<img width="771" alt="SSW345 Design Milestone" src="https://user-images.githubusercontent.com/54967638/112692499-6dc62a80-8e55-11eb-9c39-0db35933e37f.png">

*Component Descriptions:*

- **Reminders:** Users and groups will be able to set to settings for reminders to happen automatically or custom specific to a certain time. These reminders will also be modular with text, data, references, etc.
- **Project Management:** Projects will be able to be fully managed through the bot. Groups will be able to be formed and along with that, the creation of calendars and task management will also be features. For example, one specific feature will allow users to sign up for tasks and the bot will update the entire group when said task is completed. User stories will also be able to be formed with the bot.
- **Productivity Aids:**  Productivity Aids such as the Pomodoro Technique will be featured with the bot. The bot will also have methodologies such as Lean and Agile built into it to allow for modification for projects and assignments submitted with the bot.

