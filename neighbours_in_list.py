# Part 4 Exercise 37
# Neighbours in a list

def longest_series_of_neighbours(int_list):
    """ Takes a list of integers
        Looks for the longest series of neighbours
        Returns its length """

    longest_series = 0
    this_series = 1
    count = 0  # Excludes the first for iteration
    last_int = 0

    for i in int_list:
        if count == 0:
            count += 1
            last_int = i # Sets initial number to be compared by index 1
            continue

        elif i + 1 == last_int or i - 1 == last_int or i == last_int:
            this_series += 1

            if this_series > longest_series:
                longest_series = this_series

        else:
            this_series = 1

        last_int = i

    return longest_series