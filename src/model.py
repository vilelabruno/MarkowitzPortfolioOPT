from pulp import *

def main():
    x = LpVariable('x')
    w_vars = []
    problem = LpProblem('portfolio_theory', LpMaximize)
    for i in range(v.shape[0]):
        w_i = LpVariable('w_' + str(i), 0, 1)
        w_vars.append(w_i)
    for vector in vv_set.set:
        diff_list = []
        for index, _ in enumerate(vector):
            diff = v[index] - vector[index]
            diff_list.append(w_vars[index] * diff)
        problem += reduce(operator.add, diff_list, -x) >= 0
    problem += reduce(operator.add, w_vars, 0) == 1
    problem += x #What to optimise, i.e., x
    status = problem.solve()
    if value(x) <= 0:
        if(len(vv_set.set)==0):
            #Special case: in this case x is not in the problem and 
            #any solution in the weight simplex goes. Therefore, x retained
            #its initial value of 0
            return np.array([value(w) for w in w_vars]), True
        return [], False
    else:
        return np.array([value(w) for w in w_vars]), True 

if __name__ == "main":
    main()