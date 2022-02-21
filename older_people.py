# Part 5 Exercise 25
# Older people

def older_people(people: list, year: int):
    """ Takes a list of tuples and an integer
        In each tuple the first value is name and second is age
        The integer argument represents a year
        Returns the name of each person born before the year given """
    
    stored_names = []

    for i in people:
        if i[1] < year:
            stored_names.append(i[0])
    
    return stored_names
