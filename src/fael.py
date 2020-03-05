from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2020-01-01'
end_date = '2020-03-05'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader('UBSR11.SA', 'yahoo', start_date, end_date)

print(panel_data.tail(9))