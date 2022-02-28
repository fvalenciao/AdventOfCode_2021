import numpy as np

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        crabs = list(map(int, line.split(',')))
        
origins = np.linspace(0, max(crabs), num = max(crabs) +1)
fuel_cost = []

for origin in origins:
    
    fuel = 0
    
    for crab in crabs:
        
        steps = abs(origin-crab)
        
        fuel += steps*(steps+1) / 2

    fuel_cost.append(fuel)

print(min(fuel_cost))