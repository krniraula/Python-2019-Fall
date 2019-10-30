#problem of the day 1

#Name: Khem Niraula
#Student ID: 0644115
#Due Date: Octobar 29, 2019
#MSITM 6341

number_list = [45,758,12,222,2358,5469,4453,2346,5236,6139,155,6776,4569,1225]

current_largest = 0

for num in number_list:
    if num > current_largest:
        current_largest = num
print("The largest no. is: ", current_largest)