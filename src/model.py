import pulp

def create_model(self):
    # create the model
    self.model = pulp.LpProblem("Markowitz's_Modern_Portfolio_Theory", pulp.LpMinimize)

    # decision variables: assets percentage
    self.x = pulp.LpVariable('x', lowBound=0.0, upBound=1.0, cat='Continuous')

    # objective function
    self.model += pulp.LpSum()
