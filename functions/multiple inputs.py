def studentdeets(nameVar, agevar):
    if len(nameVar) > agevar:
        print("Your name has more letters than years you have lived")
        nameGtAge = True
    else:
        print("You are older than the amount of letters in your name")
        nameGtAge = False
    return {"name": nameVar, "age": agevar, "namelengthchange":nameGtAge}


studentName = str(input("Put in a name: "))
studentAge = int(input("Put in an age: "))
#functreturn = studentdeets(studentName, studentAge)
studentdeets(studentName, studentAge)
#print(functreturn)