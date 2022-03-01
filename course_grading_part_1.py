# Part 6 Exercise 4
# Course grading, part 1

file1 = input("Student information: ")
file2 = input("Exercises completed: ")

student_dictionary = {}
student_names = {}

with open(file1) as file_object:
    for line in file_object:
        line = line.replace('\n', '')
        line = line.split(';')
        if line[0] == 'id':
            continue
        student_names[line[0]] = line[1:]

for id, name in student_names.items():
    student_dictionary[id] = ' '.join(name)

student_exercises = {}

with open(file2) as file_object:
    for line in file_object:
        line = line.replace('\n', '')
        line = line.split(';')
        if line[0] == 'id':
            continue
        student_exercises[line[0]] = []
        for exercises in line[1:]:
            student_exercises[line[0]].append(int(exercises))

for id, exercises in student_exercises.items():
    student_dictionary[id] += (' ' + str(sum(exercises)) )

for values in student_dictionary.values():
    print(values)
