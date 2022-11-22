import random
import os

"""
https://www.baeldung.com/cs/2048-algorithm
http://ovolve.github.io/2048-AI/
"""

def create_board():
    board = []
    for i in range (4):
        board.append([0, 0,0,0]) # turn into int array
    return board

def show_board(board):
    print("----2048----")
    for i in range(4):
        for j in range(4):
            print( "[{out}".format(out = " " if board[i][j] == 0 else str(board[i][j])) , end="]") # print space if 0 else print the string of the num
        print()

def add_number(board):
    # generate tile
    tile = random.choice([2,4])

    # add tile to board
    pos = (random.randint(0,3) , random.randint(0,3))

    # ensure position is valid
    while board[pos[0]][pos[1]] != " ":
        pos = (random.randint(0,3) , random.randint(0,3))

    board[pos[0]][pos[1]] = str(tile)

    return board

def rotate_board(board):
    N = 4
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):
            # store current cell in temp variable
            temp = board[x][y]
            # move values from right to top
            board[x][y] = board[y][N-1-x]
            # move values from bottom to right
            board[y][N-1-x] = board[N-1-x][N-1-y]
            # move values from left to bottom
            board[N-1-x][N-1-y] = board[N-1-y][x]
            # assign temp to left
            board[N-1-y][x] = temp
    return board

def slide(board):
    # for row in board:
    #     for col in board: 
    #         pass
            
    pass
"""
code to find all non zero values
board = [[0,0,0,0],[1,2,0,0], [0,3,0,0], [1,0,0,1]]

values = []

for idx, val in enumerate(board):
    for jdx, val2 in enumerate(val):
        if val2 != 0:
            print(idx-1,jdx, val)
"""
"""
    recursion swap values

    base if val[idx] == 2 and step + 1 != 0
        swap
    if val[idx] == 2 and idx + 1 == 0
        

"""

b = create_board()
show_board(b)

# add 2 tiles to begin the game
b = add_number(b)
b = add_number(b)

show_board(b)

# show_board(b)
# b = rotate_board(b)
# show_board(b)

# while True:
#     show_board(b)
#     b = add_number(b)

#     # ask for movement
#     dir = input("Enter Direction to move [A] [W] [S] [D]: ")


#     break
