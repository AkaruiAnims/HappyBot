import discord
import os
import requests
import datetime
import asyncio

from replit import db
from active import keep_alive
from discord.ext import commands

token = os.getenv("token")
bot = commands.Bot(command_prefix="happy ", description="Discord Vistual Assistant")

@bot.event
async def  on_ready():
    print("Active")

@bot.command()
async def ping(ctx):
    await ctx.send('**pong**')
    
keep_alive()
bot.run(token)