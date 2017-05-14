prices = []     #list for valid prices
while(True):    #Continually take in inputs
    price = input("Enter a price, 0 to end: ")
    if(price.isdigit() or (price[0] == "-" and price[1:].isdigit())):   #if a number, or a NEGATIVE one
        num = int(price)        #cast to int
        if(num > 0):            #if positive
            prices.append(num)  #add it in
        elif(num == 0):         #We stop taking input
            break
        else:
            print("Number must be positive!")
    else:
        print("That's not a number")

total = 0.0
for price in prices:    #summing in a list
    total += price

print("Total cost: ", total)
average = total/len(prices)
print("Average cost: ", average)        #average
print("Highest price: ", max(prices))   #max
print("Lowest price: ", min(prices))    #min

lessThanAvg = 0
greaterThanAvg = 0
for price in prices:                    #notice how we can check for both things in one pass
    if price >= average:
        greaterThanAvg += 1
    else:
        lessThanAvg += 1

print("# of prices >= avg: ", greaterThanAvg)
print("# of prices < avg: ", lessThanAvg)


#if a > b:
##do something
#else: #a <= b
#
#if a >= b:
##do something
#else: #a < b