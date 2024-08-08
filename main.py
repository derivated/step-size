from dotenv import load_dotenv
import os
import requests
import asyncio
import interactions
import aiohttp
import math

load_dotenv()

TOKEN = os.environ['ALTTOKEN']

bot = interactions.Client(TOKEN,
                          intents=interactions.Intents.DEFAULT)

guild_ids = [647540844873646080]

@bot.command(name="ping", description="Ping command", scope=guild_ids)
async def ping(ctx: interactions.CommandContext):
    await ctx.send("Pong!")

@bot.command(name='lowestbin', description='Lowest bin command', scope=guild_ids, options=[
    interactions.Option(name='vertical', type=interactions.OptionType.INTEGER, description='Vertical length of move',
                        required=True), interactions.Option(name='horizontal', type=interactions.OptionType.INTEGER, description='Horizontal length of move',
                        required=True), interactions.Option(name='counts', type=interactions.OptionType.INTEGER, description='counts of move',
                        required=True)])
async def lowestbin(ctx: interactions.CommandContext, vertical, horizontal, counts):

    num = pow(vertical,2) + pow(horizontal, 2)
    num = math.sqrt(num)
    num /= counts

    num = 1 / num
    num *= 8



    await ctx.send(str(num))