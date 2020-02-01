import unittest

import requests_mock

from openweather_api.api import CityWeatherApi


class CityWeatherApiSut(CityWeatherApi):

    def api_key(self):
        return 'dummy_key'


@requests_mock.Mocker()
class TestNothing(unittest.TestCase):
    sut = CityWeatherApiSut()

    def test_nothing(self, m):
        m.get('https://api.openweathermap.org/data/2.5/weather?q=Hamburg&appid=dummy_key',
              json={'city': 'Hamburg', 'temp': 1.1})
        r = self.sut.weather('Hamburg')
        self.assertEqual(r, {'city': 'Hamburg', 'temp': 1.1})
