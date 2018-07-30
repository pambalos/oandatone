import configparser #ConfigParser to connect to oanda
import pandas as pd #pandas
import oandapy as opy #oanda api python wrapper
import numpy as np #number/data analytics module

sets = {('2018-7-23', '2018-7-26')}
insts = {'EUR_USD', 'USD_CAD'}

config = configparser.ConfigParser()
config.read('oanda.cfg')
oanda = opy.API(environment='practice', access_token = '841e0af7b84586d7df37f3788cefa3bd-5dab7842f80ee94ebaf0134ad3c4dc0b')
print('successfully pulled oanda')
d = [] #raw data set holding list
for pair in sets:
    st = pair[0]
    nd = pair[1]
    for i in insts: #iterate through instruments pulling data and add to datatable holder d
        d.append(oanda.get_history(instrument = i, start = st, end = nd, granularity = 'M1'))

f = [] #dataframe holding list making a frame for each data set
for data in d:
    f.append(pd.DataFrame(data['candles']).set_index('time'))

for frame in f:
    frame.index = pd.DatetimeIndex(frame.index)
    frame.info()
#dataOne = oanda.get_history(instrument = 'EUR_USD', start='2018-7-25', end='2018-7-27', granularity = 'M1')
#dataTwo = oanda.get_history(instrument = 'USD_CAD', start='2018-7-25', end='2018-7-27', granularity = 'M1')
"""
frameOne = pd.DataFrame(dataOne['candles']).set_index('time')
frameOne.index = pd.DatetimeIndex(frameOne.index)
frameOne.info()
print('f1 info')

frameTwo = pd.DataFrame(dataTwo['candles']).set_index('time')
frameTwo.index = pd.DatetimeIndex(frameTwo.index)
frameTwo.info()
print('f2 info')
"""
