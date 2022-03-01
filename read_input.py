# Part 6 Exercise 17
# Reading input

def read_input(string: str, num1: int, num2: int):
    """ Takes a string and two integers
        Asks for input until user provides an integer between
        the two integer arguments """

    while True:
        try:
            number = int(input(string ))
        except ValueError:
            print(f"You must type in an integer between {num1} and {num2}")
        else:
            if number < num1 or number > num2:
                print(f"You must type in an integer between {num1} and {num2}")
            else:
                return number
