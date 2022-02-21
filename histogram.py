# Part 5 Exercise 16
# Histogram

def histogram(string: str):
    """ Takes a string
        Prints out a histogram representing
        the number of times each letter occurs in the string
        Each occurrence is represented by an asterisk * """

    histo_dict = {}

    for char in string:
        if char not in histo_dict:
            histo_dict[char] = "*"

        elif char in histo_dict:
            histo_dict[char] += "*"
    
    for key, value in histo_dict.items():
        print(key, value)