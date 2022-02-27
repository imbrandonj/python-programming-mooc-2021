# Part 6 Exercise 3
# Matrix
# Optimize this by adding another function that reads the file

def matrix_sum():
    """ Reads the file 'matrix.txt' 
        Returns the sum of the elements """
    sum = 0
    with open('matrix.txt') as object_file:
        for line in object_file:
            line = line.split(',')
            for value in line:
                value = int(value)
                sum += value
    return sum

def matrix_max():
    """ Reads the file 'matrix.txt'
        Returns the element of the greatest value """

    greatest_value = -9999
    with open('matrix.txt') as object_file:
        for line in object_file:
            line = line.split(',')
            for value in line:
                value = int(value)
                if value > greatest_value:
                    greatest_value = value
    return greatest_value

def row_sums():
    """ Reads the file 'matrix.txt'
        Returns a list 
        Each index contains the sum of the row """
    
    sum_list = []

    with open('matrix.txt') as object_file:
        for line in object_file:
            line_value = 0
            line = line.split(',')
            for value in line:
                value = int(value)
                line_value += value
            sum_list.append(line_value)
    return sum_list
