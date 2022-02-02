# Write your solution here

def same_chars(string, index_1, index_2):
    '''The 2 integers refer to indexes within the string
        Return a boolean if indexes are the same or different'''
    if index_1 > (len(string) - 1) or index_2 > (len(string) - 1):
        return False

    char1 = string[index_1]
    char2 = string[index_2]
    return char1 == char2

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))