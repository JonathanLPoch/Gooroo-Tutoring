def valid_n_number(num):
    if(len(num) != 9):      #length checking
        return False
    if(num[0] != "N"): #if it is an upper case N
        return False

    newString = num[1:]             #substringing! See comments at bottom
    if(not newString.isdigit()):    #if the substring after N is not full of digits
        return False        

    #Alternative, also valid
    for x in range(1,9):            #ranged for loop, goes character by character from 1 -> 8
        if (not num[x].isdigit()):  #if the number is not a digit
            return False

#why does this not work?
#    for x in range(1,9):
#        if (not int(num[x]) > -1 & int(num[x]) < 10):
#            return False
    return True

test1 = valid_n_number("N123")
test2 = valid_n_number("N1234567890")
test3 = valid_n_number("n12345678")
test4 = valid_n_number("NXYZ!5678")
test5 = valid_n_number("N12345678")

print(test1, test2, test3, test4, test5)

#len(string)
#string[index] is charAt
#>>> x = "Hello World!"
#>>> x[2:]
#'llo World!'
#>>> x[:2]
#'He'
#>>> x[:-2]
#'Hello Worl'
#>>> x[-2:]
#'d!'
#>>> x[2:-2]
#'llo Worl'
