#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pycoingecko')


# In[2]:


from pycoingecko import CoinGeckoAPI


# In[3]:


cg=CoinGeckoAPI()


# In[4]:


bitcoin_data=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)


# In[24]:


bitcoin_price_data=bitcoin_data['prices']


# In[6]:


import pandas as pd


# In[25]:


data=pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','Price'])


# In[26]:


data


# In[27]:


data['Date'] = pd.to_datetime(data['TimeStamp'],unit='ms')


# In[28]:


data


# In[29]:


candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})


# In[30]:


candlestick_data


# In[35]:


get_ipython().system('pip install plotly')


# In[50]:


import plotly.graph_objects as go


# In[48]:


dir(matplotlib.pyplot)


# In[61]:


fig=go.Figure(data=[go.Candlestick(x= candlestick_data.index, 
                                   open=candlestick_data['Price']['first'], 
                                   high=candlestick_data['Price']['max'],
                                   low=candlestick_data['Price']['min'],
                                   close=candlestick_data['Price']['last'])])


# In[62]:


fig


# In[60]:


fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
                  yaxis_title='Price(USD$)',
                  title='Bitcoin Candlestick Chart Over Past 30 Days')


# In[ ]:




