mark = int(input("What is your mark? "))

if mark > 85:
    print("Distinction")
elif mark >= 65 and mark < 85:
    print("Pass")
else:
    print("Fail :( ")