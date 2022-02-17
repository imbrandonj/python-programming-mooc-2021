# Part 5 Exercise 5
# Sudoku: check column

def column_correct(sudoku: list, column_no: int):
    """ Takes a two dimensional array representing a sudoku grid
        An integer referring to a single column
        Returns true or false whether the column is filled in correctly """
    
    column_list = []

    for row in range(9):
        if sudoku[row][column_no] == 0:
            continue
        elif sudoku[row][column_no] not in column_list:
            num = sudoku[row][column_no]
            column_list.append(num)
        else:
            return False

    return True