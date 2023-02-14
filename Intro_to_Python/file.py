import os
import time

os.system('clear') 

NUM_ROWS = 8
NUM_COLS = 8
board = []
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
        row_list.append('.')
        board.append(row_list)

NUM_ROWS = 8
NUM_COLS = 8
# board was created on previous slide
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(board[row][col], end = " ")
    print()

time.sleep(30)