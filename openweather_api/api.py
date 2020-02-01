import requests
from . import _api_key


class KeyMixin(object):
    def api_key(self):
        return _api_key()


class CityWeatherApi(KeyMixin):
    def weather(self, city):
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key()}')
        return r.json()
