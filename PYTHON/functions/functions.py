#functions are similar to a procedure
def countLetters(personname):
    return len(personname) ## passes the output of the function

studentName = str(input("Enter your name: "))
nameCount = countLetters(studentName) ## this variable is set up to catch the return of the function

print(f"{studentName} has {nameCount} characters in it")

def reversename(personname):
    if personname.isdigit():
        print("No numbers!")
        exit()
    countStr = len(personname)  #count the letters
    
    while countStr > -1: # lists start at 0 so need to use -1. eg if length is 5, the last letter will be number 4 in the index
        sdrawkacb = sdrawkacb + personname[countStr] 
    countStr = countStr -1
    return sdrawkacb
  


reversedname = reversename(studentName)
print(f"{studentName} is {reversedname} backwards")





