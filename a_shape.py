# Pt4 Exercise 7
# A shape

def line(length, words):
    """Prints the first character in words
        The length of the length argument"""
    
    if words == '':
        print("*" * length)

    else:
        character = words[0]
        print(character * length)

def shape(width, char_one, height, char_two):
    '''The first two arguments creates a descending shape (from 1 to width)
        The latter two arguments creates a base, at the width of width'''
    width += 1
    for i in range(width):
        line(i, char_one)
    
    width -=1
    for i in range(height):
        line(width, char_two)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")