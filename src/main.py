from pandas_datareader import data

def marko1():
    shares = []
    weight = []
    with open("../januaryData/necton.txt") as prtf:
        shares = prtf.readline().split(",")
        shares[len(shares)-1] = shares[len(shares)-1].strip()
        weight = prtf.readline().split(",")
        weight[len(weight)-1] = weight[len(weight)-1].strip()
    
    for share in shares:
        start_date = '2020-01-01'
        end_date = '2020-03-05'
        df = data.DataReader(share, 'yahoo', start_date, end_date)
        df.reset_index(inplace=True)
        op = df["Open"][df["Date"] == "2020-01-01"] 
        #print(df.tail())
        cl = df["Close"][df["Date"] == "2020-02-02"]
        print(df.head())

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