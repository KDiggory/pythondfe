textVar = "Katie"
otherVar = textVar
capsVar = textVar.upper()

print(bool(textVar is otherVar))    ## is and is not is used when looking at strings not numbers
print(bool(textVar is not capsVar)) 

print(bool(9 == 9)) # true
print(bool(9 != 9)) # false
print(bool(9 >= 10)) # false
print(bool(9 <= 11)) # true
