def valid_url(url):                         #Checks for a valid URL...url is a STRING
    if(url[0:7] == "http://"):              #if it starts with http://
        urlBody = url[7:]                   #takes the URL body
        domainSegments = urlBody.split(".") #separates into segments
        for segment in domainSegments:      #for each segment
            if(segment == "" or not segment.isalpha()): #make sure it isn't a "" or that it has something that isn't a char
                return False
        if(len(domainSegments) > 1):        #if there are 2 or more segments
            return True                     #This is the only path that where it will be true
    return False                            #If any of the checks fail, this catches all

print(valid_url("http://www.nyu.edu"))      #valid
print(valid_url("http://files.nyu.edu"))    #valid
print(valid_url("http://www.myweb.nyu.edu"))#valid
print(valid_url("http://nyu.edu"))          #valid
print(valid_url("http://nyu"))              #invalid
print(valid_url("nyu.edu"))                 #invalid
print(valid_url("http://http://"))          #invalid
print(valid_url("http://foobar"))           #invalid
print(valid_url("http://www2.nyu.edu"))     #invalid
print(valid_url("http://nyu.edu."))         #invalid