# Part 6 Exercise 7
# Spell checker

text = input("Write text: ")
text_list = text.split(' ')

with open('wordlist.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('\n', ' ')

for word in text_list:
    if f" {word.lower()} " in contents or word == 'a':
        print(word, end=' ')
    else:
        print(f"*{word}*", end=' ')
