
measur = []
increases = []

with open(r'day_1\inputs.txt', 'r') as inp_file:
    
    for line in inp_file.readlines():
        
        measur.append(int(line.rstrip()))
        
for i in range(len(measur)):
    
    if i > 0:
        if measur[i] > measur[i-1]:
            increases.append('inc')
        else:
            increases.append('dec')
    else:
        increases.append('N/A')

print(increases.count('inc'))

sum_increases = []

for i in range(2, len(measur)-1):
    
    A = measur[i-2] + measur[i-1] + measur[i]
    B = measur[i-1] + measur[i] + measur[i+1]
    
    if A < B:
        sum_increases.append('inc')
    else:
        sum_increases.append('dec')
    
print(sum_increases.count('inc'))
