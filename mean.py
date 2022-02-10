# Part 4 Exercise 18
# Arithmetic mean

def mean(list):
    '''Takes a list and returns the mean of the values of the list'''
    
    total = 0.0

    for i in list:
        total += i
        
    result = total / len(list)
    return result


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1]
    result = mean(my_list)
    print(result)