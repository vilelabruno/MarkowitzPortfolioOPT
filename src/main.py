from pandas_datareader import data
import datetime
import pandas as pd

def readFile(stockbroker):
    shares = []
    weight = []
    with open("../januaryData/"+stockbroker+".txt") as prtf:
        shares = prtf.readline().split(",")
        shares[len(shares)-1] = shares[len(shares)-1].strip()
        weight = prtf.readline().split(",")
        weight[len(weight)-1] = weight[len(weight)-1].strip()
    return shares, weight

def marko1():
    shares = []
    monthReturn = []
    weight = []
    shares, weight = readFile("necton")
    start_date = '2019-12-03'
    end_date = '2020-03-03'

    for share in shares:
        returnArr = []
        df = data.DataReader(share, 'yahoo', start_date, end_date)
        df.reset_index(inplace=True)
        op = df["Open"][df["Date"] == "2019-12-02"] 
        #print(df.tail())
        cl = df["Close"][df["Date"] == "2020-01-06"]
        returnArr.append(cl-op)
        op = df["Open"][df["Date"] == "2020-01-06"] 
        #print(df.tail())
        cl = df["Close"][df["Date"] == "2020-02-02"]
        returnArr.append(cl-op)
        op = df["Open"][df["Date"] == "2020-02-03"] 
        #print(df.tail())
        cl = df["Close"][df["Date"] == "2020-03-02"]
        print(cl[58])
        returnArr.append(cl-op)
    print(returnArr)

def marko2():
    shares, weight = readFile('necton')
    start_date = '2019-12-03'
    end_date = '2020-03-03'
    
    df = data.DataReader(shares, 'yahoo', start_date, end_date)
    df.reset_index(inplace=True)
    df[("Close", "TGAR11.SA")][df[("Date","")] == "2020-02-28"] = 131.80
    getFirstLastDaysOfMonth(2019, 12, df)
    
    ri = []
    for share in shares:
        init = df['Open'][share][df['Date'] == '2019-12-03'].iloc[0]
        fin = df['Close'][share][df['Date'] == '2019-12-30'].iloc[0]
        ror = ((fin - init) / init) * 100 # Rate of return
        
        init = df['Open'][share][df['Date'] == '2020-01-02'].iloc[0]
        fin = df['Close'][share][df['Date'] == '2020-01-31'].iloc[0]
        ror += ((fin - init) / init) * 100 # Rate of return
        
        init = df['Open'][share][df['Date'] == '2020-02-03'].iloc[0]
        fin = df['Close'][share][df['Date'] == '2020-02-28'].iloc[0]
        ror += ((fin - init) / init) * 100 # Rate of return
        ri.append(ror/3)
        
    eror = 0
    for i in range(0, len(weight)):
        eror += float(weight[i]) * float(ri[i])
    
    print(eror)
def marko3():
    return True
def marko4():
    return True
def marko5():
    return True
def marko6():
    return True
def marko7():
    return True
def getFirstLastDaysOfMonth(year, month, dataframe):
    first = 0
    last = 0
    
    print(dataframe['Date'][dataframe['Date'].apply(lambda x: x.month) == month][0])
    
    return first, last

#if __name__ == 'main':
#marko1()
marko2()
marko3()
marko4()
marko5()
marko6()
marko7()