# %%

def find_adj(map, a, b):
    # a and be are the indexes of the
    
    adjac = []
    
    if a > 0: #up
            adjac.append(int(map[a-1][b]))
        
    if a < len(map) - 1: #down
        adjac.append(int(map[a+1][b]))
        
    if b > 0: #left
        adjac.append(int(map[a][b-1]))    
        
    if b < len(map[a]) - 1: #right
        adjac.append(int(map[a][b+1]))
        
    return(adjac)

def find_adj_ind(map, a, b):
    # a and be are the indexes of the
    
    adj_ind = []
    
    if a > 0: #up
        adj_ind.append([a-1, b])
        
    if a < len(map) - 1: #down
        adj_ind.append([a+1, b])
        
    if b > 0: #left
        adj_ind.append([a, b-1])    
        
    if b < len(map[a]) - 1: #right
        adj_ind.append([a, b+1])
        
    return(adj_ind)

def find_basin(map, explored, a, b):
    # a and be are the indexes of the lowpoint in the heightmap
    basin_index = [[a, b]]
    explored[a][b] = 1
    
    adj_ind = find_adj_ind(map, a, b)
    
    for ind in adj_ind:
        
        if ind not in basin_index:
            ind_num = int(map[ind[0]][ind[1]])
            
            if ind_num < 9 and explored[ind[0]][ind[1]] == 0:
                basin_index.extend(find_basin(map, explored, ind[0], ind[1]))
                # explored[ind[0]][ind[1]] = 1
    
    return(basin_index)

heightmap = []

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        heightmap.append(line.rstrip())

explored_points = []

for i in heightmap:
    
    a = []
    
    for j in i:
        a.append(0)
    
    explored_points.append(a)
    

lowpoints = []
basins = []

for i in range(len(heightmap)):
    
    for j in range(len(heightmap[i])):
        
        basin = []
                
        target = int(heightmap[i][j])
        
        adj = find_adj(heightmap, i, j)
            
        if target < min(adj):
            lowpoints.append(target)
            basins.append(find_basin(heightmap, explored_points, i, j))
            

basins_len = []

for i in basins:
    
    basins_len.append(len(i))
