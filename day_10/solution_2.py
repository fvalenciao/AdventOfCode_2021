#%%

def find_corr_lines(lines):
    "returns list of corrupted lines"
    
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    
    corrupted_lines = []
    count = 0
    
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
                    corrupted_lines.append(count)
                    break
        count += 1
    
    return(corrupted_lines)

def find_closing_seq(line):
    
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    
    open_chunks = []
    closing_seq = []
        
    for i in line:
        
        if i in openers:
            
            open_chunks.append(i)
        
        else:
            
            if open_chunks[-1] == openers[closers.index(i)]:
                del open_chunks[-1]
    
    for i in open_chunks[::-1]:
        closing_seq.append(closers[openers.index(i)])
    
    return(closing_seq)

lines = []

with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        lines.append(line.rstrip())
        

corr_lines = find_corr_lines(lines) 

for i in corr_lines[::-1]: # discard corrupted lines
    
    del lines[i]

scores = []
closers = [')', ']', '}', '>']

for line in lines:
    
    closing_seq = find_closing_seq(line)
    
    score = 0
    
    for i in closing_seq:
        
        score *= 5
        score += closers.index(i) + 1
    
    scores.append(score)
    
scores = sorted(scores)
print(scores[len(scores)//2])


# %%
