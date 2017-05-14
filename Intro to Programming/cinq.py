def valid_n_number(num):    #same as from #4
    if(len(num) != 9):
        return False
    if(num[0] != "N"):
        return False
    
    newString = num[1:]
    if(not newString.isdigit()):
        return False
    
    for x in range(1,9):
        if (not num[x].isdigit()):
            return False

#why does this not work?
#    for x in range(1,9):
#        if (not int(num[x]) > -1 & int(num[x]) < 10):
#            return False
    return True

list = []                                   #to hold valid numbers
while(len(list) < 5):                       #once the list has 5 unique, valid N Numbers
    num = input("Enter an N Number: ")      #prompts input (what kind of value is num?)
    if(valid_n_number(num)):                #if valid
        if not num in list:                 #if not already recorded (basically, if unique)
            list.append(num)                #add to list
        else:
            print("Duplicate N Number")     #otherwise...duplicate
    else:
        print("Invalid N Number")           #otherwise...invalid

print("Your N-Numbers:\n\n")
list.sort()                                 #important for ascending order. Think about why this works
for x in range(0, 5):                       #ranged for loop, x takes on values 0, 1, 2, 3, 4 (not 5)
    print(list[x])                          #same as print(list[x], end = "\n")