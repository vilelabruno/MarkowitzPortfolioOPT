import pandas as pd

shDf = pd.read_csv("../output/shDf.csv")

with open("shDf.txt", "w") as shDfT:
    for vl in shDf["share"].values:
        shDfT.write(vl+",")
    shDfT.write("\n")    
    for vl in shDf["mi"].values:
        shDfT.write(str(vl)+",")
    shDfT.write("\n")
    for vl in shDf["share"].values:
        for vl2 in shDf["share"].values:
            if vl != vl2:
                shDfT.write(str(shDf[vl][shDf["share"] == vl2].iloc[0])+",")
        shDfT.write("\n")

