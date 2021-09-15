# Procedures and functions
# split the code into small 'methods' --> Keeps the code dry and not repeating yourself. If a method is defined it is easier to debug as well

def testz(testVar):  ## define your procedure, needs brackets and a colon. The brackets dont have to have a value
    print(testVar)
    if testVar < 5:
        exit()

# this function can then replace each instance of if z < 5 print and exit

def sausage():      # this procedure doesnt take an input, it just prints out. 
    print("sausage")


x = 1000
y = 2000
z = x + y
#print(z)
#if z < 5: # built in function to quits the program straight away
   # exit()
z = y- x
testz(z) # this is a faster and more streamlined way to write the code --> looks neater and easier to read
sausage()
#print(z)
#if z < 5:
 #   exit()
z = y * (x/2)
testz(z)
#print(z)
#if z < 5: 
 #   exit()
z = x * x
testz(z)
#print(z)
#if z < 5: 
    #exit()
z = y * y
testz(z)
#print(z)
#if z < 5: 
    #exit()