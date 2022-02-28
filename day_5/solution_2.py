import numpy as np

lines = []

with open('input.txt', 'r') as inp_file:
    
    for line in inp_file.readlines():
        
        line = line.rstrip()
        
        lines.append(line.split(' '))

coords = []     # list containing numpy arrays. each array contains the coordinates of the ends of a line


for i in range(len(lines)):
        
    temp_coords = np.zeros([2,2])
    
    temp_coords[0,:] = lines[i][0].split(',')
    temp_coords[1,:] = lines[i][1].split(',')
    
    coords.append(temp_coords) # vertical and horizontal lines only
    
x_bounds = [np.min(coords[0][:,0]), np.max(coords[0][:,0])] # dummy value to initiate variable
y_bounds = [np.min(coords[0][:,1]), np.max(coords[0][:,1])]


for line in coords:
    
    min_x = np.min(line[:,0])
    max_x = np.max(line[:,0])
    min_y = np.min(line[:,1])
    max_y = np.max(line[:,1])
    
    if min_x < x_bounds[0]:
        
        x_bounds[0] = min_x
    
    if max_x > x_bounds[1]:
        
        x_bounds[1] = max_x
        
    if min_y < y_bounds[0]:
        
        y_bounds[0] = min_y
    
    if max_y > y_bounds[1]:
        
        y_bounds[1] = max_y
        
line_map = np.zeros([int(x_bounds[1]- x_bounds[0] + 1), int(y_bounds[1]- y_bounds[0] + 1)])


rel_zero = np.array([[x_bounds[0], y_bounds[0]],[x_bounds[0], y_bounds[0]]]) # origin point of relative coordinates system

for line in coords:
    
    rel_coords = line - rel_zero
    
    x1 = int(rel_coords[0][0])
    x2 = int(rel_coords[1][0])
    y1 = int(rel_coords[0][1])
    y2 = int(rel_coords[1][1])
    
    if x1 == x2:  # horizontal line
    
        if   y2 > y1:
            
            line_map[x1][y1:y2+1] += np.ones(y2 - y1 + 1)
            
            a = line_map[x1][y1:y2+1]
            b = np.ones(y2 - y1 + 1)
            
        else:   
            
            line_map[x1][y2:y1+1] += np.ones(y1 - y2 + 1)
            
            a = line_map[x1][y2:y1+1]
            b = np.ones(y1 - y2 + 1)
            
    elif y1 == y2: # vertical line
    
        if   x2 > x1:
            
            line_map[x1:x2 +1 , y1] += np.ones(x2 - x1 + 1)
            
            a = line_map[x1:x2 +1 , y1]
            b = np.ones(x2 - x1 + 1)
            
        else:   
            line_map[x2:x1 + 1, y1] += np.ones(x1 - x2 + 1)
            
            a = line_map[x2:x1 + 1, y1]
            b = np.ones(x1 - x2 + 1)
    
    else:
        
        if x2 > x1:
            
            if y2 > y1:
                
                j = y1
                
                for i in range(x1, x2+1):
                    
                    line_map[i, j] += 1
                    
                    j += 1
                       
            elif y1 > y2:
                
                j = y1
                
                for i in range(x1, x2+1):
                    
                    line_map[i, j] += 1
                    
                    j -= 1
                                     
        elif x1 > x2:
            
            if y2 > y1:
                
                j = y2
                
                for i in range(x2, x1+1):
                    
                    line_map[i, j] += 1
                    
                    j -= 1
                          
            elif y1 > y2:
                
                j = y2
                
                for i in range(x2, x1+1):
                    
                    line_map[i, j] += 1
                    
                    j += 1
         

intersect = np.where(line_map >= 2)

    

