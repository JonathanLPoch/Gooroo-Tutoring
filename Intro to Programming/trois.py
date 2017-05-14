code = {
    6:["t", "g"],
    14:["p", "g"],
    15:["c","d"],
    9:["o","a"]
}
data = "5,0:3,1:2,0"

splitdata = data.split(":")     #splitdata = ["5,0", "3,1", "2,0"]
for item in splitdata:          #for each string in list
    splititem = item.split(",") #splititem = ["5", "0"], etc. Think of like coordinates
    print(code[int(splititem[0])*3] [int(splititem[1])], end="")    #takes coordinate, int casts, and accesses dictionary
    #first item multiplied by 3 (key), second for value
