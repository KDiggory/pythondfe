number2 = 452

revlist = [] #set variables outside of loop
revlist2 = []

varasStr = str(number2) 
for i in reversed(varasStr):
    revlist.append(i)
print(revlist) # this is a list --> needs to be an integer
#convert the list to a string and then an integer
listAsStr = [str(ints) for ints in revlist] # as a string iterate through each number to make the list a string
furtherStr = "".join(listAsStr) # join each number together in the string so they arent comma separated
finalInt = int(furtherStr) # turn this string into an int
print(finalInt)
print(number2)
print(furtherStr)
while int(number2) != (finalInt):
    if int(number2) != (finalInt):
        revlist = []
        varasStr = str(number2)
        print(varasStr)
    for i in varasStr:
        revlist.append(i)
        listAsStr = [str(ints) for ints in revlist] 
        furtherStr = "".join(listAsStr)
        number2 = int(furtherStr)
        number2 = number2 + finalInt
    else:
        finalInt = str(number2)
        revlist = []
        for i in reversed(finalInt):
            revlist.append(i)
            listAsStr = [str(ints) for ints in revlist] 
            furtherStr = "".join(listAsStr)
            finalInt = int(furtherStr)

print(finalInt)
print(number2)