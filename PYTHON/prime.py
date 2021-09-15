bigListOPrimes = []
for testPrimeRange in range(2,1001):

    divideRemainder = 0.5 # resets the variables each loop
    divisorVar = 1

    while divideRemainder != 0: # is the remainder 0? if not keep running the test
        divisorVar = divisorVar + 1 # increment the divisor to 2 to testPrime
        divideRemainder = testPrimeRange % divisorVar # divide the testPRime by the divisor and store the remainder

    if divisorVar == testPrimeRange: # if devisorVar (the incremented number) is equal to a number in the range
        print(f"{testPrimeRange} is prime") # then it must be a prime number 
        bigListOPrimes.append(testPrimeRange)

print(bigListOPrimes)
primeCount = len(bigListOPrimes)
print(f"I have {primeCount} primes")
bigPrime = bigListOPrimes[-1]
print(f"My biggest prime is {bigPrime}")

