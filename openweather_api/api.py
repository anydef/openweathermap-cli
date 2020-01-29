import requests
from . import api_key


def weather(city):
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key()}')
    print(r.text)

