# Part 5 Exercise 4
# Sudoku: check row

def row_correct(sudoku: list, row_no: int):
    """ Takes a two dimensional array representing a sudoku grid
        An integer referring to a single row
        Returns true or false whether the row is filled in correctly """
    
    row_list = []

    for num in sudoku[row_no]:
        if num == 0:
            continue
        elif num in row_list:
            return False
        else:
            row_list.append(num)
    
    return True
