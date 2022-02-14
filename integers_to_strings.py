# Part 4 Exercise 32
# Integers to strings

def formatted(float_list):
    ''' Takes a list of floating point numbers
        Returns a new list with floating point numbers as strings
        The floating points will be rounded to two decimal places '''

    new_list = []

    for i in float_list:
        float_string = f'{i:.2f}'
        new_list.append(float_string)

    return new_list