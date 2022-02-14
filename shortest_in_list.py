# Part 4 Exercise 30
# The shortest in the list

def shortest(string_list):
    ''' Takes a list of strings
        Returns the length of the shortest string '''
    
    shortest = 10000
    return_string = " "

    for i in string_list:
        if len(i) < shortest:
            shortest = len(i)
            return_string = i
    
    return return_string