from __future__ import division
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
%matplotlib inline

from pandas_datareader import DataReader
from datetime import datetime


# initializing the tech list and getting stock prices

tech_list = ['AAPL','GOOGL','MSFT','AMZN']

end = datetime.now()
start = datetime(end.year-1,end.month,end.day)

for stock in tech_list:
    globals()[stock] = DataReader(stock,'iex',start,end)


#Basic Stock Information Analysis

AAPL.head()
AAPL.describe()
AAPL.info()
AAPL['close'].plot(legend=True, figsize=(10,4))
AAPL['volume'].plot(legend=True, figsize=(10,4))

# moving averages

MA_day = [10,20,50,100]

for ma in MA_day:
    column_name = 'MA for %s days' %(str(ma))
    AAPL[column_name] = AAPL['close'].rolling(ma).mean()


AAPL[['close','MA for 10 days','MA for 20 days','MA for 50 days','MA for 100 days']].plot(subplots=False,figsize=(10,4))


#Daily Return Analysis

AAPL['Daily Return'] = AAPL['close'].pct_change()

AAPL['Daily Return'].plot(figsize=(12,4), legend=True, linestyle='--', marker='o')

AAPL['Daily Return'].hist(bins=100)

closingprice_df = DataReader(tech_list, 'iex', start, end)['close']
closingprice_df.head(10)

tech_returns = closingprice_df.pct_change()
tech_returns.head()

sns.jointplot('GOOGL','AMZN',tech_returns, kind='hex',height=8, color='skyblue')

sns.pairplot(tech_returns.dropna(),height=3)

sns.heatmap(tech_returns.corr(),annot=True,fmt=".3g",cmap='YlGnBu')


#Risk Analysis

rets = tech_returns.dropna()
rets.head()
