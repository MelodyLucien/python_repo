#!/usr/bin/python3
import pandas as pd

import quandl

quandl.ApiConfig.api_key = 'UqFxQsZQUXnBRfLxAnsp'
df = quandl.get_table('WIKI/PRICES')

df = df[["adj_open","adj_high","adj_low","adj_close","adj_volume"]]

df['HL-PCT']=(df['adj_high']-df['adj_close'])/df["adj_close"] *100.0

df['HL-change']=(df['adj_close']-df['adj_open'])/df["adj_close"] *100.0

df = df[['adj_close',"adj_volume",'HL-PCT','HL-change']]

print(df)









