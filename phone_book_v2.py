# Part 5 Exercise 18
# Phone book, version 2

phonebook = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit) "))

    if command == 1:
        name = input("name: ")
        if name in phonebook:
            if type(phonebook[name]) == list:
                for values in phonebook[name]:
                    print(values)
            else:
                print(phonebook[name])
        else:
            print("no number")

    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number]
        print("ok!")

    elif command == 3:
        print("quitting...")
        break
