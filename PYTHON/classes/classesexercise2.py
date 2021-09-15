
class VowelCheck:

    
    def __init__(self, toCheck = "AEIOUaeiou"): # defaults to vowels
        self.toCheck = toCheck
        self.count = 0
        

    def check(self, toBeChecked):
        for i in str(toBeChecked):
            if i in self.toCheck:
                self.count = self.count + 1
        if self.count > 0: 
            return self.count
        
wordcheck = VowelCheck() # this is the object made from the class
testthis = VowelCheck() # These two are identical at the moment but will learn how to change later
letterA = VowelCheck()

testthis.toCheck = "gjpqyGJPQY"
letterA.toCheck = "Aa"


vowelNum = wordcheck.check("Check this")
descenders = testthis.check("Does this work. Has it got any descenders?")
letterA = letterA.check("Check for any of the first letter of the alphabet")

#print(f"There are {vowelNum} vowels in your word")
#print(f"There are {descenders} of the letters in your word") # should only return one 
#print(f"There are {letterA} letter A's in your word")

## When this is used as a module to import comment out the print statements else you get those too!


                
        



