import unittest
from openweather_api.api import weather

class TestNothing(unittest.TestCase):
    def test_nothing(self):
        print(weather('banana'))
