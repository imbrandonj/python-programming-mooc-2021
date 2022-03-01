# Part 6 Exercise 19
# Incorrect lottery numbers

def filter_incorrect():
    """ Creates a file called correct_numbers.csv 
        Contains correct numbers from lotter_numbers.csv"""
        
    contents = []
    with open('lottery_numbers.csv') as f:
        lines = f.readlines()
        x = 1  # Counts the week

        for line in lines:
            format_line = line.split(';')
            numbers = format_line[1].split(',')  # Stores lottery numbers in list to test length and repeat values
            format_line[1] = format_line[1].replace(',','')

            repeat_numbers = []
            is_repeat = False
            within_range = True
            is_int = True

            for number in numbers:
                try:
                    number = int(number)
                except ValueError:
                    is_int = False
                else:
                    if number in repeat_numbers:
                        is_repeat = True
                    elif number > 39 or number < 1:
                        within_range = False
                    else:
                        repeat_numbers.append(number)
            
            if len(numbers) == 7 and is_repeat == False and within_range == True and is_int == True:
                if format_line[0] == f"week {x}":
                    contents.append(line)

            x += 1

    with open('correct_numbers.csv', 'w') as correct_f:
        for line in contents:
            correct_f.write(line)

# filter_incorrect()