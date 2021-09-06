# We will write a while loop which asks for the users name, then prints the user's name followed by "is awesome!" 5 times.

count = 0
name = str(input("What is your name? "))

while count < 5:
    print(name + "is awesome!")
    count += 1

# We will write a for loop which prints all the numbers between 5 and 10

for i in range(5,11):
    print(i)

#Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"
names = input("Enter your names: ")
namesList = names.split()
for each in namesList:
    print(f"{each} is awesome")

for i in range(10, 21, 2): ## this prints the numbers between 10 and 20 in intervals of 2
    print(i)

