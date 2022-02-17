# Part 5 Exercise 6
# Sudoku: check block

def block_correct(sudoku: list, row_no: int, column_no: int):
    """ Takes a two dimensional array representing a sudoku grid
        And two integers referring to the row and column of a single square
        Returns true or false whether the 3x3 block is filled in correctly
        The 3x3 block's top left begins with sudoku[row_no][column_no] """
    
    block_list = []

    for r in range(row_no, row_no+3):
        for c in range(column_no, column_no+3):
            num = sudoku[r][c]
            if num > 0 and num in block_list:
                return False
            block_list.append(num)

    return True