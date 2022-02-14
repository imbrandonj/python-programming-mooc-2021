# Part 4 Exercise 27
# The sum of lists

def list_sum(list_one, list_two):
    ''' Takes two lists as integers
        Returns a new list with the sum of two lists
        At each original index '''

    new_list = []
    count = 0

    for i in list_one:
        new_list.append(i)
    
    for i in list_two:
        new_list[count] += i
        count += 1
    
    return new_list