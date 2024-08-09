from dotenv import load_dotenv
import os
import requests
import asyncio
import interactions
import aiohttp
import math

load_dotenv()

TOKEN = os.environ['ALTTOKEN']

bot = interactions.Client(token=TOKEN,
                          intents=interactions.Intents.DEFAULT)

guild_ids = [647540844873646080]


@interactions.slash_command(name="ping", description="Ping command")
async def ping(ctx: interactions.SlashContext):
    await ctx.send("Pong!")


@interactions.slash_command(name='stridesize', description='Calculates the stride size of a singular move',
                            scopes=guild_ids, options=[
        interactions.SlashCommandOption(name='vertical', type=interactions.OptionType.INTEGER, description='Vertical '
                                                                                                           'length of move',
                                        required=True),
        interactions.SlashCommandOption(name='horizontal', type=interactions.OptionType.INTEGER,
                                        description='Horizontal length of move',
                                        required=True),
        interactions.SlashCommandOption(name='counts', type=interactions.OptionType.INTEGER,
                                        description='Count number of move',
                                        required=True)])
async def stridesize(ctx: interactions.SlashContext, vertical, horizontal, counts):
    await ctx.defer()
    num = pow(vertical, 2) + pow(horizontal, 2)
    num = math.sqrt(num)
    num /= counts

    num = 1 / num
    num *= 8

    await ctx.send('This move is ' + str(num) + ' to 5')


bot.start()
