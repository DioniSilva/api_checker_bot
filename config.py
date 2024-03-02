import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('API_BASE_URL')
email = os.getenv('USER_EMAIL')
password = os.getenv('USER_PASSWORD')

token = os.getenv('DISCORD_TOKEN')
channel = os.getenv('DISCORD_CHANNEL')

API_ENDPOINTS = {
    'login': f'{base_url}/public/login',
    'listagem': f'{base_url}/tasks/list/synchronized',
}

USER_DEFAULT = {
    'email': email,
    'password': password
}

CALL_INTERVAL_MINUTES = int(os.getenv('CALL_INTERVAL_MINUTES') or 1)  # Intervalo entre as chamadas em minutos
REQUEST_QUANTITIES = int(os.getenv('REQUEST_QUANTITIES') or 100)

DISCORD = {
    'token': token,
    'channel': channel
}