#Sidney & Kenyatta Battleship
import random

def print_board(board):
    for row in board:
        print(" ".join(row))

###we tried to allow for letting the user choose between random and deliberate placement, but we couldn't get it done in time and commented it out####

def makelo(board):
    #choice = (input("Would you like to place your ships?: y/n: "))
    #if choice == ("n"):
        return random.randint(1, len(board)), random.randint(1, len(board[0]))
    #if choice == ("y"):
        #inputrow=int(input("row: "))
        #inputcol=int(input("col: "))
        #if (inputrow > grid) and (inputcol > grid):
            #print("enter valid inputs")

        
def inputthatthang(grid):
    while(True):
        try:
            GuessRow = eval(input("Take a shot, Guess Row: "))
            GuessColumn = eval(input("Now Guess Column: "))
            
            if GuessColumn <= grid and GuessRow <= grid:
                return GuessRow-1, GuessColumn-1
            else:
                print("Seems like you're aiming for failure. Try again...\n")
        except: 
            print("Aim inside the grid.\n")
        
print("Let's Play Battleship! Your enemy is on water. They're coming at you and FAST! Do your best to destroy their fleet. You have 6 chances.")

grid = int(input("Choose Your Grid Size:"))

board = []
for i in range(grid):
    board.append(["O"] * grid)



RowRowRow, ColColCol = makelo(board) 


for LAUNCH in range(6):

    if LAUNCH == 5:
        print("Game Over.")
        board[GuessRow][GuessColumn] = "X"
        break
    
    print("Launch", LAUNCH + 1,"!")
    print_board(board)
    
    GuessRow, GuessColumn = inputthatthang(grid)

    if GuessRow + 1 == RowRowRow and GuessColumn + 1 == ColColCol:
        print("\nWow! You sunk an enemy ship!")
        board[GuessRow][GuessColumn] = "X"
        print_board(board)
        print("")
        break
    
    else:
        if board[GuessRow][GuessColumn] == "-":
            print("\n YOU ALREADY GUESSED THAT :|.")
            print(" ")
        else:
            print("\n Come on man! You MISSED!")
            board[GuessRow][GuessColumn] = "-"