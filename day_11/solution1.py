#%%
import numpy as np

def find_adj_ind(map, a, b):
    # a and be are the indexes of the
    
    adj_ind = []
    
    if a > 0: #up
        adj_ind.append([a-1, b])
        
        if b < len(map[a]) - 1: #upper right corner
            adj_ind.append([a-1, b+1]) 
            
        if b > 0: #upper left corner
            adj_ind.append([a-1, b-1])
        
    if a < len(map) - 1: #down
        adj_ind.append([a+1, b])
        
        if b < len(map[a]) - 1: #lower right corner
            adj_ind.append([a+1, b+1]) 
            
        if b > 0: # lower left corner
            adj_ind.append([a+1, b-1])
        
    if b > 0: #left
        adj_ind.append([a, b-1])    
        
    if b < len(map[a]) - 1: #right
        adj_ind.append([a, b+1])
        
    return(adj_ind)

def flash(map, flashed, a, b):
    
    if map[a][b] > 9:
        if flashed[a][b] == 0:
            flashed[a][b] = 1
            adj_ind = find_adj_ind(map, a, b)
            
            for adj in adj_ind:
                i, j = adj[0], adj[1]
                map[i][j] += 1
                
                flash(map, flashed, i, j)

def reset_energy(map):
    
    for i in range(len(map)):
        
        for j in range(len(map[i])):
            
            if map[i][j] > 9:
                map[i][j] = 0
    
levels = []

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        line = line.rstrip()
        level = []
        for a in line:
            level.append(int(a))
        levels.append(level)

total_flashes = 0
steps = 0
synched = []

while True:
    
    has_flashed = np.zeros([10, 10])
    
    for i in range(len(levels)):
        
        for j in range(len(levels[i])):
            
            levels[i][j] += 1
            
            if levels[i][j] > 9:
                flash(levels, has_flashed, i, j)

    flashes = np.count_nonzero(has_flashed == 1)
    
    total_flashes += flashes
    
    reset_energy(levels)
    
    steps += 1
    
    if flashes == len(levels)**2:
        synched.append(steps)
        break

print(total_flashes)
print(synched)

