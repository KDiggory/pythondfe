# Goal: “Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number of balls of each color that 
# are in the hat. Give the object the ability to pick a random number of balls from the hat, which will then be used to compute the 
# probability of picking a certain distribution of balls over a large number of experiments”

# Considerations: this is a very interesting project as it allows not only to comprehend how a class is initialized and used, but also 
# represented and used as input to other functions. You will learn how to add methods to your classes and print them in a way that allows 
# complex representation of your class object at different points in the program. As a bonus, you will define a function that computes 
# how much money you are spending across class categories as a % of your total expenses, something that can be very useful for the 
# money-savvy programmers among you.

# Approach: define the purpose and flexibility of a class object; build its class methods using a modular approach and develop an understanding
#  for how different instances of the same class can interact.

# Key concepts: Class initialization, instance methods and instance representation. Defining and using functions that take class instances as 
# input parameters

class budgetApp:
    def __init__(self, name):
        self.name = name 
        self.balance = float(input(f"Enter budget for {name} :"))
        self.reciepts = []  

    def deposit(self):
        depositAmount = int(input("How much would you like to deposit? "))
        if depositAmount == "":
            print("Deposit cancelled")
        else:
            self.balance += depositAmount 
        print(f"Thank you for depositing {depositAmount}")    


    def withdraw(self, spent):
        purchase = str(input("What do you want to buy? "))
        if spent > self.balance:
            print("Insufficient funds")
        elif spent < self.balance: 
            self.balance -= spent
            self.reciepts.append(f"{purchase} : {spent}")
            return self.reciepts
        
    def transfer (self, other, amount):
        if amount > self.balance:
            print(f"Insufficient funds, please make a transfer into the {other} account")
        elif amount < self.balance:
            self.balance -= amount
            other.balance += amount 

    