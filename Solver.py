import BOARD
import time

playing_board = BOARD.file

def solve(print_info):
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
                        break

def sudoku_printer():
    print("")
    for i in range(0,9):
        if (i % 3 == 0):
            print("| ----- | ----- | ----- |")
        for j in range(0,9):
            if (j % 3 == 0):
                print("| ", end="")
            if (playing_board[i][j] != 0):
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

sudoku_printer()
solve(0)
sudoku_printer()