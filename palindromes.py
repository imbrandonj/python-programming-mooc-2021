# Part 4 Exercise 24
# Palindromes

def main():
    ''' Requests a string until string is a palindrome '''
    
    while True:
        string = input("Please type in a palindrome: ")
        is_palindromes = palindromes(string)
        if is_palindromes == True:
            break

def palindromes(string):
    ''' Tests if a string is a palindrome
        Palindrome are words which are spelled
        the same backwards and forward '''

    string_copy = string.lower()
    listed_string = list(string_copy)
    string_copy = list(string_copy)
    listed_string.reverse()
    reverse_string = listed_string

    if string_copy == reverse_string:
        print(f"{string} is a palindrome!")
        is_palindrome = True
        return is_palindrome

    else:
        print("that wasn't a palindrome")
        is_palindrome = False
        return is_palindrome

main()