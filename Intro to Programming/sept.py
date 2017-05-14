lyrics = "like Baby baby baby ohhh Baby baby Like oooo this is terrible"
words = lyrics.split(" ")           #["like", "Baby", "baby", "baby", ..., "terrible"]
unique = []
for word in words:                  #iterate through the words (a list)
    if not word.lower() in unique:  #if the word, case insensitive, already exists in unique (list)
        unique.append(word.lower()) #add to the list
for item in unique:                 #for each item in the unique word list
    print(item, end = " ")          #print with end separated by space (newline is default "\n")