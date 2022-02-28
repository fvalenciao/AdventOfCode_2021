#%%

lines = []

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        lines.append(line.rstrip())
        
score = 0

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

points = [3, 57, 1197, 25137]
for line in lines:
    
    # indexes: () = 0, [] = 1, {} = 2, <> = 3
    open_chunks = []
    
    for i in line:
        
        if i in openers:
            
            open_chunks.append(i)
        
        else:
            
            if open_chunks[-1] == openers[closers.index(i)]:
                del open_chunks[-1]
                
            else:
                score += points[closers.index(i)]
                break

print(score)

