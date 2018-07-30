import configparser #ConfigParser to connect to oanda
import pandas as pd #pandas
import oandapy as opy #oanda api python wrapper
import numpy as np #number/data analytics module
from IPython import get_ipython #pull from iPython for matlab

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
cols = []
for frame in f:
    frame.index = pd.DatetimeIndex(frame.index)
    frame.info()
    frame['returns'] = np.log(frame['closeAsk']/frame['closeAsk'].shift(1))
    for momentum in [15, 30, 60, 120]:
        col = 'position_%s' % momentum
        print(frame['returns'].rolling(momentum).mean())
        frame[col] = np.sign(frame['returns'].rolling(momentum).mean())
        cols.append(col)
ipy = get_ipython()
ipy.run_line_magic('matplotlib', 'inline')
