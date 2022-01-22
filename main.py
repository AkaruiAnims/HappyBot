import discord
import os
import requests
import asyncio
from pytz import timezone, all_timezones
from datetime import datetime
from replit import db
from active import keep_alive
from discord.ext import commands

token = os.getenv("token")
bot = commands.Bot(command_prefix="happy ", description="Discord Vistual Assistant")
prefix = "happy"
again = ""
prevAuthor = ""
msgStage = 0
free = True

@bot.event
async def  on_ready():
    print("Active")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  global again
  if message.content.startswith('happy again') or message.content.startswith('again happy') and again != "":
    message.content = again

  if message.content.startswith('what time is it happy') or message.content.startswith('happy what time is it') or message.content.startswith('what time is it'):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await message.channel.send(f"Right now it's  {current_time}")

  if message.content.startswith('how do i get started happy'):
    await message.channel.send(f"""To get strated say; 'happy register me'.
Answer some questions and I'll take care fo the rest :)""")
  
  again = message.content
    
keep_alive()
bot.run(token)