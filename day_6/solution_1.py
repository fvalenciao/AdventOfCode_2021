
with open('input.txt', 'r') as f:
    
    for line in f:
        
        lanterns = line.split(',')
        

lanterns = list(map(int, lanterns))
day = 0

while day < 256:
    
    day += 1
    new_lants = []
    
    for i in range(len(lanterns)):
        
        if lanterns[i] == 0:
            
            new_lants.append(8)
            lanterns[i] = 6
            
        else:
            lanterns[i] -= 1
        
            
    lanterns.extend(new_lants)
    
print(len(lanterns))
            
