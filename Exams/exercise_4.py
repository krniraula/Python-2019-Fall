menu = ["potato","chicken","milk","egg","tomato",]
price = [3.99,299,1.89,4.29,6.39]
#print(menu)
#print(price)

print("item: ",menu[2] + ' Price: $' + str(price[2]))
menu.insert(1,"orange") 
print(menu)
price.insert(1,1.98)
print(price)
del menu[-1]
print(menu)
del price [-1]
print(price)
double_price = price[3]*2
price[3]= double_price
print(menu)
print(price)

menu_items_in_stock = ['Tacos', 'Chips', 'Salsa', 'Quesadilla']

customer_order = ['Tacos','Guacamole','Burrito','Chips','Salsa']

menu_items_in_stock = [ item.lower() for item in menu_items_in_stock]

customer_order = [ item.lower() for item in customer_order]

for item in customer_order:
    if item in menu_items_in_stock:
        print("We have " + item.title() + " in stock.")
    else:
        print("We do not have " + item.title() + " in stock.")