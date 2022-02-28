
with open('input.txt', 'r') as f:
    
    for line in f:
        
        lanterns = line.split(',')
        

lanterns = list(map(int, lanterns))

lanterns_count = []
update_count = []

for i in range(9):
    
    lanterns_count.append(lanterns.count(i))
    update_count.append(0)
    
day = 0

while day < 256:
    
    day += 1
    
    for i in range(len(lanterns_count)-1,-1,-1):
        
        update_count[i-1] = lanterns_count[i]
        
        if i == 0:
            
            update_count[6] += lanterns_count[i]
    
    lanterns_count = update_count.copy()
    
total = sum(lanterns_count)
    
    
    
    
            
