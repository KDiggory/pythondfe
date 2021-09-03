print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~ Love match calculator ~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name1 = str(input("What is the first name? ")) ## ask for input names
name2 = str(input("What is the second name? "))

num3 = name1.count("a") ## count how many of the letter a there is in it
num4 = name2.count("a")
num5 = len(name1.zfill(4)) ## add 4 0s on and count the new length 


numbers = [] ## make a list of numbers - number depending on which letter in the string
for letter in name2:
    num6 = ord(letter) -96 ## its -96 because lowercase a is assigned a value of 97
    numbers.append(num6)

num7 = 0                # set a new variable as 0, as will need the variable already made for the next step
for ele in range(0, len(numbers)):  #for each element in numbers add it to the new variable, each time taking the variable and adding the new element
    num7 = num7 + numbers[ele]

final = (num7 + num3 + num4 + num5 + num6)  ## add them together
print(f"Your match is {final}%")    ## print it out

##From Anthony - shows the characters and their unicode values


def split(word): ## split the string into characters
    return [char for char in word]

def uniVal(lWord): ##for each thing in LWord add the unicode character into the variable emp
    emp = []
    for i in lWord:
        emp.append(ord(i))

    return emp

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
aLower = split(lower)
aUpper = split(upper)
print(lower)
print(uniVal(aLower))
print()
print(upper)
print(uniVal(aUpper))

