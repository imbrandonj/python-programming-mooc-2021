# Pt 4 exercise 8
# Spruce

def spruce(height):
    '''Prints asterisks, centered, descending from 1 to height
    (Creates a spruce tree)
    Will always have single asterisk as spruce base'''

    print("a spruce!")
    i = 1
    width = 1
    while i <= height:
        print(("*" * width).center((height * 2) - 1))
        i += 1
        width += 2
    print(("*").center(width - 2))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)