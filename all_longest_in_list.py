# Part 4 Exercise 31
# All the longest in the list

def all_the_longest(string_list):
    ''' Takes a list of strings
        Returns a new list with the longest string
        If two strings are equally long, return both strings in list '''
    
    new_string_list = []
    longest_string = 0

    for i in string_list:
        if len(i) == longest_string:
            new_string_list.append(i)

        elif len(i) > longest_string:
            longest_string = len(i)
            new_string_list = []
            new_string_list.append(i)
    
    return new_string_list