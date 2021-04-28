# SSW345- FocusBot Version: 1.0.1  

Jonathan Cucci: *joncucci*
- User Story: /createTask

William Baltus: *WilliamBaltus*
- User Story: /StartTask

Joseph Letizia: *josephletizia*
- User Story: /ShowTask

Markell Torres: *mtorres3*
- User Story: /FinishTask'


## Instructions for Running:

1. IDE: User choice  
2. Language: Python3.X  
3. Package manager: pip (install if you don't have it already)

### Crucial Dependencies and Packages to download/install:

1. Youtube_dl: this downloads a youtube video if provided a url
2. Discord.py Voice: voice commands for discord bot, does not install by default
3. FFMpeg: this converts a video into a format that discord can understand, think of it as an audio file compiler

#### Youtube_dl  
You can use a package manager, such as pip to get this. Simply run this command to install:
> pip install youtube_dl  
> pip install --upgrade youtube-dl  
You can learn more about it [Here](https://pypi.org/project/youtube_dl/)    

#### Discord.py Voice  
You can use a package manager, such as pip to get this. Simply run this command to install:
> pip install -U discord.py[voice]  

#### FFMpeg 
This is more complicated to install properly. Here are the steps I took. There are many different ways to do this FYI. 
1. The link to downlod ffmpeg is [Here](https://www.gyan.dev/ffmpeg/builds/)
2. When you arrive at the page, you will scroll down and see something like this. Download and install the 7-zip Utility, shown below.
  ![FFMpeg home page](7zip-ffmpeg.PNG)  
3. Scroll down some more until you find this:  
  ![FFMpeg full download link](full-ffmpeg.PNG)  
4. Open the 7zip utility and open the ffmpeg folder you downloaded, it should look similar to this:
  ![7zip-open download](7zip-open.PNG)
5. Open the folder and find the bin subfolder. 
6. Open the bin folder, there you will find a few .exe files. Those are the ffmpeg binaries. Drag this 7zip window to the side. 
7. Create a new folder in your drive. I created them in my C Drive. It is best to name the folder something easy as it will help you down the line. In my case, I named it "FFMPEg"
8. Now you want to select the .exe files in the 7zip and copy them over to the folder you made in the C drive. It may look similar to this:
  ![7zip .exe to C drive](copy-ffmpeg.PNG)
 

