# create a class
# attributes which holds all the vowels
# method which sees if the input has vowels in it
# returns true or false
# Create an object from it
# check a string for vowels
# use the self variable --> will be self.vowels - used to represent the instance of the class

class VowelCheck:
    vowels = "AEIOUaeiou"
    count = 0

    def check(self, toBeChecked):
        for i in str(toBeChecked):
            if i in self.vowels:
                self.count = self.count + 1
        if self.count > 0: 
            return self.count
        
wordcheck = VowelCheck() # this is the object made from the class
testthis = VowelCheck() # These two are identical at the moment but will learn how to change later
letterA = VowelCheck()

testthis.vowels = "gjpqyGJPQY"
letterA.vowels = "Aa"


vowelNum = wordcheck.check("Check this")
descenders = testthis.check("why is this not working?")
letterA = letterA.check("Check for any of the first letter of the alphabet")

print(f"There are {vowelNum} vowels in your word")
print(f"There are {descenders} of the letters in your word") # should only return one 
print(f"There are {letterA} letter A's in your word")




                
        


