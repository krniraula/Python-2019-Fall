#Name: Khem Niraula
#Student ID: 0644115
#Due Date: Octobar 29, 2019
#MSITM 6341

menu_items = {
    'Fish Curry': 15.00,
    'Chicken': 14.00,
    'Fry Rice': 9.00,
    'Mashed Potatoes': 12.00,
    'French Fries': 23.00,
    'American Pasta' : 15.99
}

customer_order = []
active = True
prompt = "\nPlease enter an item you want to order:"
prompt += "\n(Enter 'done' when you are finished.) "

while active:
    input_order = input(prompt)
    if input_order.lower() == 'done':
        active = False
    else: customer_order.append(input_order)
Total=0
print("\nBelow is your order details:")
for item in customer_order:
    if item in menu_items:
        print('{} : ${}'.format(item,menu_items[item]))
        Total += menu_items[item]
    else:
        print("sorry, we don't have {}".format(item))
print("----------------")
print("Total : $" + str(round(Total,2)))