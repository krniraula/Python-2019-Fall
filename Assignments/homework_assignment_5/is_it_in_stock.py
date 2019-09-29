
#Name: Khem Niraula
#Student ID: 0644115
#Due Date: September 29, 2019
#MSITM 6341

menu_items_in_stock = ['Tacos', 'Chips', 'Salsa', 'Quesadilla']
customer_order = ['Tacos', 'Guacamole', 'Burrito', 'Chips', 'Salsa']

#converting both the lists to lower case using lower keyword

menu_items_in_stock_lower =[dish.lower() for dish in menu_items_in_stock]
customer_order_lower = [dish.lower() for dish in customer_order]
print(menu_items_in_stock_lower)
print(customer_order_lower)

#checking whether the customer_order is available in stocks for elements in customer_order:
for item_ordered in customer_order:
    if item_ordered in menu_items_in_stock:
        print('We have ' + item_ordered + ' in stock' + '.')
    else:
        print('We do not have ' + item_ordered + ' in stock' + '.')
