#Name: Khem Niraula
#Student ID: 0644115
#Due Date: December 8, 2019
#MSITM 6341


file_name = "C:/Python 2019 Fall/Assignments/bonus_homework_1/bonus.txt"

with open(file_name) as file_object:
        for line in file_object:
            print("Email address Loaded: " +line)

print('Enter quit when finished')

while True:
    value = input("Enter the email address you would like to add: ")

    if value.lower() != 'quit':
        with open(file_name, 'a') as file_add:
            #add_info = input("Enter the email address you would like to add: ")

            file_add.write(value + '\n')
            print("Information saved")

    elif value.lower() == 'quit':
        with open(file_name) as read_file:
            for line in read_file:
                print("Email Address loaded: " + line)
            break
        breakkhemrajniraula@gmail.com
