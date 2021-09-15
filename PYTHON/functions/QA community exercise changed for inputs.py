def total_score(homework,assessment,final_exam):
    total = homework + assessment + final_exam
    totalperc = (total/175) * 100
    return totalperc

def grade_calc(totalpercentage):
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
    elif totalpercentage >= 30:
        grade = "F"
    else:
        grade = "FAIL"
    return grade

def checkscore(question, thelimit):
    while True:
        var1 = int(input(question))
        if var1 > thelimit:
            print("That is too high, try again")
        else:
            return var1

nameVar = (input("Enter your name: "))
  
homework = checkscore("Homework score: ", 25)
assessment = checkscore("Assessment score: ", 50)
examscore = checkscore("Final exam score: ", 100)


totalpercentage = 0
totalpercentage = total_score(homework, assessment, examscore) ## need to assign the returned variable to a variable that can be used outside the function
totalgrade = grade_calc(totalpercentage)
print(f"{nameVar} got an overall percentage of {totalpercentage}, your grade is: {totalgrade}")




