import discord
from discord.ext import commands
import requests
import json
import random
from discord import Embed
import urllib
import urllib.request
from discord import FFmpegPCMAudio

bot = commands.Bot(command_prefix = ".")
news_api_key = "" #Get your API key from https://newsapi.org/ 
discord_token = "" #Put your discord bot token here
tts_channel = "" #put the channel ID of your text to speech channel in order to hear text to speech messages
voice_channel = "" #put the channel ID of your voice channel in order to take attendance

tts = False
badwords = []
with open("full-list-of-bad-words_text-file_2021_01_18.txt", "r") as f:
  badwords = f.read().splitlines()

@bot.event
async def on_ready():
  print("Bot is ready.")
@bot.event
async def on_message(message):
  global tts
  if message.author == bot.user:
    return
  for word in message.content.lower().split(' ')[:]:
    if word in badwords:
      await message.delete()
  
  if message.content.startswith('.stress'):
    embed = discord.Embed(title = "Breathe in...and breathe out...", description = "", color = discord.Colour.green())
    embed.add_field(name="How to relieve stress:", value = " 1. Try some deep breathing exercises: https://www.youtube.com/watch?v=acUZdGd_3Dg \n\n 2. Meditate: https://www.youtube.com/watch?v=x0nZ1ZLephQ \n\n 3. Yoga/Exercise/Go on a walk or run \n\n 5. Relax to some music \n\n 6. Counseling: 1-800-668-6868", inline=False )
    gif = ["https://media.giphy.com/media/xWC0BCZtkDxE869erD/giphy.gif", "https://media.giphy.com/media/Y3yBSFNb0n1Xa/giphy.gif", "https://media.giphy.com/media/hL8a3mIQK8Ehy/giphy.gif", "https://media.giphy.com/media/2WiiB5KgivGrlstYcl/giphy.gif", "https://media.giphy.com/media/13tB0WgrJvp5DO/giphy.gif", "https://media.giphy.com/media/KDteAGZcv7LiehlTDm/giphy.gif", "https://media.giphy.com/media/LLYMoDblVhhjvjRBtj/giphy.gif", "https://media.giphy.com/media/S9EwIrpnSlG9LIitP2/giphy.gif"  ]
    rand = random.randint(0, len(gif)-1)
    embed.set_image(url=gif[rand])
    await message.channel.send(embed=embed)
  
  elif message.content.startswith('.commands'):
    embed = discord.Embed(title = "List of Commands For the Bot", description = "", color = discord.Colour.purple())
    embed.set_thumbnail(url="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ivPyAVC2O7As/v1/1000x-1.jpg")
    embed.set_author(name="Teacher's Assistant", icon_url = "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ivPyAVC2O7As/v1/1000x-1.jpg")
    embed.add_field(name = ".stress", value = "Posts a relaxing gif, and tips to relieve stress", inline = True)
    embed.add_field(name = ".studytips", value = "Gives the user tips for studying", inline = True)
    embed.add_field(name = ".music", value = "Displays all the music commands", inline = True)
    embed.add_field(name = ".research", value = "Please enter `.research <query>` to research about any topics", inline = True)    
    embed.add_field(name = ".advice", value = "Gives you random advice, type the command again for another piece of advice ", inline = True)
    embed.add_field(name = ".hotlines", value = "Gives user a list of hotlines they can reach out to", inline = True)
    embed.add_field(name = ".define", value = "Please enter `.define <query>` to look up what any word means", inline = True)
    embed.add_field(name = ".speech", value = "Turns on and off text to speech in the text to speech channel", inline = True)
    embed.add_field(name = ".attendance", value = "To record the attendance of the people in the specific voice channel", inline = True)
    embed.add_field(name = ".members", value = "Prints all the members recorded from the `.attendance` command", inline = True)
    await message.channel.send(embed=embed)

  elif message.content.startswith('.studytips'):
    embed = discord.Embed(title = "Resources", description = "Useful resources to help you study!", color = discord.Colour.blue())
    embed.set_footer(text="Studying efficently is the way to go!")
    embed.add_field(name="How to study more efficently:", value = "``` 1. Stay healthy (grab a snack and stay hydrated)\n\n 2. Plan your day, whether that is making a schedule or having goals for yourself.\n\n 3. Remember to take breaks, maybe after every hour of studying take a 20 minute break.```", inline=False )
    embed.add_field(name="Cool Links", value = "Teachers don't want students to know this: https://www.youtube.com/watch?v=wVc_ilWtA6g", inline=False )
    embed.set_image(url="https://media.giphy.com/media/qdnMr2j2anHsLTv5TO/giphy.gif")
    await message.channel.send(embed=embed)

  elif message.content.startswith('.hotlines'):
    embed = discord.Embed(title = "Hotlines", description = "Here are some useful resources, we hope you are okay!", color = discord.Colour.red())
    embed.add_field(name="Contact", value = "`Kids Help Phone:` https://kidshelpphone.ca/\n`Canada Suicide Prevention Service:` https://www.crisisservicescanada.ca/en/", inline=False )
    embed.set_image(url="https://i.pinimg.com/originals/b2/42/04/b242041d60ee8fe7f94fd592fd24f0ee.gif")
    await message.channel.send(embed=embed)
  
  elif message.content.startswith('.research'):
    try:
      query = ""
      user_input = message.content.split(' ')[1:]
      for word in user_input:
        query += word+"-"
      query = query[:-1]
      response = requests.get(f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=popularity&apiKey={news_api_key}").text
      json_data = json.loads(response)
      if json_data["status"] != "ok":
        await message.channel.send("Cannot find any results")
      
      title = f"You searched: {query.capitalize()}."
      article = random.choice(json_data["articles"])
      embed = discord.Embed(title = title.replace('-', ' '), description = "To get another link, use the `.research` command with the same query", color = discord.Colour.red())
      embed.add_field(name="Article Title", value = (f"```{article['title']}```"), inline=False )
      embed.add_field(name="Description", value = (f"```{article['description']}```"), inline=False )
      embed.add_field(name="Author", value = (f"```{article['author']}```"), inline=False )
      embed.add_field(name="Date Published", value = (f"```{article['publishedAt'][:10]}```"), inline=False )
      embed.add_field(name="Link", value = (f"<{article['url']}>"), inline=False )
      embed.set_image(url=article["urlToImage"])
      embed.set_footer(text="Now do your citations with ease :)")
      await message.channel.send(embed=embed)
    except:
      await message.channel.send(f"Please enter `.research <query>`")
  
  elif message.content.startswith('.advice'):
    req = requests.get("https://api.adviceslip.com/advice")
    data = json.loads(req.text)
    await message.channel.send(data["slip"]["advice"])

  elif message.content.startswith('.define'):
    overall_word = ""

    user_input = message.content.split(' ')[1:]
    for word in user_input:
      overall_word += word+" "
    overall_word = overall_word[:-1]
    req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}")
    data = json.loads(req.text)    
    try:
      embed = discord.Embed(title = "Dictionary", description = f"The word you want to define is **{word}**.", color = discord.Colour.gold())
      embed.add_field(name="Definition", value = (f'```{data[0]["meanings"][0]["definitions"][0]["definition"]}```'), inline=False )
      embed.add_field(name="Phonetics", value = (f'```{data[0]["phonetics"][0]["text"]}```'), inline=False )
      embed.add_field(name="Pronunciation", value = (f'{data[0]["phonetics"][0]["audio"]}'), inline=False )
      embed.add_field(name="Part of Speech", value = (f'```{data[0]["meanings"][0]["partOfSpeech"]}```'), inline=False )
      try:
        embed.add_field(name="Example", value = (f'```{data[0]["meanings"][0]["definitions"][0]["example"]}```'), inline=False )
      except:
        example = "No Examples Available"
        embed.add_field(name="Example", value = (f'```{example}```'), inline=False )
      synonyms = ""
      try:
        for synonym in data[0]["meanings"][0]["definitions"][0]["synonyms"]:
          synonyms += synonym + ', '
        synonyms = synonyms[:-2]
      except:
        synonyms = "No Synonyms Available"
      embed.add_field(name="Synonyms", value = (f'```{synonyms}```'), inline=False )
      await message.channel.send(embed=embed)
    except:
      await message.channel.send(f"No definitions found for the word **{word}**")

  elif (message.content.startswith('.join')):
          if (message.author.voice): 
              channel = message.author.voice.channel
              await channel.connect()
              await message.channel.send('Bot joined')
          else: 
              await message.channel.send("You must be in a voice channel first so I can join it.")

  elif message.content.startswith('.leave'): 
        if (message.guild.voice_client): 
            await message.guild.voice_client.disconnect() 
            await message.channel.send('Bot left')
        else: 
            await message.channel.send("I'm not in a voice channel, use the join command to make me join")

  elif message.content.startswith('.pause'):
    voice = discord.utils.get(bot.voice_clients, guild=message.guild)
    if voice.is_playing():
      voice.pause()
    else:
      await message.channel.send("At the moment, there is no audio playing in the voice channel!")

  elif message.content.startswith('.resume'):
    voice = discord.utils.get(bot.voice_clients, guild=message.guild)
    if voice.is_paused():
      voice.resume()
    else:
      await message.channel.send("At the moment, there is no audio paused in the voice channel!")

  elif message.content.startswith('.stop'):
    voice = discord.utils.get(bot.voice_clients, guild=message.guild)
    voice.stop()

  elif message.content.startswith('.play'):
    try:
      voice = message.guild.voice_client
      overall_word = ""
      user_input = message.content.split(' ')[1:]
      for word in user_input:
        overall_word += word+" "
      overall_word = overall_word[:-1]
      source = FFmpegPCMAudio("./music/" + word + ".mp3")
      player = voice.play(source)
    except:
      await message.channel.send("Encountered an error. Ensure that you or I are in a voice channel, and there is not any audio currently playing. If that is not the case, pause/stop the song to play a different song.")

  elif message.content.startswith('.music'):
    embed = discord.Embed(title = "Music Commands", description = "", color = discord.Colour.orange())
    embed.set_thumbnail(url="https://scx2.b-cdn.net/gfx/news/2016/578650fe544c4.jpg")
    embed.set_author(name="Teacher's Assistant Music Player", icon_url = "https://i0.hippopx.com/photos/706/372/896/microphone-sound-music-preview.jpg")
    embed.add_field(name = ".join", value = "Joins a voice channel", inline = True)
    embed.add_field(name = ".leave", value = "Leaves a voice channel", inline = True)
    embed.add_field(name = ".pause", value = "Pauses song", inline = True)
    embed.add_field(name = ".resume", value = "Resumes song", inline = True)
    embed.add_field(name = ".play `song`", value = "Plays a song, currently there is lofi and classical music available.", inline = True)
    embed.add_field(name = ".stop", value = "Stops a song", inline = True)
    await message.channel.send(embed=embed)

  elif message.content.startswith(".attendance"):
      vc = bot.get_channel(int(voice_channel)) 
      attend = vc.members
      with open("attendees.txt", 'w') as file:
        for member in attend:
          file.write(member.name + '\n')

  elif message.content.startswith(".members"):
    with open("attendees.txt") as f:
      content = "".join(f.readlines())
    await message.channel.send("**Current members of this channel are:**\n" + content)
  
  elif message.content.startswith('.speech'): 
    tts = not tts

  elif message.content.startswith('.'): 
    text = ("Sorry I cannot understand. Please use the `.commands` feature to view all the available features on the bot.")
    await message.channel.send(text)
  
  await bot.get_channel(int(tts_channel)).send(str(message.author) + " said " + message.content, tts=tts)

bot.run(discord_token)

