# openweathermap-cli

## Install
For local package installation  - `python setup.py install`

For development linking - `python setup.py develop`

## Configure 
1. Register at openweathermap.org
1. Generate api key
1. Copy .openweathermaprc into the home folder
1. Replace dummy `api_key` value with a generated key

## Execute in test mode
Use `--mode test` to run program in the test mode, this will result in calling 
sample api endpoint, without required installation of api key  