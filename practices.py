## Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old

name = str(input("Hello, whats your name? "))
age = int(input("How old are you? "))

birthYear = (2021 - age)
print(f"You were born in {birthYear}")

year100 = (2021 + (100 - age))
print(f"You will be 100 in the year {year100} (plus or minus 1 year)")

## odd or even Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

number = int(input("Please give me a number: "))

if (number/2==0):
    print("Your number is even!")
elif (number/2!=0): 
    print("Your number is odd!")

