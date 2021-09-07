# take 2 names as input
# take name length, 
# take a loop which counts the vowels,
        # for letters in variable:
        # if letter is in a list add 1 to counter
#  make sure name (the input) is validated - this is often hard in programming. Keep this simple. make sure name isnt numbers .isdigit
#  do maths with the numbers

vowels =["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

def name_calculator(name1, name2):
    len1 = len(name1)
    len2 = len(name2)
    count1 = 0
    count2 = 0
    for l in name1:
        if l in vowels:
            count1 = count1 +1
    for l in name2:
        if l in vowels:
            count2 = count2 +1
    total = 0
    lens = len1 + len2
    counts = count1 + count2 
    counts = counts *5
    counts = counts /1.5
    total = (counts/lens) * 100
    if total > 100:
        total = total -100
    if total > 200:
        total = total -200
    if total > 300:
        total = total -300
    if total > 400:
        total = total -400
    if total > 500:
        total = total -500
    total = round(total,2)
    return total 

def love(total_score):
    if totalpercentage > 90:
        grade = "Crazy stupid love"
    elif totalpercentage >=80:
        grade = "True love"
    elif totalpercentage >=70:
        grade = "Love"
    elif totalpercentage >= 60:
        grade = "Best Friends"        
    elif totalpercentage >= 50:
        grade = "Good Friends"
    elif totalpercentage >= 40:
        grade = "Aquaintances"
    elif totalpercentage >= 30:
        grade = "Real dislike"
    elif totalpercentage >= 20:
        grade = "Hate them"
    elif totalpercentage < 20:
        grade = "Mortal enemies"
    else:
        grade = "FAIL"
    return grade



firstname = (input("Enter the first name: "))
if len(firstname) > 100:
    print("Thats a bit long, try a shorter name")
    exit()
elif firstname.isdigit():
    print("A name not a number please")
    exit()
secondname = (input("Enter the second name: "))  
if len(secondname) > 100:
    print("Thats a bit long, try a shorter name")
    exit()
elif secondname.isdigit():
    print("A name not a number please")
    exit() 

totalpercentage = name_calculator(firstname, secondname)
compgrade = love(totalpercentage)
print(f"The compatibility score of {firstname} and {secondname} is {totalpercentage}%") 
print("~~~" + compgrade + "~~~")


 