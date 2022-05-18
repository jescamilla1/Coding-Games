import random
from queue import Queue 
from colorama import Fore 

class Board:
    def __init__(self, board_size, num_bombs):
        self.board_size = board_size
        self.num_bombs = num_bombs
        self.flags_placed = 0
        self.bomb_locations = set()
        self.flags = set()

        self.cover = self.create_cover_field()
        self.board = self.create_new_board()
        
        

    def create_cover_field(self):
        cover = [["#" for _ in range(self.board_size)] for _ in range (self.board_size)]
        return cover

    def create_new_board(self):
        board = [[0 for _ in range(self.board_size)] for _ in range (self.board_size)]

        # create bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            bomb = (random.randint(0, self.board_size - 1),random.randint(0,self.board_size - 1)) # create tuple of bomb location
            
            if bomb not in self.bomb_locations:
                self.bomb_locations.add(bomb)
                bombs_planted += 1

        # place bombs onto board
        for bomb in self.bomb_locations:
            bomb_row = bomb[0]
            bomb_col = bomb[1]

            board[bomb_row][bomb_col] = "*"

            # use neighbors for range 
            # neighbors do not include bombs
            bomb_neighbors = self.get_neighbors(board,bomb_row, bomb_col)
            for location in bomb_neighbors:
                row = location[0]
                col = location[1]
                board = self.update_bomb_range(board, row, col)


        return board

    def get_neighbors(self,temp_board, bomb_row, bomb_col):
        # returns list of neighbors not including those with bombs
        bomb_neighbors = set()
        # boundaries
        MAX_RIGHT = self.board_size - 1
        MAX_LEFT = 0
        MAX_UP = 0
        MAX_DOWN = self.board_size - 1

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                ROW = bomb_row + i
                COL = bomb_col + j
                # check if within range
                if MAX_UP <= ROW <= MAX_DOWN and MAX_LEFT <= COL <= MAX_RIGHT:
                    #cannot access board because it is in process of being created
                    # board calls make board, make board calls get_neighbors, get_neightbors wants to access board, but board has not been returned at all
                    # TODO: have the functions be seperate and not rely on echother 
                    if temp_board[ROW][COL] != '*':
                        bomb_neighbors.add((ROW,COL)) 
        return bomb_neighbors

    def update_bomb_range(self, board, row, col):
        board[row][col] += 1
        return board
    
    def uncover_from_position(self,row,col):
        # uncover bomb then return cover to display updated board and false for not safe
        if self.board[row][col] == "*":
            self.cover[row][col] = self.board[row][col]
            return False

        if self.cover[row][col] == "&":
            # must remove flag before revealing
            print("Invalid Move! Remove Flag")
            return True
        q = Queue()
        q.put((row,col))
        visited = set()

        while not q.empty():
            current = q.get()
            current_row = current[0]
            current_col = current[1]

            neighbors = self.get_neighbors(self.board, current_row,current_col)

            for location in neighbors:
                if location in visited or location in self.flags:
                    continue
                loc_row = location[0]
                loc_col = location[1]

                value = self.board[loc_row][loc_col]

                self.cover[loc_row][loc_col] = value # reveal position in cover 
                if value == 0:
                    q.put(location)
                visited.add(location)

        return True
    
    def display_board(self):
        print()
        for r in range(self.board_size):
            for c in range(self.board_size):
                if isinstance(self.cover[r][c], int):
                    print(Fore.BLUE + str(self.cover[r][c]) + Fore.RESET, end=" ")
                elif self.cover[r][c] == "#":
                    print(Fore.GREEN + str(self.cover[r][c]) + Fore.RESET, end=" ")
                elif self.cover[r][c] == "*":
                    print(Fore.RED + str(self.cover[r][c]) + Fore.RESET, end=" ")
                elif self.cover[r][c] == "&":
                    print(Fore.LIGHTRED_EX + str(self.cover[r][c]) + Fore.RESET, end=" ")
                else:
                    print(str(self.cover[r][c]), end=" ")
            print()
        print()

    def place_flag(self, row, col):
        # insert flag if available
        if 0 <= self.flags_placed <= 10:
            if self.cover[row][col] == "#":
                self.cover[row][col] = "&"
                self.flags.add((row,col))
                self.flags_placed += 1
                return True
        return False
    
    def remove_flag(self,row,col):
        # remove flag
        if self.cover[row][col] == "&":
            self.cover[row][col] = "#"
            self.flags.remove((row,col))
            self.flags_placed -= 1
            return True
        return False

    def check_win(self):
        # win if 10 uncovered spots and 10 bombs
        uncovered = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.cover[i][j] == "#" or self.cover[i][j] == "&":
                    uncovered += 1
        if uncovered == len(self.bomb_locations):
            return True
        return False
# play the game
def play(board_size=10, num_bombs=10):
    while True:
        board = Board(board_size, num_bombs)

        
        safe = True
        while safe:
            board.display_board()

            # ask for next move
            print("Moves:")
            choice = int(input("1. Dig\n2. Place Flag\n3. Remove Flag\nEnter Choice: "))
            while choice not in [1,2,3]:
                print("Invalid Move!")
                choice = int(input("1. Reveal location\n2. Insert Flag\n3. Remove Flag\nEnter choice: "))

            # enter coordinate
            row, col = int(input("Enter Row: ")), int(input("Enter Col: "))

            while not (0 <= row <= board_size-1) and not (0 <= col <= board_size):
                print("Invalid Location!")
                row, col = int(input("Enter Row: ")), int(input("Enter Col: "))

            # call appropriate functions for move
            if choice == 1:
                safe = board.uncover_from_position(row,col)
                if not safe:
                    print("You Lost. RIP")
                    continue
            elif choice == 2:
                flag_placed = board.place_flag(row, col)
                if not flag_placed:
                    print("Flag Not Placed")
                    continue
            elif choice == 3:
                flag_removed = board.remove_flag(row, col)
                if not flag_removed:
                    print("Flag Not Removed")
                    continue

            if board.check_win():
                print("You Win. Great work")
                break

        board.display_board()
        choice = int(input("Do you want to continue: 1. yes 2. no: "))
        if choice == 2:
            print("thank you for playing")
            break;
        else:
            print("here we go again")
            continue;
if __name__=='__main__':
    play()
