import discord
from discord.ext import commands
import aiohttp
import json
import asyncio
import logging
from config import DISCORD, API_ENDPOINTS, USER_DEFAULT, REQUEST_QUANTITIES, CALL_INTERVAL_MINUTES

TOKEN = DISCORD['token']
CHANNEL_ID = DISCORD['channel']
LOGIN_URL = API_ENDPOINTS['login']
REQUEST_LIST_URL = API_ENDPOINTS['listagem']

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    logger.info(f'{bot.user.name} está online!')
    try:
        channel = await bot.fetch_channel(int(CHANNEL_ID))
        await channel.send('Estou online!')
        await main()
    except discord.errors.NotFound:
        logger.error(f"Channel with ID {CHANNEL_ID} not found!")


async def send_message(message):
    try:
        channel = await bot.fetch_channel(int(CHANNEL_ID))
        await channel.send(message)
    except discord.errors.NotFound:
        logger.error(f"Channel with ID {CHANNEL_ID} not found!")


async def get_access_token():
    payload = {
        'email': USER_DEFAULT['email'],
        'password': USER_DEFAULT['password']
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(LOGIN_URL, json=payload) as response:
            if response.status == 200:
                return (await response.json())['accessToken']
            else:
                error_message = f"Failed to get access token: \nStatus Code: {response.status}\nResponse: {await response.text()}"
                logger.error(error_message)
                await send_message(error_message)
                return None


async def make_requests(access_token, num_requests=100):
    log = []
    success_count = 0
    error_count = 0
    headers = {
        'Authorization': access_token
    }
    async with aiohttp.ClientSession() as session:
        for i in range(num_requests):
            async with session.post(REQUEST_LIST_URL, json=[0], headers=headers) as response:
                logger.info(f"Request {i+1}/{num_requests} completed. Status Code: {response.status}")
                if response.status != 200:
                    log.append({
                        "request_number": i+1,
                        "status_code": response.status,
                        "response_body": await response.text()
                    })
                    error_count += 1
                else:
                    success_count += 1
    return log, success_count, error_count


async def main():
    time_interval = CALL_INTERVAL_MINUTES * 60  # convertendo minutos para segundos
    num_requests = REQUEST_QUANTITIES
    while True:
        try:
            access_token = await get_access_token()
            if access_token:
                log, success_count, error_count = await make_requests(access_token, num_requests)
                message = f"Total successful requests: {success_count}, Total failed requests: {error_count}"
                logger.info(message)
                await send_message(message)
                if log:
                    with open('error_log.json', 'w') as f:
                        json.dump(log, f, indent=4)
            await asyncio.sleep(time_interval)
        except Exception as e:
            logger.exception("An error occurred in the main loop:")
            await asyncio.sleep(time_interval)


if __name__ == "__main__":
    bot.run(TOKEN)
