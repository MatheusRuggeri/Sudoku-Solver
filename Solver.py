import BOARD
import time
import numpy as np
import copy

playing_board = copy.deepcopy(BOARD.file3)
start_board = copy.deepcopy(BOARD.file3)

def smart_solve(print_info):
    # Check for positions that accept just a single value
    change_board = False
    for i in range(0,9):
        for j in range(0,9):
            possible_values = []
            if (playing_board[i][j] == 0):
                for n in range(1,10):
                    playing_board[i][j] = n
                    if valid_board(print_info) == True:
                        possible_values.append(n)
                    playing_board[i][j] = 0
                if len(possible_values) == 1:
                    playing_board[i][j] = possible_values[0]
                    change_board = True
    return change_board
            
def brute_force_solve(print_info): 
    change_board = False       
    for i in range(0,9):
        for j in range(0,9):
            if (playing_board[i][j] == 0):
                for n in range(1,10):
                    if print_info:
                        print(n, end=" - ")
                    playing_board[i][j] = n
                    if valid_board(print_info) == False:
                        playing_board[i][j] = 0
                    else:
                        change_board = True
                        break
    return change_board

def sudoku_printer():
    print("")
    for i in range(0,9):
        if (i % 3 == 0):
            print("| ----- | ----- | ----- |")
        for j in range(0,9):
            if (j % 3 == 0):
                print("| ", end="")
            if (playing_board[i][j] != 0):
                if (playing_board[i][j] == start_board[i][j]):
                    print('\x1b[6;30;42m' + str(playing_board[i][j]) + '\x1b[0m', end=" ")
                else:  
                    print(playing_board[i][j], end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("| ----- | ----- | ----- |")

def valid_board(print_info):
    # Check all the lines to find a repetition in Column
    for j in range(0,9):
        # Set the comparision value and loop through the matrix comparing them
        for i_compare in range(0,9):
            repetition = 0
            for i in range(0,9):
                # Add the condition (in Python True = 1 and False = 0) 
                repetition += (playing_board[i_compare][j] != 0 and playing_board[i_compare][j] == playing_board[i][j])
            if repetition > 1:
                if print_info:
                    print("Invalid game, same number in column")
                return False
            
    # Check all the columns to find a repetition in Lines
    for i in range(0,9):
        for j_compare in range(0,9):
            repetition = 0
            for j in range(0,9):
                repetition += (playing_board[i][j_compare] != 0 and playing_board[i][j_compare] == playing_board[i][j])
            if repetition > 1:
                if print_info:
                    print("Invalid game, same number in line")
                return False

    # Check the small squares (box)
    # Select the box (there are 9 small boxes in the game)
    for i_box in range(0,3):
        for j_box in range(0,3):
            # Select the value to compare
            for i_compare in range(3*i_box,3*i_box+3):
                for j_compare in range(3*j_box,3*j_box+3):
                    repetition = 0
                    # Compare with the 9 elements in the box to check any repetition
                    for i in range(3*i_box,3*i_box+3):
                        for j in range(3*j_box,3*j_box+3):
                            repetition += (playing_board[i_compare][j_compare] != 0 and playing_board[i_compare][j_compare] == playing_board[i][j])
                    if repetition > 1:
                        if print_info:
                            print("Invalid game, same number in box")
                        return False                    
    if print_info:
        print("Valid game")
    return True


def check_possibility(i0, j0, value):
    for i in range(0,9):
        if playing_board[i][j0] == value:
            return False
    for j in range(0,9):
        if playing_board[i0][j] == value:
            return False
    
    iSquare = ((i0//3)*3)+1
    jSquare = ((j0//3)*3)+1
    for i in range(iSquare-1,iSquare+2):
        for j in range(jSquare-1,jSquare+2):
            if playing_board[i][j] == value:
                return False
    return True

def solve(recursive):
    print(recursive)
    sudoku_printer()
    time.sleep(1)
    for x in range(0,9):
        for y in range(0,9):
            if playing_board[x][y] == 0:
                for value in range(1,10):
                    if check_possibility(x, y, value):
                        playing_board[x][y] = value
                        solve(recursive+1)
                        playing_board[x][y] = 0
                    return

solve(1)


# Print the first Sudoku board, with empty spaces
sudoku_printer()

# Keep trying to use the Smart solver until it is not effective anymore
while smart_solve(0):
    pass

# Then uses brute force to solve
while brute_force_solve(0):
    pass

# Print the final result
sudoku_printer()