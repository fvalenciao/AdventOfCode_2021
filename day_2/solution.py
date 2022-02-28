x_pos = 0
y_pos = 0
aim = 0

with open(r'day_2\input.txt', 'r') as inp_file:
    
    for line in inp_file.readlines():
        
        command = line.rstrip().split(" ")

        if command[0] == 'forward':
            
            x_pos += int(command[1])
            y_pos += aim * int(command[1])
            
        elif command[0] == 'down':
            
            aim += int(command[1])
            
        elif command[0] == 'up':
            
            aim -= int(command[1])
        
prod = x_pos * y_pos

print(prod)