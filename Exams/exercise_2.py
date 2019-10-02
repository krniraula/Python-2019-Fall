#Homework 3

grocery_items = ['Chicken', 'Steak', 'Fish', 'Apple']
grocery_items_prices = [10, 15, 25, 2]

print("Items: " + grocery_items[2] + " Prices: ", grocery_items_prices[2])

print("Items: " + grocery_items[3] + " Prices: ", grocery_items_prices[3])

grocery_items.append("Pineapple")
grocery_items_prices.append(4)

print(grocery_items)
print(grocery_items_prices)

del grocery_items[0]
del grocery_items_prices[0]

grocery_items_prices[1] = grocery_items_prices[2] * 2.0

print(grocery_items)
print(grocery_items_prices)