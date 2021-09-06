#number = int(input("type a number: "))
#count = 0
#while str(number) != str(number)[::-1]:
    
   # number = int(number) + int(str(number)[::-1])
  #  count = count + 1
 #   print(f"checking {number}")
#print("Palindrome found in " + str(count) + " steps. Final number was: " + str(number))

##without slicing - need to get it using reverse and then put all onto one line


#ask for input
number2 = int(input("type a number again: "))
#set variables outside of loop
revlist = []
varasInt = int(number2)
print(varasInt)
varasStr = str(varasInt)
print(varasStr)

for i in reversed(varasStr):
    revlist.append(i)
print(revlist) # this is a list --> needs to be an integer
#convert the list to a string and then an integer
listAsStr = [str(ints) for ints in revlist] # as a string iterate through each number to make the list a string
furtherStr = "".join(listAsStr) # join each number together in the string so they arent comma separated
finalInt = int(furtherStr) # turn this string into an int


print(finalInt)
print(varasInt)
type(finalInt)
type(varasInt)
print(reversed(str(finalInt)))

count = 0
while varasInt != finalInt:
    varasInt = varasInt + finalInt
    finalInt = varasInt + finalInt
    count = count + 1
    print(f"checking {varasInt}")
print("Palindrome found in " + str(count) + " steps. Final number was: " + str(varasInt))

