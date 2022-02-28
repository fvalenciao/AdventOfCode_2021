import numpy as np

inp_line = True # read first line of of file as draw numbers
board_count = -1 # controlls index in boards list filling
boards = [] # each position contains a numpy array with a bingo board

with open('input.txt','r') as inp_file:
    
    line_num = 0
    for line in inp_file.readlines():
        
        if inp_line == True:
            
            draw_nums = line.split(',')
            inp_line = False
            continue
        
        if ' ' not in line:     # empty line between boards
            
            if board_count >= 0:
                boards.append(board)
                
            board_count += 1
            board = np.zeros([5,5]) # create new board
            board_row = 0   # reset board row counter
            continue
        
        else:
            row_nums = line.split(' ')
            
            try:
                row_nums.remove('')
                board[board_row, :] = row_nums
            except:
                board[board_row, :] = row_nums
            
            board_row += 1
        
        line_num += 1
   
matches = [] # list of binary matrices (one matrix per board)

for i in range(len(boards)):
    matches.append(np.zeros([5,5]))
    
bingo = False

for num in draw_nums:
    
    for i in range(len(boards)):
        
        ind = np.where(boards[i] == int(num)) # returns position of draw number in board i
                                         # if num is not in the board, it still won't break the program
        
        matches[i][ind] = 1
        
        if np.sum(matches[i][ind[0],:]) == 5 or np.sum(matches[i][:,ind[1]]) == 5:
            
            bingo = True
            print('BINGO!\n')
            print(f'Board {i} is the winner')
            
            winner = boards[i]
            win_num = int(num)
            
            break
        
    if bingo == True:
        break


unmarked_nums = np.where(matches[i] == 0) # positions of unmarked numbers in winning board

unmarked_sum = np.sum(winner[unmarked_nums]) #sum of all unmarked numbers

result = unmarked_sum * win_num

print(result)
        
        
    