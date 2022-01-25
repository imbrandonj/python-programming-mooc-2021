# Taking Turns
"""Please write a program which asks the user to type in a number. 
The program then prints out the positive integers between 1 and the number itself, 
alternating between the two ends of the range as in the examples below."""


number = int(input("Please type in a number: "))
base_count = 1
end_count = number

while base_count <= (number / 2):
    print(base_count)
    base_count += 1
    print(end_count)
    end_count -= 1

if number % 2 == 1:
    print(base_count)