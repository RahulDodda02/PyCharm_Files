import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objs as go
from matplotlib import pyplot as plt

data = yf.download(tickers='UBER', period='1mo', interval='5m')
print(data)

fig = go.Figure()
plt.bar(data.index, data['High'], color = 'black', width = 0.4)

fig.add_trace(go.Candlestick(x=data.index, open = data['Open'], high  = data['High'], low = data['Low'], close = data['Close'], name = 'Tesla Market Data - 1 Month'))
fig.update_layout(title = 'Tesla 1 Month Prices', yaxis_title = 'Stock Price (USD per Share)')

fig.show()
plt.show()


