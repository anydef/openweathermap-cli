import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openweathermap-cli",
    version="0.0.1",
    author="Pavlo Fedyna",
    author_email="fed.pavlo@gmail.com",
    description="Small cli utility fetching weather and forecasts from openweathermap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anydef/openweathermap-cli",
    packages=setuptools.find_packages(),
    install_requires=['requests == 2.22.0', 'pytest == 5.3.5', 'requests-mock == 1.7.0'],
    python_requires='>=3.7',
)
