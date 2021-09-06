number = int(input("type a number: "))
count = 0
while str(number) != str(number)[::-1]:
    
    number = int(number) + int(str(number)[::-1])
    count = count + 1
    print(f"checking {number}")
print("Palindrome found in " + str(count) + " steps. Final number was: " + str(number))