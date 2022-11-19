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
            print( "|" + board[i][j], end="|")
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

def move_left(board, ):

    pass


b = create_board()
# show_board(b)

# add 2 tiles to begin the game
b = add_number(b)
b = add_number(b)

while True:
    show_board(b)
    b = add_number(b)

    # ask for movement

    break
