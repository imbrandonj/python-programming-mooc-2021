# Part 5 Exercise 23
# Create a tuple

def create_tuple(x: int, y: int, z: int):
    """ Takes three integers
        Creates and returns a tuple
        First index should contain the smallest integer
        Second should contain the largest integer
        Third is the sum of all three arguments """
    
    stored = [x, y, z]
    stored.sort()
    sum = 0

    for value in stored:
        sum += value

    print(stored)
    my_tuple = (stored[0], stored[2], sum)

    return my_tuple
    