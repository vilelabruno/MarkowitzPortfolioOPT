import pandas as pd

df = pd.read_csv('generic.csv')
tickers = df['Ticker']

st = ""
for t in tickers:
    st = st+t+','
    
file = open("tickers.txt", "a")
file.write(st)
file.close()