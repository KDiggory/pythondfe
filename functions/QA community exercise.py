def total_score(name,homework,assessment,final_exam):
    total = hw + ass + exam
    totalperc = (total/175) * 100
    return totalperc

def grade_calc(total_score):
    if totalpercentage > 80:
        grade = "A"
    elif totalpercentage >=70:
        grade = "B "
    elif totalpercentage >=60:
        grade = "C"
    elif totalpercentage >= 50:
        grade = "D"        
    elif totalpercentage >= 40:
        grade = "E"
    else:
        grade = "FAIL"
    return grade

   
nameVar = (input("Enter your name: "))
hw = int(input("Enter your homework score: "))
if hw > 25: # this checks if the score given is within the possible score
    print("Score not possible out of 25") ## this line prints an error if the number given is higher than the possible score 
    exit() # this exits without asking for anything else
ass = int(input("Enter your assessment score: "))
if ass > 50:
    print("Score not possible out of 50")
    exit()
exam = int(input("Enter your exam results: "))
if exam > 100:
    print("Score not possible out of 100")
    exit()

totalpercentage = total_score(nameVar, hw, ass, exam) ## need to assign the returned variable to a variable that can be used outside the function
totalgrade = grade_calc(totalpercentage)
print(f"{nameVar} got an overall percentage of {totalpercentage}, your grade is: {totalgrade}")




