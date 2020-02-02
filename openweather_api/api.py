import requests
from . import _api_key


class KeyMixin(object):
    def api_key(self):
        return _api_key()


class CityWeatherApi(KeyMixin):
    def weather(self, city):
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key()}')
        r.raise_for_status()
        return r.json()


class SampleWeatherApi():
    def weather(self, _):
        r = requests.get(
            'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
        r.raise_for_status()
        return r.json()


class ApiFactory(object):
    def create(self, mode):
        if mode == 'test':
            return SampleWeatherApi()
        return CityWeatherApi()
