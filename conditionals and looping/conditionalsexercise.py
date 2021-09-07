devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to play smash")
else:
    print("Dev just can't play smash")

mark = int(input("What mark did you get? "))
if mark > 85:
    print("Distinction")
elif mark >= 65 and mark <= 85:
    print("Pass")
else:
    print("Fail")


## practices from online

# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

n1=[]
for n in range(1500,2701):
    if (n%7==0) and (n%5==0):
        n1.append(str(n))
print(",".join(n1))

## Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

temp = int(input("What temperature in would you like to convert? "))
type = str(input("And what unit is that? "))
capType = upper.type

if capType == "C":
    c1 = int((9 * temp)/5 +32)
    print(f("The temperature is " + c1 + " farenheit"))
if capType == "F":
    f1 = 
   



