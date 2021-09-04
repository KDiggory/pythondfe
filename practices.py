## Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old

name = str(input("Hello, whats your name? "))
age = int(input("How old are you? "))

birthYear = (2021 - age)
print(f"You were born in {birthYear}")

year100 = (2021 + (100 - age))
print(f"You will be 100 in the year {year100} (plus or minus 1 year)")

## odd or even Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

n = int(input("Please give me a number: "))

if (n/2==0):
    print("Your number is odd!")
elif (n/2!=0): 
    print("Your number is even!")


## take a list and write a program that prints out all the elements that are less than 5

a = [1,2,3,4,5,6,7,8,9,10]

print([i for i in a if i <5]) # this works - output = i, item = i, list = a, filter == aa< 5

# if were doing it for words

letter = ["A", "B","G","B", "S"]
print([i for i in letter if i == "B"]) ## prints B twice as there are two

 ## create a program that asks for a number and then prints a list of the divisors of that number - a number that divides evenly into that number (has no remainder)num = int(input("Please choose a number to divide: "))

num = int(input("Please choose a number to divide: ")) ## This works - gotten from the internet.
                                                        # 1st get an input number and assign it to the variable num
listRange = list(range(1,num+1))                        # then make a list called listRange that has the numbers between 1 and the input number, the + 1 is needed because the last number in a range isnt included. 

divisorList = []                                        # make a function divisorList
                                                        # 
for number in listRange:                                # for each number in listRange do the following
    if num % number == 0:                               # if num % number is 0 then add it to the divisorList using append
        divisorList.append(number)

print(divisorList)                                       # print the list of appended numbers

