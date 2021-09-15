class UserInput:

class Numbers(UserInput):

def numbers():
    print("What number would you like to choose?")
    num1 = float(input(">"))
    print("and another please")
    num2 = float(input(">"))
    print("do you want to add a another number?")
    answer = str(input(">"))
    if "y" in answer:
        print("Ok great, whats that number then?")
        num3 = float(input(">"))
    elif "n" in answer:
        print("Great, I can work with just 2 numbers!")
    calculation()
    return num1, num2, num3

class Calculation(UserInput):
    def calculation():
        print("What kind of calculation would you like to do")

class ComplicatedCalculation(UserInput):

class Maths:




class Multiplication(Maths):

class Subtraction(Maths):

class Addition(Maths):

class Division(Maths):

