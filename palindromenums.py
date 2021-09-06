num = int(input("What is your input? ")) # input needs to be a string so it can be reversed

print(numStr)
revStr = numStr[::-1] # reverse the number and store it in another
print(revStr)
totalSteps = 0
while str(num) != str(num)[::-1]:
    num = int(num) + int(Str(num)[::-1])
    totalSteps = totalSteps +1
    print(f"checking {num}")
print("Palindrome found in" + str(totalSteps) + " steps. Final number was: " str(num))
        


#while (int(numStr) > -1 ):
    #rev = str(num[::-1])

#if num == rev:
   # print (num)
        #break
#else:
    #num = int(str(num[::-1])) + int(num) 
   # print(num)
    #numberOfSums += 1

#print(numberOfSums)


## this was from David - kind of similar to my original but much better --> just need while loop not if and else as well
number = int(input("type a number")
count = 0
while str(number) != str(number)[::-1]: 
    number = int(number) + int(str(number)[::-1])
    count = count +1
    print(f"checking {number}")
print("Palindrome found in" + str(count) + " steps. Final number was: " str(number))
        





