# Part 5 Exercise 15
# Factorials

def factorials(n: int):
    """ Takes an integer and creates a dictionary
        Stores all numbers up to integer as keys
        The values are the factorials of each key
        Returns dictionary """
    
    factorial_dict = {}

    for factorial in range(1, n + 1):

        if factorial == 1:
            factorial_dict[factorial] = factorial
            continue

        operand = factorial * (factorial - 1)
        countdown = factorial - 2

        for i in range(countdown):
            operand *= countdown
            countdown -= 1

        factorial_dict[factorial] = operand
        factorial += 1
    
    return factorial_dict