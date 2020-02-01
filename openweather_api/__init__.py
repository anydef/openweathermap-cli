import configparser
from pathlib import Path

home = str(Path.home())
config = configparser.ConfigParser()
config.read(f'{home}/.openweathermaprc')


def _api_key():
    return config.get('default', 'api_key')
