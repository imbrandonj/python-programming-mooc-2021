# Part 5 Exercise 24
# The oldest person

def oldest_person(people: list):
    """ Takes a list of tuples
        In each tuple the first value is name and second is age
        Returns the name of the oldest person in the list """

    stored_years = []

    for i in people:
        stored_years.append(i[1])
    
    stored_years.sort()

    for i in people:
        if stored_years[0] in i:
            return (i[0])

