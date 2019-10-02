# Name: Khem Niraula
# Student ID: 0644115
# Due Date: 10/01/2019
# MSITM 6341
#
#
######################## Instructions ############################
#
# 1. Resolve any compiler errors
# 2. Follow any instructions given in comments starting with TODO
# 3. Resolve any runtime errors
# 4. Resolve any logical errors until the program outputs EXACTLY as the sample output below shows
#
##################### Program Description ########################
#
# The following program takes the stock prices for the past 6 days
# for a single company. It calculates the change in price over the
# provided days and outputs this change in price and indicates if the stock
# increased, decreased, or stayed the same. 
#
############## Sample Output of Functioning Program ##############
#
# ------------ SBUX ------------
# Yesterday:  Stock Decreased: -0.43
# 2 Days Ago: Stock Increased: 0.89
# 3 Days Ago: Stock Decreased: -0.74
# 4 Days Ago: Stock Increased: 1.49
# 5 Days Ago: No Change in Price
#
##################################################################

########## DO NOT MODIFY ##########
stock_symbol = "sbux"
stock_prices = [90.35, 89.92, 90.81, 90.07, 91.56, 91.56]
###################################

stock_price_changes = []

#TODO Write a for loop that iterates over all of the stock prices and computes the change in prices.
#Hint: How many elements should there be in stock_price_changes?

last_stock_price=0
# find the price change
for current_stock_price in stock_prices:

    if (last_stock_price == 0):
        last_stock_price = current_stock_price
    else:
        stock_price_changes.append( ( last_stock_price - current_stock_price )  )
        last_stock_price=current_stock_price

#print(stock_price_changes)
print("------------ " + stock_symbol.upper() + " ------------")

idx = 0
for price_change in stock_price_changes:

    what_day = ""
    if idx == 0:
        what_day = "Yesterday: "
    else:
        what_day = str(idx + 1) + " Days Ago:"


    if price_change > 0:
        print(what_day + " Stock Decreased: " + str(round((price_change * -1),2)))
    elif price_change < 0:
        print(what_day + " Stock Increased: " + str(round((price_change * -1),2)))
    else:
        print(what_day + " No Change in Price")

    idx = idx + 1
