# Part 5 Exercise 7
# Sudoku: check grid

def sudoku_grid_correct(sudoku: list):
    """ Takes a two dimensional array representing a sudoku grid 
        If all nine rows, columns, and 3x3 blocks contain each:
        Numbers 1 to 9 at most once
        Return True
        Return False if filled incorrectly """

    if row_correct(sudoku) != True:
        return False
    if column_correct(sudoku) != True:
        return False
    if block_correct(sudoku) != True:
        return False
    return True

def row_correct(sudoku: list):
    """ Takes a two dimensional array representing a sudoku grid
        An integer referring to a single row
        Returns true or false whether the row is filled in correctly """
    
    for r in range(9):
        row_list = []
        for num in sudoku[r]:
            if num > 0:
                if num in row_list:
                    return False
                row_list.append(num)
    return True   
    
def column_correct(sudoku: list):
    """ Takes a two dimensional array representing a sudoku grid
        An integer referring to a single column
        Returns true or false whether the column is filled in correctly """

    for c in range(9):
        column_list = []
        for row in range(9):
            if sudoku[row][c] > 0:
                if sudoku[row][c] in column_list:
                    return False
                column_list.append(sudoku[row][c])
    return True


def block_correct(sudoku: list):
    """ Takes a two dimensional array representing a sudoku grid
        Returns true or false whether the 3x3 block is filled in correctly
        The 3x3 indexes begin at (0,0) and increase by increments of three: 
        (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6) """
    
    
    row_no = 0
    for rows in range(3):
        column_no = 0
        for columns in range(3):
            block_list = []
            for r in range(row_no, row_no+3):
                for c in range(column_no, column_no+3):
                    num = sudoku[r][c]
                    if num > 0 and num in block_list:
                        return False
                    block_list.append(num)
            column_no += 3
        row_no += 3

    return True