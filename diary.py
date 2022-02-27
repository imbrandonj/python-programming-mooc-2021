# Part 6 Exercise 11
# Diary

file = 'diary.txt'

while True:
    print("1 - add entry, "
            "2 - read entries, "
            "0 - quit")
    selection = int(input("Function: "))

    if selection == 1:
        add_entry = input("Diary entry: ")

        with open(file, 'a') as file_object:
            file_object.write(f"{add_entry}\n")

        print("Diary saved")

    elif selection == 2:
        print("Entries:")

        with open(file) as file_object:
            for line in file_object:
                print(line)

    elif selection == 0:
        print("Bye now!")
        break