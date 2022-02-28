# %%

heightmap = []

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        heightmap.append(line.rstrip())
        
lowpoints = []

for i in range(len(heightmap)):
    
    for j in range(len(heightmap[i])):
        
        adj = []
        
        target = int(heightmap[i][j])
        
        if i > 0: #up
            adj.append(int(heightmap[i-1][j]))
        
        if i < len(heightmap) - 1: #down
            adj.append(int(heightmap[i+1][j]))
            
        
        if j > 0: #left
            adj.append(int(heightmap[i][j-1]))    
            
        if j < len(heightmap[i]) - 1: #right
            adj.append(int(heightmap[i][j+1]))
            
        if target < min(adj):
            lowpoints.append(target)
            
risk = 0

for low in lowpoints:
    
    risk += (low+1)
    
print(risk)