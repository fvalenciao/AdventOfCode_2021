
def get_rate(oxy_inps,opt):
    
    index = 0
    
    while index < len(oxy_inps[0]) and len(oxy_inps) > 1:
        
        ones = 0
        zeros = 0

        for inp in oxy_inps:
                
            if inp[index] == '1':
                ones += 1
                
            elif inp[index] == '0':
                zeros += 1

        if opt == 1:
            if ones >= zeros:
                
                for i in range(len(oxy_inps)-1,-1,-1):
                    
                    if oxy_inps[i][index] == '0':
                        
                        del oxy_inps[i]
                        
            elif zeros > ones:
                
                for i in range(len(oxy_inps)-1,-1,-1):
                    
                    if oxy_inps[i][index] == '1':
                        
                        del oxy_inps[i]
        elif opt == 2:
            if ones >= zeros:
                
                for i in range(len(oxy_inps)-1,-1,-1):
                    
                    if oxy_inps[i][index] == '1':
                        
                        del oxy_inps[i]
                        
            elif zeros > ones:
                
                for i in range(len(oxy_inps)-1,-1,-1):
                    
                    if oxy_inps[i][index] == '0':
                        
                        del oxy_inps[i]
                
        index += 1
            
    return(oxy_inps) 

inps = []

with open(r'day_3\input.txt', 'r') as inp_file:
    
    for line in inp_file.readlines():
        
        inps.append(line.rstrip())
        
oxy_rate_inps = inps.copy()
co2_rate_inps = inps.copy()

oxy_rate_bin = get_rate(oxy_rate_inps,1)
co2_rate_bin = get_rate(co2_rate_inps,2)               

oxy_rate_dec = int(oxy_rate_bin[0],2)
co2_rate_dec = int(co2_rate_bin[0],2)

result = oxy_rate_dec * co2_rate_dec
print(result)