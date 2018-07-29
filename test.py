import configparser

import pandas as pd

import oandapy as opy
config = configparser.ConfigParser()
config.read('oanda.cfg')
oanda = opy.API(environment='practice', access_token = '841e0af7b84586d7df37f3788cefa3bd-5dab7842f80ee94ebaf0134ad3c4dc0b')
print('successfully pulled oandapy')

dataOne = oanda.get_history(instruments = 'EUR_USD', start='2018-7-25', end='2018-7-27', granularity = 'M1')
dataTwo = oanda.get_history(instruments = 'USD_CAD', start='2018-7-25', end='2018-7-27', granularity = 'M1')
