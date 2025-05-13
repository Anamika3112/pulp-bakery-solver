from pulp import *

#Elementary features:

lp = LpProblem("Bakery_Problem", LpMaximize)

#Define variables
x1 = LpVariable(name="Bowdoin_log", lowBound=0, cat="Integer")
x2 = LpVariable(name="Chocolate_cake", lowBound=0, cat="Integer")

#Add the objective function
lp += 10 * x1 + 5 * x2
print(lp.objective)

# Add the constraints
lp += (5 * x1 + x2 <= 90, "oven_constraint")
lp += (x1 + 10 * x2 <= 300, "food_processor_constraint")
lp += (4 * x1 + 6 * x2 <= 125, "boiler_constraint")
print(lp.constraints)

# Solve the LP
status = lp.solve(PULP_CBC_CMD(msg=0))
print("Status:", status) #1:optimal, 2:not solved, 3:infeasible, 4:unbounded, 5:undef

#Print solution
for var in lp.variables():
    print(var, "=", value(var))
print("OPT =", value(lp.objective))
