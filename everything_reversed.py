# Part 4 Exercise 33
# Everything reversed

def everything_reversed(string_list):
    ''' Takes a list of strings
        Returns new list with all items reversed, including reversed index'''

    reversed_list = []

    for i in string_list:
        i = i[::-1]
        reversed_list.append(i)

    reversed_list.reverse()
    return reversed_list