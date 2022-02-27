# Part 6 Exercise 2
# Fruit market

def read_fruits():
    """ Reads a csv file
        Returns a dictionary based on the contents """
    
    fruit_dict = {}
    
    with open('fruits.csv') as object_file:
        for line in object_file:
            parts = line.split(';')
            fruit = parts[0]
            value = parts[1:]
            value = ' '.join(value)
            fruit_dict[fruit] = float(value)
    
    return fruit_dict

