def foo(a):                 #foo will take a string, check if the input is a digit, and if so, print
    if a.isdigit():         #is the string a digit?
        print(a)            

data1 = "5,10,15"
for item in data1:          #Equivalent of saying, for character in string
    foo(item)               #call foo on each character

print("----")
data2 = data1.split(",")    #split by comma ["5", "10", "15"] <- list of STRINGS

for item in data2:          #for each item in data2
    foo(item)               #call the function

print("======")

#str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
#print(str.split())      #by default, it returns by line
#print(str.split('\n'))  #delimits by exactly what you give it