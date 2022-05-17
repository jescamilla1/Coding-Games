from queue import Queue # for depth first search
import random
from colorama import Fore 

# declare globals
mines = []
flags = set() # use set() to differentiate from dict
SIZE = 10 # size of board and number of mines

def create_mine_field():
    board = []
    # creates board with all 0s 8x8
    # range does not include 8 therefore 0-7
    row = []
    for i in range(SIZE):
        for j in range(SIZE):
            row.append(0)
        board.append(row)
        row = []
        
    # creates list of mines
    global mines
    while len(mines) != 10:
        m = [random.randint(0, SIZE-1),random.randint(0,SIZE - 1)] # use 0-7 since randint includes 7
        if m in mines:
            continue
        mines.append(m)
            
    # place mines onto board
    for mine in mines:
        m_row = mine[0]
        m_col = mine[1]

        board[m_row][m_col] = "*"

        mine_neighbors = get_neighbors(board, m_row, m_col) # get neighbors of mines
        for n in mine_neighbors: # add to values of neighbors
            board = add_neighbor_val(board, n[0], n[1])
    
    return board

# returns board with updated value
def add_neighbor_val(board, row, col):
    # note: neighbors do not include pos of mines
    board[row][col] += 1     
    return board
    
def showBoard(board):
    # DIY output for visual
    print("  ", end =" ")
    for n in range(SIZE):
        print(n , end=" ")
    print("\n")
    for i in range(SIZE):
        print( i , end = "  ")
        for j in range(10):
            if isinstance(board[i][j], int): # check if board holds an int
                if board[i][j] == 1:
                    print(Fore.LIGHTCYAN_EX + str(board[i][j]) + Fore.RESET, end=" ")
                elif board[i][j] == 2:
                    print(Fore.BLUE + str(board[i][j]) + Fore.RESET, end=" ")
                elif board[i][j] == 3:
                    print(Fore.LIGHTMAGENTA_EX + str(board[i][j]) + Fore.RESET, end=" ")
                elif board[i][j] == 4:
                    print(Fore.LIGHTRED_EX + str(board[i][j]) + Fore.RESET, end=" ")
                else: 
                    print(board[i][j], end=" ")
            elif board[i][j] == "*":
                print(Fore.RED + str(board[i][j]) + Fore.RESET, end=" ")
            elif board[i][j] == "#":
                print(Fore.LIGHTGREEN_EX + str(board[i][j]) + Fore.RESET, end=" ")
            elif board[i][j] == "&":
                print(Fore.LIGHTYELLOW_EX + str(board[i][j]) + Fore.RESET, end=" ")
            else:
                print(board[i][j], end=" ")
        print()
    print()

def create_cover_field():
    # creates field using hashtags
    board = []

    row = []
    for i in range(10):
        for j in range(10):
            row.append('#')
        board.append(row)
        row = []
    return board


def uncover_from_position(board, cover, row, col):

    # uncover bomb then return cover to display updated board and false for not safe
    if board[row][col] == "*":
        cover[row][col] = board[row][col]
        return cover, False

    q = Queue()
    q.put((row,col))
    visited = set()

    while not q.empty():
        current = q.get()
        neighbors = get_neighbors(board, current[0], current[1])

        for n in neighbors:
            if n in visited or n in flags:
                continue
            value = board[n[0]][n[1]]
            cover[n[0]][n[1]] = value
            if value == 0:
                q.put(n)
            visited.add(n)
    return cover, True


def get_neighbors(board, row, col):
    # returns list of neighbors not including those with bombs
    neighbors = []

    MAX_RIGHT = 9
    MAX_LEFT = 0
    MAX_UP = 0
    MAX_DOWN = 9
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            # check if within range
            ROW = row + i
            COL = col + j
            if MAX_UP <= ROW <= MAX_DOWN and MAX_LEFT <= COL <= MAX_RIGHT:
                if board[ROW][COL] != '*':
                    neighbors.append((ROW,COL)) # if not mine add to neightbor
    return neighbors

def insert_flag(cover, row, col):
    # insert flag if available
    if 0 < len(flags) <= 10:
        if cover[row][col] == "#":
            cover[row][col] = "&"
            flags.add((row,col))
    return cover

def remove_flag(cover, row, col):
    # remove flag
    if cover[row][col] == "&":
        cover[row][col] = "#"
        flags.remove((row,col))
    return cover

def check_win(cover):
    # win if 10 uncovered spots and 10 bombs
    global mines
    uncovered = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if cover[i][j] == "#" or cover[i][j] == "&":
                uncovered += 1
    if uncovered == len(mines):
        return True
    return False

while True:
    # create board and place bombs
    mineField = create_mine_field()
    # showBoard(mineField)
    # print(mines)
    # create cover board that user will see
    coverField = create_cover_field()

    safe = True
    while safe:
        #showBoard(mineField)
        showBoard(coverField)

        choice = int(input("1. Reveal location\n2. Insert Flag\n3. Remove Flag\nEnter choice: "))
        while choice not in [1,2,3]:
            print("invalid input!")
            choice = int(input("1. Reveal location\n2. Insert Flag\n3. Remove Flag\nEnter choice: "))
        print()

        
        row, col = int(input("Enter Row: ")), int(input("Enter Col: "))
        print()
        while not (0 <= row <= 9) and not (0 <= col <= 9):
            print("invalid input!")
            row, col = int(input("Enter Row: ")), int(input("Enter Col: "))


        if choice == 1:
            coverField, safe = uncover_from_position(mineField, coverField, row, col)
        elif choice == 2:
            coverField = insert_flag(coverField, row, col)
        elif choice == 3:
            coverField = remove_flag(coverField, row, col)

        if not safe:
            showBoard(coverField)
            print("you lost")
            continue;
        if check_win(coverField):
            print("You Won")
            break;
    choice = int(print("Do you want to continue: 1. yes 2. no"))
    if choice == 2:
        print("thank you for playing")
        break;
    else:
        print("here we go again")
        continue;

