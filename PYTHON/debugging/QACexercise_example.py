# Debug the following programs. For the first 2 perform static analysis. For the 3rd and 4th exercises use dynamic analysis either manually or through PDB.
#import pdb
#pdb.set_trace()

def tailRecursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
    if factorial == 1:
        return result
    else:
        return tailRecursion((factorial- (factorial + result)))

def tailRecursion(factorial, result = 1):
    if factorial == 1:
        return result
    else:
        tempResult = factorial * result
        return tailRecursion((-factorial), tempResult)