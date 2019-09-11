grocery_items = ['Apple', 'orange','steak','chicken','water'] 
grocery_items.sort() 
sorted(grocery_items)  

(grocery_items_sorted) = sorted(grocery_items) 
#grocery_items.reverse()
print(grocery_items_sorted)

print(grocery_items)
print(len(grocery_items))
print(grocery_items[2:len(grocery_items)])
print(grocery_items[3:])

for item in grocery_items:
    print(item)    