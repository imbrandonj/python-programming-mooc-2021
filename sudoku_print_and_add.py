# Part 5 Exercise 10
# Sudoku: print out the grid and add a number

def print_sudoku(sudoku: list):
    """ Takes a two dimensional array representing a sudoku grid
        Prints out the grid formatted as a sudoku grid
        The 0s of the grid are empty slots and should be represented by
        An underscore _ """

    gridblock_row_index = 0
    for row in sudoku:
        item_index = 0
        for i in range(9):
            # future you reading this:
            # thank you for coming back to old code for reoptimization
            # the conditions are because the problem inputs a sudoku list of 0s
            # appends items to the list and requests a reprint
            # this function runs through twice
            # thus reformatting the sudoku puzzle twice can easily add extra spaces (doubles essentially)
            # this code can be optimized, I am sure of it, perhaps with a different print() function, a print of each item
            # however, as is, the code runs as desired

            if row[item_index] != 0 and row[item_index] != '_ ' and row[item_index] != '_' and (i == 2 or i == 5 or i == 8):
                row[item_index] = f"{row[item_index]} "
            
            elif row[item_index] != 0:
                row[item_index] = f"{row[item_index]}"

            elif row[item_index] == 0:
                row[item_index] = '_'
                if i == 2 or i == 5 or i == 8:
                    row[item_index] = '_ '

            item_index += 1

        print(*row, sep=" ")

        if gridblock_row_index == 2 or gridblock_row_index == 5 or gridblock_row_index == 8:
            print()
        gridblock_row_index +=1

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    """ Takes a two dimensional array representing a sudoku grid
        Takes two integers referring to the row and column index
        Adds the number argument to the grid location """

    sudoku[row_no][column_no] = number