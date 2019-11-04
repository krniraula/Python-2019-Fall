#Name: Khem Niraula
#Student ID: 0644115
#Due Date: November 3, 2019
#MSITM 6341


menu_item_name = []
def ask_user_for_menu_item_name():
    
    continue_or_not = True
    while continue_or_not == True:
        item_name = input('Item name: ')
        item_name.lower()
        if item_name.lower() in menu_item_name:
            print("WARNING: ITEM ALREADY EXISTS")

        else:
            menu_item_name.append(item_name)
            want_to_continue = input("You want to continue? Y/N: ")
            want_to_continue.lower()

            if want_to_continue == "n":
                continue_or_not = False
                print(menu_item_name)
            elif want_to_continue == "y":
                continue_or_not = True
            else:
                return want_to_continue

menu_item_cost = []
loop_count = len(menu_item_name)

def ask_user_for_menu_item_cost():
    
    
    loop_count = len(menu_item_name)
    for loop_count in range(0,loop_count):
        #print("Works Works Works \n")
        item_cost = input("Item price: ")
        menu_item_cost.append(item_cost)

       
def add_menu_item():


    ask_user_for_menu_item_name()
    ask_user_for_menu_item_cost()

print("\n......................... ")
print("Please enter the menu items for the Restaurant")
print(".........................")
add_menu_item()
menu_item_add = dict(zip(menu_item_name, menu_item_cost))
#print(menu_item_add)

print(".........................")
print("Restaurant Menu")
print(".........................")
for item in menu_item_add:
    print("Item:",item + "  Cost:",menu_item_add[item])
print(".........................")