# The Battleship game
# square (10x10  cells) identified  by  letters  and  numbers.  
# player  plays  against  the  computer.  
# 1) the computer secretly places one (hidden) ship size 3 on the board 
# - random location, random orientation (horizontal or vertical) 
# -> goal is to "destroy" the ship with the least number of guesses.
# the player takes turns entering a coordinate
# hit -> the cell = 'X', miss = # 
# if the ship is destroyed, the player wins.

import random  # import the random module 
import os  # import the os module

ship_size = 7  # constant variable for the size of the ship 
dimension = 10  # constant variable for the size of the board (square) 

# Create Board DIMENSION X DIMENSION 
columns = []
for i in range(dimension):
    columns.append(chr(65+i))
# print("columns", columns)

rows = []
for i in range(dimension):
    rows.append(i)
# print("rows", rows)

board = []  # create an empty list
for i in range(dimension):  # loop through the rows
    board.append([])  # add an empty list to the board
    for j in range(dimension):  # loop through the columns
        board[i].append("0")  # add a # to the board

#for i in range(dimension):
#    print(rows[i], board[i])
# print(board)


# randomly choose the orientation of the ship
# 0 = horizontal, 1 = vertical
orientation = random.randint(0, 1)

# randomly place the ship. Use random.randint() to draw numbers 
if orientation == 0:
    rand_row = random.randint(0, dimension-1)
    rand_col = random.randint(0, dimension-ship_size)
else:
    rand_row = random.randint(0, dimension-ship_size)
    rand_col = random.randint(0, dimension-1)

# place the ship on the board
if orientation == 0:
    for i in range(ship_size):
        board[rand_row][rand_col+i] = "S"
else:
    for i in range(ship_size):
        board[rand_row+i][rand_col] = "S"

# print the board matrix
# for i in range(dimension):
#     print(rows[i], board[i])
# print(board)


# display the board

row_labels = "   "
for letter in columns:
    row_labels += letter + "   "
grid_row = " " + "+---" * 10 + "+"

def create_visible_row(row_number):
    field_row = str(row_number) + "|"
    for i in range(dimension):
        if board[row_number][i] == "#":
            field_row += " # |"
        elif board[row_number][i] == "X":
            field_row += " X |"
        else:
            field_row += "   |"
    return field_row

def create_hidden_row(row_number):
    field_row = str(row_number) + "|"
    field_row += "   |" * 10
    return field_row

def create_game_board():
    game_board = ["\n", row_labels]
    for i in range(dimension):
        game_board.append(grid_row)
        game_board.append(create_visible_row(i))
    game_board.append(grid_row)
    game_board.append("\n")
    return game_board

game_board = create_game_board()

def print_game_board(input_board):
    for line in input_board:
        print(line)

#print_game_board(game_board)

# Ask for user guess
hits = 0
tries = 0
guesses = []

def update_board(guesses):
    global hits
    for guess in guesses:
        row = int(guess[1])
        col = ord(guess[0]) - 65
        if board[row][col] == "S":
            board[row][col] = "X"
            hits += 1
        elif board[row][col] == "0":
            board[row][col] = "#"

print("\n\n\nWelcome to Battleship! \n\ntry to sink my ship in the least amount of tries. \nGood luck!")
print_game_board(game_board)

while hits < ship_size:
    print("\n Tries: ", tries, "Hits: ", hits, "\n")
    new_guess = input("Enter your guess: ")
    # print("length", len(new_guess), "first", type(new_guess[0].upper()), (new_guess[0].upper() in columns), "second", type(new_guess[1].upper()), (int(new_guess[1]) in rows))
    if (len(new_guess) == 2 and (new_guess[0].upper() in columns) and (int(new_guess[1]) in rows)):
        guesses.append(new_guess[0].upper() + new_guess[1])
    # print("Your guesses: ", guesses)
    update_board(guesses)
    game_board = create_game_board()
    print_game_board(game_board)
    tries += 1

print("You won!")

