import click
import json
import os

from openweather_api.api import ApiFactory


@click.command()
@click.option('--city', default='Hamburg')
@click.option('--mode', default=None, type=click.Choice(['test', 'api'], case_sensitive=False))
def city_weather_cli(city, mode):
    api = ApiFactory().create(mode)

    res = api.weather(city)
    out = json.dumps(res, indent=2, sort_keys=True)
    os.sys.stdout.write(out)
