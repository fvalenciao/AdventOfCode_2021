import numpy as np

inps = []

with open(r'day_3\input.txt', 'r') as inp_file:
    
    for line in inp_file.readlines():
        
        inps.append(line.rstrip())

ones = np.zeros(len(inps[0]))
zeros = np.zeros(len(inps[0]))

for inp in inps:
    
    for i in range(len(inp)):
        
        if inp[i] == '1':
            ones[i] += 1
            
        elif inp[i] == '0':
            zeros[i] += 1

most_common = []
least_common = []

for i in range(len(ones)):
    
    if ones[i] > zeros[i]:
        most_common.append('1')
        least_common.append('0')
        
    else:
        most_common.append('0')
        least_common.append('1')
        
gamma_bin = ''.join(most_common)
gamma_dec = int(gamma_bin,2)

epsilon_bin = ''.join(least_common)
epsilon_dec = int(epsilon_bin,2)

power_consum = epsilon_dec * gamma_dec

print(power_consum)