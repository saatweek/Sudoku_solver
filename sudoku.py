import numpy as np
backtracks = 0

#input
input = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def findNextCellToFill(grid):
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return i, j
    return -1,-1


def isValid(grid, x, y, n):
    for i in range(0, 9):
        if grid[i][y]==n:
            return False
    for i in range(0,9):
        if grid[x][i] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == n:
                return False
    return True
        
#solve
def solve(grid, x=0, y=0):
    global backtracks
    x, y = findNextCellToFill(grid)
    if x==-1:
        return True
    for n in range(1, 10):
        if isValid(grid, x, y, n):
            grid[x][y]=n
            if solve(grid, x, y):
                return True
            backtracks+=1
            grid[x][y]=0
    return False
#end of code
