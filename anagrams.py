# Part 4 Exercise 23
# Anagrams

def anagrams(string1, string2):
    ''' Tests if a string is an anagram 
        Two words are anagrams if they
        contain exactly the same characters '''

    string1 = sorted(string1.lower())
    string2 = sorted(string2.lower())

    if string1 == string2:
        is_anagram = True
        return is_anagram
    
    else:
        is_anagram = False
        return is_anagram
