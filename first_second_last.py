# Part 4 exercise 11
# first_second_last
# Takes a string and returns the first word, second word, and last word

def first_word(string):
    ''' Returns the first word in a string '''
    if ' ' in string:
        index = string.find(' ')
        word = string[:index]
        return word

def second_word(string):
    ''' Returns the second word in a string '''
    if ' ' in string:
        index = string.find(' ') + 1
        string_2 = string[index:]
        if ' ' in string_2:
            index = string_2.find(' ')
            word = string_2[:index]
            return word
        return string_2
    
def last_word(string):
    ''' Returns the last word in a string '''
    if ' ' in string:
        index = string.rfind(' ') + 1
        word = string[index:]
        return word


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))