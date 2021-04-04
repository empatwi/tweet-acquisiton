from decouple import config

API_KEY = config('API_KEY')
API_KEY_SECRET = config('API_KEY_SECRET')
BEARER_TOKEN = config('BEARER_TOKEN')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

TRACKED_TOPICS = [
    "BBB", 
    "Big Brother Brasil",
    "Coronavírus",
    "Corona",
    "Covid 19",
    "Bolsonaro"]