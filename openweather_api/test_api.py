import unittest

import requests_mock

from openweather_api.api import CityWeatherApi, SampleWeatherApi


class CityWeatherApiSut(CityWeatherApi):

    def api_key(self):
        return 'dummy_key'


@requests_mock.Mocker()
class TestWeatherApi(unittest.TestCase):
    sut = CityWeatherApiSut()

    def test_nothing(self, m):
        m.get('https://api.openweathermap.org/data/2.5/weather?q=Hamburg&appid=dummy_key',
              json={'city': 'Hamburg', 'temp': 1.1})
        r = self.sut.weather('Hamburg')
        self.assertEqual(r, {'city': 'Hamburg', 'temp': 1.1})


@requests_mock.Mocker()
class TestSampleWeatherApi(unittest.TestCase):
    sut = SampleWeatherApi()

    def test_nothing(self, m):
        m.get('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22',
              json={'city': 'Hamburg', 'temp': 1.1})
        r = self.sut.weather('Hamburg')
        self.assertEqual(r, {'city': 'Hamburg', 'temp': 1.1})


