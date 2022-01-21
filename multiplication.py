# Please write a program which asks the user for a positive integer number. 
# The program then prints out a list of multiplication operations 
# until both operands reach the number given by the user. 

number = int(input("Please type in a number: "))
i = 1
y = 1

while i <= number and y <= number:
    while y <= number:
        outcome = i * y
        print(f"{i} x {y} = {outcome}")
        y += 1
    i += 1
    y = 1