def print_board(board):
    for row in range(1, 6):
        for day in range(1, 8):
            for pos in range(1, 4):
                slot = grid_to_index((day, row, pos))
                print("%3d"%board[slot], end = "")
                
                if pos == 3: 
                    print("   ", end = "")
                    if day == 7: print()
    print('\n')

def empty_intersection(A, B):
    for a in A:
        if a in B:
            return False
    return True

def custom_divmod(n, d):
    a, b = divmod(n, d)
    if b == 0: return (a - 1, d)
    return (a, b)

def index_to_grid(i):
    day, rem = custom_divmod(i, 15)
    row, pos = custom_divmod(rem, 3)
    return (day + 1, row + 1, pos)

def grid_to_index(grid):
    day, row, pos = grid[0], grid[1], grid[2]
    return 15*(day - 1) + 3*(row - 1) + pos

def neighbors(slot, board):
    day, row, pos = index_to_grid(slot)
    return [board[grid_to_index((day, row, j))] for j in range(1, 4) if j != pos]
    
def can_walk(slot, walker, board):
    day = index_to_grid(slot)[0]
    for slot1 in range(1, slot):
        if board[slot1] == walker:
            day1 = index_to_grid(slot1)[0]

            if day1 == day: return False

            if not empty_intersection(neighbors(slot, board), neighbors(slot1, board)):
                return False

    return True

def walker_limits(slot, board):
    starter = 4; ender = 15
    day, row, pos = index_tob_grid(slot)
    
    if pos == 1 and row in [1, 2, 3]: return (row, row)
    
    if row > 1 and pos == 1:
        starter = max(starter, board[grid_to_index((day, row - 1, 1))] + 1)
        
    if pos > 1:
        starter = max(starter, board[grid_to_index((day, row, pos - 1))] + 1)
    
    if row == 1 and pos == 2:
        starter = max(starter, board[grid_to_index((day - 1, 1, 2))] + 1)
        
    if pos != 3: ender = 12
        
    return (starter, ender)    

def place_from(slot, board):
    starter, ender = walker_limits(slot, board)
    for walker in range(starter, ender + 1):
        if can_walk(slot, walker, board):
            board[slot] = walker
            if slot == 105: 
                return board
            
            global iteration
            iteration += 1
            if iteration % interval == 0:
                print("Iteration = ", iteration)
                print_board(board)
                
            place_from(slot + 1, board[:])
                
Board = [0 for j in range(0, 106)]

Board[0] = None
for slot in range(1, 16): Board[slot] = slot

iteration = 1; interval = 50000
place_from(16, Board[:])