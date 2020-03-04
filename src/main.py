from pybovespa.bovespa import *
from pybovespa.stock import *

def main():
    shares = []
    weight = []
    with open("../januaryData/necton.txt") as prtf:
        shares = prtf.readline().split(",")
        shares[len(shares)-1] = shares[len(shares)-1].strip()
        weight = prtf.readline().split(",")
        weight[len(weight)-1] = weight[len(weight)-1].strip()
    for share in shares:
        bovespa = Bovespa()
        stock = bovespa.query(share)
        print(stock.cod, stock.name, stock.last)


#if __name__ == 'main':
main()