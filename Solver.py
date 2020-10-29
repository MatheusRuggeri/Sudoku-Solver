import BOARD
import copy

# Copy the board values to new variables (it will be used to print)
playing_board = copy.deepcopy(BOARD.file4)
start_board = copy.deepcopy(BOARD.file4)

def smart_solve(print_info):
    # Check for positions that accept just a single value
    change_board = False
    for i in range(0,9):
        for j in range(0,9):
            possible_values = []
            if (playing_board[i][j] == 0):
                for value in range(1,10):
                    if check_possibility(i, j, value) == True:
                        possible_values.append(value)
                    playing_board[i][j] = 0
                if len(possible_values) == 1:
                    playing_board[i][j] = possible_values[0]
                    change_board = True
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

def check_possibility(i0, j0, value):
    # Check all the lines to find a repetition in Column
    for i in range(0,9):
        # If it finds a repetition, just stop the function returning False
        if playing_board[i][j0] == value:
            return False
    # Check all the lines to find a repetition in Line
    for j in range(0,9):
        # If it finds a repetition, just stop the function returning False
        if playing_board[i0][j] == value:
            return False
    
    # Check the small squares (there are 9 small boxes in the game)
    iSquare = ((i0//3)*3)+1
    jSquare = ((j0//3)*3)+1
    # Compare with the 9 elements in the box to check any repetition
    for i in range(iSquare-1,iSquare+2):
        for j in range(jSquare-1,jSquare+2):
            if playing_board[i][j] == value:
                return False
    return True

def complete_board():
    for i in range(0,9):
        for j in range(0,9):
            if (playing_board[i][j] == 0):
                return False
    return True

def recursive_solve():
    # Loop in X and Y looking for a empty cell
    for x in range(0,9):
        for y in range(0,9):
            if playing_board[x][y] == 0:
                for value in range(1,10):
                    # If it is empty, tests a value and enter in this recursive function again
                    if check_possibility(x, y, value):
                        playing_board[x][y] = value
                        recursive_solve()
                        # When it is complete, the function will return without changing values
                        if complete_board():
                            return
                        # If it couldn't fill all the values, the last cell will be erased and return one level in recursivity
                        playing_board[x][y] = 0
                return

# Print the first Sudoku board, with empty spaces
print("The original game:")
sudoku_printer()

# Keep trying to use the Smart solver until it is not effective anymore
while smart_solve(0):
    pass

print("\n\nUsing an smart algorith to solve faster:")
sudoku_printer()

# Then uses brute force to solve
recursive_solve()

# Print the final result
print("\n\nUsing brute force:")
sudoku_printer()