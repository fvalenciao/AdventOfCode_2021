
with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        crabs = list(map(int, line.split(',')))
        
crabs_set = set(crabs)
fuel_cost = []

for origin in crabs_set:
    
    fuel = 0
    
    for crab in crabs:
        
        fuel += abs(origin-crab)

    fuel_cost.append(fuel)

print(min(fuel_cost))