Symbol = "FB"
Today_price = 111.12
Yesterday_price = 113.10
print(f"Symbol is {Symbol}")
print("Yesterday_price is",(Yesterday_price))
print("Today_price is",(Today_price))
print("Difference is", round(Yesterday_price-Today_price,2))

menu_items_in_stock = ['Tacos', 'Chips', 'Salsa', 'Quesadilla']
customer_order = ['Tacos', 'Guacamole', 'Burrito', 'Chips', 'Salsa']

#converting both the lists to lower case using lower keyword

menu_items_in_stock_lower =[item.lower() for item in menu_items_in_stock]
customer_order_lower = [item.lower() for item in customer_order]
#print(menu_items_in_stock_lower)
#print(customer_order_lower)

for i in range (0,len(customer_order_lower)):
    if customer_order_lower[i] in menu_items_in_stock_lower:
        print("We have", customer_order[i],"in stock.")
    else:
        print("We do not have",customer_order[i],"in stock.")