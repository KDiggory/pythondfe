## number guessing
# get the program to generate a number between 1 and 100 then ask user to guess
## each time it is wrong they get another hint
#

import random ## import the random module

number = random.randint(1,10) ## set the number variable as a number between 1 and 100
guess = None

while number != guess:
    guess = int(input("What number do you guess? (between 1 and 10) "))
    if guess == number:
        print("Wow, got it! Winner!")
        break
    elif guess < number:
        print("Higher than that!")
        print("Have another try: ")
        break
    elif guess > number:
        print("Lower than that")
        print("Have another try: ")
        break
    else:
        exit()

print(f"The answer was {number}")
