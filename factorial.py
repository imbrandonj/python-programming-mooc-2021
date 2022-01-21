# Please write a program which asks the user to type in an integer number. 
# If the user types in a number equal to or below 0, the execution ends. 
# Otherwise the program prints out the factorial of the number.

number = int(input("Please type in a number:"))
i = 1
factorial = 1

while number > 0:
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")
    number = int(input("Please type in a number:"))
    factorial = 1
    i = 1

print("Thanks and bye!")