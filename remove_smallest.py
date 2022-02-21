# Part 5 Exercise 9
# Remove the smallest

def remove_smallest(numbers: list):
    """ Takes a list of integers
        Removes the smallest item in the list
        Modifies the list with no return value
        List kept in same order """

    numbers.remove(sorted(numbers)[0])