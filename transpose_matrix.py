# Part 5 Exercise 13
# Transpose a matrix

def transpose(matrix: list):
    """ Takes a two dimensional integer array i.e. a matrix
        Flips the matrix over its diagonal
        Columns become rows, rows become columns """

    copy_list = []
    N = len(matrix)
    
    for i in range(N):
        copy_list.append([])
    
    for row in matrix:
        row_count = 0
        for column in row:
            copy_list[row_count].append(column)
            row_count += 1

    matrix[:] = copy_list[:]

