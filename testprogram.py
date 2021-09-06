#take a user input and print it out backwards

inputString = str(input("What is your input? ")) 

asList = inputString.split()

rev = inputString[::-1] ## this prints it our to one line
print(rev)

#for rev2nd in reversed(inputString):       ## this puts each letter on a different line, not as good
 #  print(rev2)

# test is the output is a palindrome!

if rev == inputString:
   print(f"{True}, your word is a palindrome")
else:
   print(f"{False}, your word is not a palindrome")

   # palindromes - add one number plus the reverse, keep doing this and eventually you will get a palindrome!!
  #456 +654 = 1110
  #1110 + 111 == 1221 



  
 












