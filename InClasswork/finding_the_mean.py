#Find the mean of a list of numbers

def mean(list_of_numbers):

    total = sum(list_of_numbers)
    count = len(list_of_numbers)
    return total/count

test_numbers = [5,6,56,45,3,34]
print(round(mean(test_numbers),2))