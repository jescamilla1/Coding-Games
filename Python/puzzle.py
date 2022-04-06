import random
def intro():
    print("""
            8 PUZZLE

        Rules:
        use WASD to move empty tile around
        to win you must have all numbers in order
        empty tile 0 must be bottom right
          """)
def printBoard(board):
    for row in board:
        for i in row:
            print("[{}]".format(i), end="")
        print()
    print()
        
def checkWin(board):
    winning_board = [
         [1,2,3],
         [4,5,6],
         [7,8,0]
        ]
    
    if winning_board == board:
        return True
    return False
    
def generateBoard():
    values = [1,2,3,4,5,6,7,8,0]
    board = []
    
    random.shuffle(values)
    board = [
             values[0:3],
             values[3:6],
             values[6:9]
            ]
    return board

def moveBlank(board, dir):
    MAX_UP = 0
    MAX_DOWN = 2
    MAX_RIGHT = 2
    MAX_LEFT = 0
    
    def getIndex(board, value):
        for i,j in enumerate(board):
            if value in j:
                return (i,j.index(value))
            
    def swap(board, blank, dest):
        # blank and dest are tuples holding coordinate for board use
        temp = board[dest[0]][dest[1]]
        board[dest[0]][dest[1]] = board[blank[0]][blank[1]]
        board[blank[0]][blank[1]] = temp
        return board

    blank = getIndex(board, 0)
    
    if dir == 'w':
        if blank[0] - 1 >= MAX_UP:
            board = swap(board, blank, (blank[0]-1,blank[1]))
    elif dir == 's':
        if blank[0] + 1 <= MAX_DOWN:
            board = swap(board, blank, (blank[0]+1,blank[1]))
    elif dir == 'a':
        if blank[1] - 1 >= MAX_LEFT:
            board = swap(board, blank, (blank[0],blank[1]-1))
    elif dir == 'd':
        if blank[1] + 1 <= MAX_RIGHT:
            board = swap(board, blank, (blank[0], blank[1]+1))
    return board
        

    

intro()
moves = ['w','s','a','d']
board = generateBoard()

while True:
    printBoard(board)
    
    move = input("Enter movement [W] [A] [S] [D]: ").lower()
    while move not in moves:
        move = input("Enter move again: ").lower()
        
    board = moveBlank(board, move)
    
    if checkWin(board):
        print("You won!")
        break
        

    
    
    