from pandas_datareader import data
import datetime
import pandas as pd
import numpy as np
import more_itertools as mit


def readFile(stockbroker):
    shares = []
    weight = []
    with open("../februaryData/"+stockbroker+".txt") as prtf:
        shares = prtf.readline().split(",")
        shares[len(shares)-1] = shares[len(shares)-1].strip()
        weight = prtf.readline().split(",")
        weight[len(weight)-1] = weight[len(weight)-1].strip()
    return shares, weight

def marko1():
    shares = []
    monthReturn = []
    weight = []
    shares, weight = readFile("itau")
    start_date = '2019-12-03'
    end_date = '2020-03-03'

    returnArr = []
    df = data.DataReader(shares, 'yahoo', start_date, end_date)
    df.reset_index(inplace=True)
    #df[("Open", "TGAR11.SA")][df[("Date","")] == "2020-03-03"] = 131.80 #yahoo finance dont returning correct value here 
    #df.to_csv("dr.csv", index=False)
    shDf = pd.DataFrame(shares,columns=["share"])
    shDf.reset_index(inplace=True)
    shDf["m1R"] = 0
    shDf["m1P"] = 0
    shDf["m2R"] = 0
    shDf["m2P"] = 0
    shDf["m3R"] = 0
    shDf["m3P"] = 0
    for share in shares:
        cl1 = df[('Close', share)][df[("Date","")] == "2020-01-03"]
        op1 = df[('Open', share)][df[("Date","")] == "2019-12-03"]
        cl2 = df[('Close', share)][df[("Date","")] == "2020-02-05"]
        op2 = df[('Open', share)][df[("Date","")] == "2020-01-03"]
        cl3 = df[('Close', share)][df[("Date","")] == "2020-02-05"]
        op3 = df[('Open', share)][df[("Date","")] == "2020-03-03"]
        #print(op2.iloc[0])
        shDf["m1R"][shDf["share"] == share] = cl1.iloc[0] - op1.iloc[0]
        shDf["m1P"][shDf["share"] == share] = (cl1.iloc[0] - op1.iloc[0]) / df[('Open', share)][df[("Date","")] == "2019-12-03"].iloc[0]
        shDf["m2R"][shDf["share"] == share] = (cl2.iloc[0] - op2.iloc[0])
        shDf["m2P"][shDf["share"] == share] = (cl2.iloc[0] - op2.iloc[0]) / df[('Open', share)][df[("Date","")] == "2020-01-03"].iloc[0]
        shDf["m3R"][shDf["share"] == share] = (cl3.iloc[0] - op3.iloc[0])
        shDf["m3P"][shDf["share"] == share] = (cl3.iloc[0] - op3.iloc[0]) / df[('Open', share)][df[("Date","")] == "2020-03-03"].iloc[0]
    shDf["m1E"] = (shDf["m1P"] - (shDf["m1P"]+shDf["m2P"]+shDf["m3P"])) * 100
    shDf["m2E"] = (shDf["m2P"] - (shDf["m1P"]+shDf["m2P"]+shDf["m3P"])) * 100
    shDf["m3E"] = (shDf["m3P"] - (shDf["m1P"]+shDf["m2P"]+shDf["m3P"])) * 100
    shDf["m1EQ"] = shDf["m1E"] **2
    shDf["m2EQ"] = shDf["m2E"] **2
    shDf["m3EQ"] = shDf["m3E"] **2
    shDf["variance"] = (shDf["m1EQ"] +shDf["m2EQ"] +shDf["m3EQ"]) * (1/(3-1))
    shDf["stdDev"] = shDf["variance"] ** (1/2)
    shDf["mi"] = (shDf["m1E"] + shDf["m2E"] + shDf["m3E"]) /3
    assets = shDf.share.values
    print(shDf)
    for asset1 in assets:
        shDf[asset1] = 0
    for asset1 in assets:
        for asset2 in assets:
            shDf[asset1][shDf["share"] == asset2] = (1/2) * ((shDf["m1E"][shDf["share"] == asset1].iloc[0] * shDf["m1E"][shDf["share"] == asset2].iloc[0]) +\
                (shDf["m2E"][shDf["share"] == asset1].iloc[0] * shDf["m2E"][shDf["share"] == asset2].iloc[0]) +\
                    (shDf["m3E"][shDf["share"] == asset1].iloc[0] * shDf["m3E"][shDf["share"] == asset2].iloc[0]))

    print(shDf)
    #cov = (1/2) * ( (m1s1 * m1s2* m1s3* m1s4* m1s5* m1s6* m1s7* m1s8) +(m2s1 * m2s2* m2s3* m2s4* m2s5* m2s6* m2s7* m2s8) +(m3s1 * m3s2* m3s3* m3s4* m3s5* m3s6* m3s7* m3s8))
    #print('Covariance: '+str(cov))
    shDf.to_csv("shDf2.csv", index=False)
    ##print(shDf)
    #corre = cov / shDf['stdDev'].prod() #Correlation
    #print('Correlation: '+str(corre))

def marko2():
    shares, weight = readFile('necton')
    start_date = '2019-12-03'
    end_date = '2020-03-03'
    
    df = data.DataReader(shares, 'yahoo', start_date, end_date)
    df.reset_index(inplace=True)
    df[("Close", "TGAR11.SA")][df[("Date","")] == "2020-02-28"] = 131.80
    
    months = [12, 1, 2]
    ri = []
    for share in shares:
        for m in months:
            first, last = getFirstLastDaysOfMonth(m, df)
            init = df['Open'][share][df['Date'] == first].iloc[0]
            fin = df['Close'][share][df['Date'] == last].iloc[0]
            ror = ((fin - init) / init) * 100 # Rate of return
        
            ri.append(ror/3)
        
    eror = 0
    for i in range(0, len(weight)):
        eror += float(weight[i]) * float(ri[i])
    
    print('Extimated Rate of Return: '+str(eror))
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
def getFirstLastDaysOfMonth(month, dataframe):
    first = 0
    last = 0
    
    first = mit.first(dataframe['Date'][dataframe['Date'].apply(lambda x: x.month) == month])
    last = mit.last(dataframe['Date'][dataframe['Date'].apply(lambda x: x.month) == month])
    
    return str(first.date()), str(last.date())

#if __name__ == 'main':
marko1()
#marko2()
#marko3()
marko4()
marko5()
marko6()
marko7()