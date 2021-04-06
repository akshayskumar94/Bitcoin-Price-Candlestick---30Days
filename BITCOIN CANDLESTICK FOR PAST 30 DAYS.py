#!/usr/bin/env python
# coding: utf-8

# In[1]:CODE TO OBTAIN CANDLE STICK PLOT TO GET PRICE FLUCTUATION ON BITCOIN FOR PAST 30 DAYS


get_ipython().system('pip install pycoingecko') #INSTALL pycoingecko
from pycoingecko import CoinGeckoAPI #Import CoinGecko API

cg=CoinGeckoAPI()

bitcoin_data=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)

bitcoin_price_data=bitcoin_data['prices']

import pandas as pd

data=pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','Price'])

print(data)

data['Date'] = pd.to_datetime(data['TimeStamp'],unit='ms')

print(data)

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})

candlestick_data

get_ipython().system('pip install plotly')

import plotly.graph_objects as go

fig=go.Figure(data=[go.Candlestick(x= candlestick_data.index, 
                                   open=candlestick_data['Price']['first'], 
                                   high=candlestick_data['Price']['max'],
                                   low=candlestick_data['Price']['min'],
                                   close=candlestick_data['Price']['last'])])


print(fig)

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
                  yaxis_title='Price(USD$)',
                  title='Bitcoin Candlestick Chart Over Past 30 Days')



