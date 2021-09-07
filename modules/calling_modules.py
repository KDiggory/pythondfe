#Importing functions into your code
#the python interpreter knows where these modules are stored so you can call them using import

import random ## can type import and then the first letter and vscode will tell you the options

print(random.random()) ## you then get the same for methods

# can also use the help output on the command line - but will need to import the method on the commandline 1st

import math
print(math.cos(1)) # it will tell you what arguments you need for each thing
print(math.pi) # prints pi - as a fixed variable output


# another way to do it

import namemodule

namemodule.numCheck("Input")
namemodule.nameCheck("Input")

## if there are more than one method in the file then you can call each method in a file separately.

# it can also be done using from
from namemodule import nameCheck # then you dont have to tell it what module its coming from, brings that function into the current scope
nameCheck("only") # this then doesnt need to have namemodule.nameCheck. Its as though you've written the function in this file

# can also put an alias!
from namemodule import random as randomprint 
randomprint()

# cant then call in another function using from x import y 
random("A string") ## comes out as random.random takes no arguments, one given.

# To get around this you set an alias for the one with the problem name

