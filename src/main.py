from pandas_datareader import data

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