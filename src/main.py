from pandas_datareader import data
import pandas as pd
import numpy as np

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
    shares, weight = readFile("xp")
    start_date = '2019-12-03'
    end_date = '2020-03-03'

    returnArr = []
    df = data.DataReader(shares, 'yahoo', start_date, end_date)
    df.reset_index(inplace=True)
    #df[("Open", "TGAR11.SA")][df[("Date","")] == "2020-03-03"] = 131.80 #yahoo finance dont returning correct value here 

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
    shDf["m1E"] = (shDf["m1P"] - shDf["m1P"].sum()) * 100
    shDf["m2E"] = (shDf["m2P"] - shDf["m2P"].sum()) * 100
    shDf["m3E"] = (shDf["m3P"] - shDf["m3P"].sum()) * 100
    shDf["m1EQ"] = shDf["m1E"] **2
    shDf["m2EQ"] = shDf["m2E"] **2
    shDf["m3EQ"] = shDf["m3E"] **2
    shDf["variance"] = (shDf["m1EQ"] +shDf["m2EQ"] +shDf["m3EQ"]) * (1/(3-1))
    shDf["stdDev"] = shDf["variance"] ** (1/2)
    print(shDf)

def marko2():
    return True
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

#if __name__ == 'main':
marko1()
marko2()
marko3()
marko4()
marko5()
marko6()
marko7()