# Please write a program which asks the user to type in a sentence. 
# The program then prints out the first letter of each word in the sentence, each letter on a separate line.

sentence = input("Please type in a sentence:")
print(sentence[0])

while ' ' in sentence:
    character = sentence.find(' ') + 1
    print(f"{sentence[character]}")
    sentence = sentence[character:]