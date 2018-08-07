import configparser #ConfigParser to connect to oanda
import pandas as pd #pandas module
import oandapy as opy #oanda rest API wrapper
import numpy as np #numpy module for data analytics

sets = {('2018-7-23', '2018-7-25')} #date sets

config = configparser.ConfigParser()
config.read('oanda.cfg')
oanda = opy.API(environment='practice', access_token = '841e0af7b84586d7df37f3788cefa3bd-5dab7842f80ee94ebaf0134ad3c4dc0b')
print('successfully pulled oandapy')

for pair in sets:
    st = pair[0]
    nd = pair[1]
    dataOne = oanda.get_history(instrument = 'EUR_USD', start = st, end = nd, granularity = 'M1')
    dataTwo = oanda.get_history(instrument = 'USD_CAD', start = st, end = nd, granularity = 'M1')

#dataOne = oanda.get_history(instrument = 'EUR_USD', start='2018-7-25', end='2018-7-27', granularity = 'M1')
#dataTwo = oanda.get_history(instrument = 'USD_CAD', start='2018-7-25', end='2018-7-27', granularity = 'M1')

frameOne = pd.DataFrame(dataOne['candles']).set_index('time')
frameOne.index = pd.DatetimeIndex(frameOne.index)
frameOne.info()

frameTwo = pd.DataFrame(dataTwo['candles']).set_index('time')
frameTwo.index = pd.DatetimeIndex(frameTwo.index)
frameTwo.info()

frameOne['returns'] = np.log(frameOne['closeAsk'])
