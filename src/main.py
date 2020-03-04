import investpy

def main():
    shares = []
    weight = []
    with open("../januaryData/necton.txt") as prtf:
        shares = prtf.readline().split(",")
        shares[len(shares)-1] = shares[len(shares)-1].strip()
        weight = prtf.readline().split(",")
        weight[len(weight)-1] = weight[len(weight)-1].strip()
    
    for share in shares:
        df = investpy.get_stock_historical_data(stock=share,country='brazil',from_date='01/01/2020',to_date='03/02/2020')
        df.reset_index(inplace=True)
        op = df["Open"][df["Date"] == "2020-01-01"] 
        #print(df.tail())
        cl = df["Close"][df["Date"] == "2020-02-02"]
        print(op[0] - cl )

#if __name__ == 'main':
main()