#Write a function that takes as input a list of integers and returns the difference 
#(subtraction) between the largest and smallest numbers in the list. 
#Due Date: Dec 1, 2019
#Name: Khem Niraula
#Student ID: 0644115
#MSITM 6341

def subtraction():
  int_list = []
  ask_user = True
  while ask_user == True:
    x = int(input("Enter int value: "))
    int_list.append(x)
    ask = input("Do you want to continue? Y/N: ")
    if ask.lower() == "y":
      ask_user = True
    elif ask.lower() == "n":
      ask_user = False
    else:
      continue
  
  total_length = len(int_list)

  for check_value in range(1, total_length):
      #print(check_value)  
      if int_list[check_value] > int_list[check_value - 1]:
        largest_num =int( int_list[check_value])

      elif int_list[check_value]<int_list[check_value - 1]:
        smallest_num = int(int_list[check_value])

      elif int_list[check_value] == int_list[check_value - 1]:
        continue
      
  diff = largest_num - smallest_num
#  print("The largest and smallest number difference is " + str(diff))
  print(f"the largest num is {largest_num} and smallest num is {smallest_num} and their difference is {diff}")
  
subtraction()