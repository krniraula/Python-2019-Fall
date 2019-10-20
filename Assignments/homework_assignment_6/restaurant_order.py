

#Name: Khem Niraula
#Student ID: 0644115
#Due Date: October 20, 2019
#MSITM 6341

menu_items = {

    'Fish Curry': 15.00,

    'Chicken': 10.00,

    'Fry Rice': 9.00,

    'Mashed Potatoes': 5.00,

    'French Fries': 23.00,

    'American Pasta' : 15.99

}

ordered_items = {

    'Chicken',

    'Pork',

    'Mashed Potatoes'

}

 

total=0

for item in ordered_items:

    if item in menu_items:

      print('{} : ${}'.format(item,menu_items[item]))

      total += menu_items[item]

    else:

      print("We do not have {}".format(item))

print('---------------------')

print('Order Total : ${}'.format(total))





