## The while loop - useful is you dont know how many things you are iterating over.
# perform the loop until the result is true and then stop the loop
inputVar = 0
while inputVar < 35:            # but need something to increment the variable else it will be infinite
    inputVar = int(input("Enter your age: "))

 #incrementing    
inputVar = 0
while inputVar < 50:            # but need something to increment the variable else it will be infinite
   inputVar += 1
   print(inputVar)   # this will ask for your age until you type 35 or more
    

# Practice - testing for primes

testPrime = int(input("Please enter a number: "))
divisorVar = 1
isPrime = 0.5
print(testPrime)

while isPrime != 0:
    divisorVar += 1
    isPrime = testPrime % divisorVar
    print(divisorVar)
if divisorVar == testPrime:
    print(f"{testPrime}  is prime")
else:
    print(f"{testPrime}  is not a prime")


