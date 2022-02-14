# Part 4 Exercise 34
# Most common character

def most_common_character(some_string):
    ''' Returns the character which has
        the most occurrences within a string '''

    most_common_count = 0
    character = ' '

    for i in some_string:
        occurrences = some_string.count(i)

        if occurrences > most_common_count:
            most_common_count = occurrences
            character = i

    return character