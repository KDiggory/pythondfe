## Conditionals
#The if statement

testNum = float(input("type in a number: "))

if testNum > 100 and testNum <= 1000:
    print("Thats a big number!")
    print("This line will also print if the condition is true")
elif testNum >1000: ## this line needs to be first after the if statement as it is the biggest thing to check
    print("thats huge") # when it was below the test ran the 50 and selected taht statement
elif testNum > 50:
    print("That is a meh number")   ## can have as many elif statements as you want
#elif testNum > -1:      # this doesnt work for some reason
   # print("Negative number! ")
else:
    print("Thats not such a big number")
    print("this line print if the test is false")
    var = 2 + 2 ## can also do maths and stuff in the function
    print(var)

print("This line will print regardless --> because it is not indented")

if testNum < 50 or testNum >= 100: ## to test a ramge
    print("its either big or small")
else:
    print("A middling number")


costNum = 50
if not(testNum == 42): # not does the same as using the != so could be testNum != 42:
    print("You have not discovered the meaning of life") 
else:
    print("You've got it!")
