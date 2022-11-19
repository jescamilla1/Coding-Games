import random
import os

def create_board():
    board = []
    for i in range (4):
        board.append([" ", " "," "," "])
    return board

def show_board(board):
    print("----2048----")
    for i in range(4):
        for j in range(4):
            print( "[" + board[i][j], end="]")
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

def slide():
    pass

b = create_board()
# show_board(b)

# add 2 tiles to begin the game
b = add_number(b)
b = add_number(b)

show_board(b)
b = rotate_board(b)
show_board(b)

# while True:
#     show_board(b)
#     b = add_number(b)

#     # ask for movement
#     dir = input("Enter Direction to move [A] [W] [S] [D]: ")


#     break
