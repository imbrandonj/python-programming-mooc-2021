# Part 6 Exercise 12
# Filtering the contents of a file

def filter_solutions():
    """ Reads the contents of the file 'solutions.csv'
        Writes mathematically correct lnes into 'correct.csv'
        Writes mathematically incorrect lines into 'incorrect.csv'"""

    with open('solutions.csv') as file_object:

        contents = list(file_object)
        correct_list = []
        incorrect_list = []

        for line in contents:
            line_list = line.split(';')
            maths = line_list[1]
            maths = eval(maths)
            answer = line_list[2]
            answer = eval(answer)
            
            if maths == answer:
                correct_list.append(line)
            
            else:
                incorrect_list.append(line)
        
        with open('correct.csv', 'w') as correct_file:
            for line in correct_list:
                correct_file.write(line)

        with open('incorrect.csv', 'w') as incorrect_file:
            for line in incorrect_list:
                incorrect_file.write(line)

