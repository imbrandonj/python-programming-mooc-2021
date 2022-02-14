# Part 4 Exercise 28
# Distinct numbers

def distinct_numbers(int_list):
    ''' Takes a list of integers
        Returns a new list containing the original integers
        Sorted in order of magnitude '''

    new_list = []

    for i in int_list:
        if i not in new_list:
            new_list.append(i)
    
    new_list.sort()
    return new_list