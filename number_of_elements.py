# Part 5 Exercise 2
# Number of matching elements

def count_matching_elements(my_matrix: list, element: int):
    ''' Takes a list of lists
        Counts and returns the quantity of given element '''

    match_element = element
    count = 0

    for row in my_matrix:
        for i in row:
            if i == match_element:
                count += 1
        
    return count