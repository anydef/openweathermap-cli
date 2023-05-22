import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()
print(packages)
setuptools.setup(
    name="openweathermap-cli",
    version="0.0.1",
    author="Pavlo Fedyna",
    author_email="fed.pavlo@gmail.com",
    description="Small cli utility fetching weather and forecasts from openweathermap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anydef/openweathermap-cli",
    packages=packages,
    install_requires=['requests == 2.31.0', 'pytest == 5.3.5', 'requests-mock == 1.7.0', 'click == 7.0'],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['openweathermap-cli = cli.weather:city_weather_cli'],
    },
)
