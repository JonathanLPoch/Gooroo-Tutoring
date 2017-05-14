s = "Oh baby,baby Oh baby,baby Ah,yeah,yeah Oh baby,baby How was I supposed to know"    #Your typical song lyric
words = []  #To hold separated words
placeholder = 0 #because we cannot simply call split(" ")
for i in range(0, len(s)):  #for the entire length of the string (what is it incrementing by?)
    if(i == len(s)-1):   #if at the end of the string
        words.append(s[placeholder:i+1])    #add in the last word
if(s[i] == " " or s[i] == "." or s[i] == "," or s[i] == "?" or s[i] == "!"):    #for any type os separator
        words.append(s[placeholder:i])  #add to the list
    placeholder = i+1   #move the placeholder up

dict = {}   #dictionary to hold the words...key:value -> word:count
for word in words:
    if word.lower() in dict:    #if the word already exists...
        dict[word.lower()] += 1 #increment the count.
    else:                       #if the word doesn't exist
        dict[word.lower()] = 1  #start an entry

print(dict)                     #just so you can see the counts
maxKey = ""
maxValue = 0
for key, value in dict.items(): #Here we find the max value and key associated
    if value > maxValue:
        maxKey = key
        maxValue = value
print("\"",maxKey,"\" was used ",maxValue, " times", sep = "")  #notice the separator. by default it is a single SPACE " "