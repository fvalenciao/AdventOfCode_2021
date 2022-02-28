# %%

inputs = []

def get_inps_list(inp_nums_):
    
    inp_nums = []
    for i in inp_nums_:
        
        letters = []
        
        for j in i:
            
            letters.append(j)
        
        inp_nums.append(letters)
    
    return inp_nums
    
with open('input.txt', 'r') as f:
    
    for line in f.readlines():
        
        inputs.append(line.rstrip().split('|'))
        
fixed_nums_list = []
for inp in inputs:
    
    inp_nums_ = inp[0].split(' ')
    inp_nums = get_inps_list(inp_nums_)
    
    try:
        inp_nums.remove([])
    except:
        pass
    
    out_nums_ = inp[1].split(' ')
    out_nums = get_inps_list(out_nums_)
    
    try:
        out_nums.remove([])
    except:
        pass
    
    five_digs = []
    six_digs = []
    
    for i in inp_nums:
        
        i = sorted(i)
        
        if len(i) == 2:
            one = i
            
        elif len(i) == 3:
            seven = i

        elif len(i) == 4:
            four = i
            
        elif len(i) == 5:
            five_digs.append(i)
        
        elif len(i) == 6:
            six_digs.append(i)
            
        elif len(i) == 7:
            eight = i

    # find a from difference between 1 and 7
    a = list(set(seven) - set(one))
    a = a[0]
    
    # find bd from difference between 4 and 1
    
    bd = list(set(four) - set(one))
    
    # 5 is the only five-digit with bd in it
    for i in five_digs:
        if bd[0] in i and bd[1] in i:
            five = i
    
    #d in all five-digits, b only in number 5
    five_digs.remove(five)
    
    for i in bd:
        
        if i in five_digs[0] and i in five_digs[1]:
            d = i
        else:
            b = i
    
    # zero = 8-d
    
    zero_ = list(set(eight) - set(d))
    
    # find c as it is in 1 but not in 5
    
    for i in one:
        if i not in five:
            c = i
    
        # find f from 1 as c is known
        else:
            f = i

    # find 9 as 5+c
    nine = sorted(five)
    nine.append(c)
    
    # find e as in 8 but not in 9
    
    for i in eight:
        
        if i not in nine:
            e = i
            
    for i in eight:
        
        if i != a and i != b and i != c and i != d and i != e and i != f:
            g = i
            
    two = [a, c, d, e, g]
    three = [a, c, d, f, g]
    six = [a, b, d, e, f, g]
    
    fixed_nums = [sorted(zero_), sorted(one), sorted(two), sorted(three), sorted(four), sorted(five), sorted(six), sorted(seven), sorted(eight), sorted(nine)]
    
    for out in out_nums:
        
        count = 0
        
        out = sorted(out)
        
        for i in fixed_nums:
            
            if out == i:
                
                fixed_nums_list.append(count)
                
            count += 1
        
total_1 = fixed_nums_list.count(1)
total_4 = fixed_nums_list.count(4)
total_7 = fixed_nums_list.count(7)
total_8 = fixed_nums_list.count(8)

total = total_1 + total_4 + total_7 + total_8

print(total)