#!/usr/bin/env python3
from pulp import *
import pandas as pd

def main():
    assets = ["GGRC11.SA","HABT11.SA","HFOF11.SA","UBSR11.SA","THRA11.SA","TGAR11.SA","HGBS11.SA","HGPO11.SA"] 
    problem = LpProblem("portfolio_theory", LpMaximize)
    shDf = pd.read_csv("../output/shDf.csv")
    # if x is Binary
    x_vars  = {(i):
    LpVariable(cat=LpContinuous, lowBound= 0.0, upBound=1.0, name="x_{0}".format(i)) 
    for i in range(len(assets))}
    A = 1
    # Less than equal constraints
    c1 = sum([x_vars[i] * 1 for i in range(len(assets))]) == 1
    problem += c1

    # objective function
    objective = lpSum((x_vars[i] * x_vars[j] * shDf[assets[i]][shDf["share"] == assets[j]]) - (A * x_vars[i] * shDf["mi"][shDf["share"] == assets[i]]) for i in range(len(assets)) for j in range(len(assets)))

    # for maximization
    problem.sense = LpMaximize
    problem.setObjective(objective)

    problem.solve()

    result = []
    for v in problem.variables():
      if str(v).startswith("x_") and v.varValue:
        result.append(int(str(v).replace("x_", "")))

    
    print(value(problem.objective))


if __name__ == '__main__':
    main()