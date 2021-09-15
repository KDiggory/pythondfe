## modules - very useful for bringing things into your code
##cant have hyphens in the filename you want to import, can have underscores if needed
#python has a load of modules that you can import as well - these are 


def nameCheck(inName): ## inName is a python inbuilt variable
    while True:
        name = str(input(f'Enter the {inName} name \n')).lower()
        if not name.isalpha():  # if it's not just letters then print message
            print('Alphabet charactors only please! Not even spaces.')
        else:
            return name  # this breaks out the loop


# can put more than one function in a file but this may also get run! --> Much better to write each function in its own module. 

def numCheck(inName): ## inName is a python inbuilt variable
    while True:
        name = str(input(f'Enter the {inName} name \n')).lower()
        if not name.isdigit():  # if it's not just letters then print message
            print('Numbers only please! Not even spaces.')
        else:
            return name  # this breaks out the loop

def random():
    print("This is random!")




