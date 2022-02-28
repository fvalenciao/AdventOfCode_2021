#%%
def find_path(connect, small, path):
    
    neighbors = connect[path[-1]]
    
    for neighbor in neighbors:
        

lines = []

with open('input.txt','r') as f:
    
    for line in f.readlines():
        lines.append(line.rstrip().split('-'))

## make list with names of all caves
caves = []
for line in lines:
    for i in line:
        
        if i not in caves:
            caves.append(i)

## make dictionary with connectivity of all caves
## and identify big and small caves
connect = {}
big_caves = []
small_caves = []

for cave in caves:
    connect[cave] = []
    
    if cave == cave.lower():
        small_caves.append(cave)
        
    else:
        big_caves.append(cave)

small_caves.remove('start')
small_caves.remove('end')

## fill connectivity dictionary
for line in lines:
    connect[line[0]].append(line[1])
    connect[line[1]].append(line[0])
# %%
