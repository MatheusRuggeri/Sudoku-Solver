import BOARD
import time
import numpy as np

playing_board = BOARD.file

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
            if playing_board[i][j] == value and (i0 != i and j0 != j):
                return False
    return True

def solve(recursive):
    print(recursive)
    print("")
    print(np.matrix(playing_board))
    time.sleep(1)
    for x in range(0,9):
        for y in range(0,9):
            if playing_board[x][y] == 0:
                for value in range(1,10):
                    print(value, end="-")
                    print(check_possibility(x, y, value))
                    if check_possibility(x, y, value):
                        playing_board[x][y] = value
                        solve(recursive+1)
                        playing_board[x][y] = 0

playing_board[1][0] = 7
solve(1)