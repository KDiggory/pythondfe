# A python class is like a blueprint for something you want to build
# its not used directly but is used to create an object
# the object is then used for the task you weant to perform
#the class itself can be pulled into multiple objects
# and then those slightly different objects can be used within the program

# building an application to show the weather in a particular location for 3 days
# not going to build a network of little machines and dot around world to get weather --> will use someone elses data
# eg, sign up for a developer account with the met office, us NOA, indian weather bureau.
# from these companies will need username/password and url to log into - 3 bits of information
# could write 3 functions to log you into the 3 places and write program to iterate on those --> so 3 times!
# classes can create 3 objects, 1 for each place to login. In the code these objects will work the same, but will each be named differently. 
# the class is the blueprint for 'this is how you log into a service'


## objects in python - all objects can have data associated with them, but also functions and procedures associated with them eg .upper and .lower for strings!

# Dog:
    # Attributes:
     # - Breed
     # - Weight
     # - Energy

# From this class we can create usable objects

# Bilbo Waggins:
# Breed: LAbrador
# Weight: 80kgs
# Energy: Low

# Classes group together attributes and methods - which can be used many times. Better than creating unique variables to replace the attributes given by the class - would also need lots of functions to replace the methods defined in the class
# produces tons of duplicated code = bad practice

# in a class functions = methods, variables = attributes

class Dog:          # this class can be in a separate module if wanted

    def __init__(self, name, energy, breed ="Cross breed"):  # can set up attributes in the init method - its done before the other method, can set defaults here
        print("I live")
        self.name = name 
        self.energy = energy
        self.breed = breed

    def speak(self, dognoise): # the self variable lets you know you are dealing with an attribute in the class  becuase dognoise is in the parameter already you can call that
        dogsay = f"I like to say {dognoise}, my energy is {self.energy}"
       #return "woof" # need to return the variable so that it can be used outside the class
        return dogsay

bilbo_waggins = Dog("Bilbo Waggins", "Low", "Hound") # can now use bilbo_waggins) as an object

# help(bilbo_waggins) # can call help on it to see what is in there
bilbo_waggins.speak("Woof") # prints woof
dogNoise = bilbo_waggins.speak("Woof") # set the returned variable to a new variable
print(f"The Dog says {dogNoise}") # can then use the new variable
havoc = Dog("Havoc Robinson", "Ultimate", "Cavapoo")
havocsNoise = havoc.speak("Yippee")

# self says you are talking about that particular dog - not all dogs

# this no longer works after playing with the self.  



