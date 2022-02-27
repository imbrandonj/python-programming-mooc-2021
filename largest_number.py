# Part 6 Exercise 1
# Largest number

def largest():
    number_storage = []
    with open('numbers.txt') as file_object:
        for line in file_object:
            number = int(line)
            number_storage.append(number)
    number_storage.sort()
    return number_storage[-1]

