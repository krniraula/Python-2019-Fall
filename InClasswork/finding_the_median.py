def median(list_of_numbers):
    list_of_numbers.sort()
    count = len(list_of_numbers)
    #check if "count'" of even of odd
    if count%2==0:
        first_idx = int(count / 2)
        second_idx = first_idx -1
        avg = (list_of_numbers[first_idx] +list_of_numbers[second_idx])/2
        return avg

    else:
        middle_number= count // 2
        return list_of_numbers[middle_number]
odd_numbers = [12,13,14,7,5]
even_numbers = [12,32,7,9,12,14]
    
print(median(odd_numbers))
print(median(even_numbers))