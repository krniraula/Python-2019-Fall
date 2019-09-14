
#Name: Khem Niraula
#Student ID: 0644115
#Due Date: September 15, 2019
#MSITM 6341

grocery_items=['milk','sugar','salt','orange','mango']
grocery_items_price=[1.99,4.99,1.79,4.99,6.99]

#Print the 3rd item followed by it’s price

print(grocery_items[2]+' $' + str(grocery_items_price[2]))

#Print the last item followed by it’s price

print(grocery_items[-1]+' $'+str(grocery_items_price[-1]))

#Add a 6th item and it’s price

grocery_items.append('chicken')
grocery_items_price.append(7.99)

#Print the list of items
print(grocery_items)

#Print the list of prices
print(grocery_items_price)

#Remove the first item and it’s price
del grocery_items[0]
del grocery_items_price[0]

#Double the price of the 2nd item

double_price=grocery_items_price[1]*2
grocery_items_price[1]=double_price

#Print the list of items
print(grocery_items)
#Print the list of prices
print(grocery_items_price)