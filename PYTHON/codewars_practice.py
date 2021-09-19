def narcissistic( value ):
    # Code away
    asStr = str(value) # turn the number into a string
    length = len(asStr) # get the length of that string
    length = int(length)
    print(length)
    out = 0
    for i in asStr: # iterate over the string
        singleAnswer= 0 # set the variable to 0
        singleAnswer = int(i) # add the integer you are working on at the moment to a variable
        print(singleAnswer)
        answer = singleAnswer ** length
        print(answer)
        out = out + answer
        print(out)
    if out  == int(value):
        return True
    else:
        return False

print(narcissistic(153))


#Kata - to capitalise each 1st letter in a word

import re
def titlecase(s): ## this method titlecase fixes the bug with title that also capitalises the letters after apostrophes
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        s)

def to_jaden_case(string):
    
    answer = titlecase(string)
    return answer


def song_decoder(song):
    words = song.replace(" ", " ")
    words1 = words.replace('WUB', ' ')
    words2 = words1.replace("  ", " ")     
    words3 = words2.replace("   ", " ") 
    answer = words3.strip()
    return answer 

print(song_decoder("YYRTSMNWU  C  C  FSYUINDWOBV  F  AU  V  JB"))


def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    maximum =  str(max(num_list))
    minimum = str(min(num_list))
    return maximum + " " + minimum 

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

import math
def find_next_square(sq):
    root = math.sqrt(sq)
    if sq % root == 0:
        sqroot = sq + 1
        rt = math.sqrt(sqroot)
        while sqroot % rt != 0:
            sqroot += 1
            rt = math.sqrt(sqroot)
            if sqroot % rt == 0:
                return sqroot
    else:
        return -1
    
print(find_next_square(625))

def filter_list(l):
    answer = [ i for i in l if isinstance(i, (int, float))]
    return answer

print(filter_list([1,2,'a','b']))



##can't do this one! 

def digital_root(n):
    print(n)
    sumOfDigits = 10
    for digit in str(n):
        sumOfDigits = int(sumOfDigits)
        sumOfDigits += int(digit)
        print(sumOfDigits)
        if sumOfDigits >= 10:
            repeat(sumOfDigits)
        else:
            print(sumOfDigits)

def repeat(sumOfDigits):
    sumOD = 0
    for digit in str(sumOfDigits):
        
        sumOD = int(sumOD)
        #print(sumOD)
        sumOD += int(digit)
        #print(f"{digit} + {sumOD - int(digit)} ")
        print(sumOD)
        if sumOD >= 10:
            repeat(sumOD)

##this works though - from the website 
def digital_root2(n):
    return n if n < 10 else digital_root2(sum(map(int,str(n))))  


print(digital_root2(123))