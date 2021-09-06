## Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
birthdays = {"Albert Einstein": "14/03/1879", "Benjamin FRanklin": "01/17/1706", "Ada Lovelace": "10/12/1815"}

#def BDlookup (lookup):
    #if lookup in birthdays.keys() = True
#print(birthdays[{lookup}])


# this has indentation errors for some reason!

def BDlookup( lookup ):
    if lookup in birthdays.keys():
        print(birthdays[{lookup}]) 
    Else:
        print("I'm sorry, I don't know that one")
   
 


print(">>>>>> Welcome to the birthday dictionary >>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" ")
print("We know the birthdays of: ")
print("Albert Einstein")
print("Bejnamin Franklin")
print("Ada Lovelace")
lookup = str(input("Whose bithday would you like to look up?"))
BDlookup[lookup]


