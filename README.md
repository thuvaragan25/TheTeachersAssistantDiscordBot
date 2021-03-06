# Tabby - The Teacher's Assistant Discord Bot

## Purpose
Remote learning has been a struggle for all students, with technology growing it seems as if remote learning won't end after the pandemic. Discord is an emerging platform, where users can interact with their peers and is used in many extracurriculars at school. This bot was made on this platform to be a study buddy to students and to aid teachers. 

## What it does
Using the `.commands` command on the bot, can allow the user to see in detail what commands are currently available on the bot and what each command does. Furthermore, this bot can filter inappropriate words from the chat and deletes them immediately before anyone sees them. Also, commands can be run by direct messaging the bot the specific command which is helpful for privacy. The only case that this may not work is for the music commands as a voice channel on a server is required, the text to speech command as there is a specific channel designated for text to speech, and the attendance command as it is used to check the attendance of a large group of people. 

## How the bot was built
The Python programming language and the [discord.py](https://discordpy.readthedocs.io/en/stable/api.html) module was used to build this bot. Some of the commands were built using the help of these APIs: https://newsapi.org/, https://api.adviceslip.com/advice, https://dictionaryapi.dev/. To sensor inappropriate words, the dataset was obtained from: https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/. Music for the discord bot is No Copyright music. The lofi music is from the producer Lofi Geek, taken from [here](https://www.youtube.com/watch?v=4Ta1a5VAYLg). The classical music was taken from [here](https://www.youtube.com/watch?v=bvlNy_GxVe0&t). 

## Demo
Check out the demonstration and see Tabby in action [here](https://youtu.be/MpBPUOQRiP0).

## Try it out
If you'd like to add this bot to your server, visit: [here](https://discord.com/api/oauth2/authorize?client_id=867085688638144522&permissions=8&scope=bot). Follow the instructions, and the bot should successfully be added to your server. 

### Note
If you would like to use the attendance feature or the text to speech you would have to provide the channel id/voice channel id where it says so in the comments for [main.py](https://github.com/thuvaragan25/TheTeachersAssistantDiscordBot/blob/main/main.py). This means you would have to create your own bot, and get the API tokens where the comments ask for in [main.py](https://github.com/thuvaragan25/TheTeachersAssistantDiscordBot/blob/main/main.py). Only this part of the code has to be modified which makes adding this bot to your server convenient. These commands will not be available for the bot that is up and running currently as all channels have different ids. To find channel ids check out this [tutorial](https://www.youtube.com/watch?v=GuO4TswMZho), to set up your discord bot use this [tutorial](https://www.youtube.com/watch?v=Uibz0iQjoC0). All other commands for my bot will be available on the bot that is currently up and running.