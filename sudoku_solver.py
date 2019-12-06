import sys

def can_allocate(grid, number, row, col):

    # Check if number already appeared in row
    for i in range(9):
        if grid[row][i] == number:
            return False
    
    # Check if number already appeared in col
    for j in range(9):
        if grid[j][col] == number:
            return False

    # Check if number appeared in the 3x3 block corresponding to number position.
    row = row - row%3
    col = col - col%3

    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == number:
                return False

    return True


def find_empty_position(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def solve_sudoku(grid):

    l=[0,0]

    if(not(find_empty_position(grid, l))):
        return True

    row = l[0]
    col = l[1]

    for number in range(1,10):
        if can_allocate(grid, number, row, col):
            #print(row, col, number, True)
            grid[row][col] = number

            #print(True)
            if(solve_sudoku(grid)):
                return True

            #Empty the position as this choice couldn't solve it.
            grid[row][col] = 0

    #print(False);
    return False

if __name__ == "__main__":

    grid = [[ 0 for x in range(9) ] for y in range(9) ]

    grid=[[0,0,0,0,0,3,9,0,1],
          [4,0,0,2,0,5,8,3,0],
          [0,6,0,8,0,0,2,0,0],
          [0,0,8,0,5,0,0,9,0],
          [0,2,0,0,4,0,0,5,0],
          [0,3,0,0,8,0,6,0,0],
          [0,0,3,0,0,1,0,8,0],
          [0,1,4,6,0,8,0,0,2],
          [8,0,6,5,0,0,0,0,0]]

    for row in range(9):
        print(grid[row])

    if(solve_sudoku(grid)):
        print("\n\n\nSolved !!!\n")
        for row in range(9):
            print(grid[row])
    else:
        print("\n\n\nCan not solve.\n")
