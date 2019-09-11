grocery_items = ['Apple', 'orange','steak','chicken','water'] 
number_of_grocery_iteams = [4, 3, 6, 1, 2, 4, 10, 2400]
print (grocery_items)
#print (grocery_items[0])
#print (grocery_items[-1])
#print (grocery_items[-3])

grocery_items.append('pear')

grocery_items.append('watermelon')
print(grocery_items)
grocery_items.remove("pear")
del grocery_items[2]
print(grocery_items)
grocery_items.append('mango')
print(grocery_items)

grocery_items.sort() 
sorted(grocery_items)
grocery_items.reverse()
print(grocery_items)


