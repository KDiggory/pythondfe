
from budgetCalculator import budgetApp


def start():
    print("Welcome to your budget app!")
    print("What account would you like to change today?")
    print("Food - please select 1")
    print("Entertainment - please select 2")
    print("Bills - please select 3")
    print("Clothing - please select 4")
    accChoice = input(">")
    if accChoice == 1:
        print("Thank you for selecting the food account")
        food()
    elif accChoice == 2:
        print("Thank you for selecting the entertainment account")
        entertainment()
    elif accChoice == 3:
        print("Thank you for selecting the bills account")
        bills()
    elif accChoice == 4:
        print("Thank you for selecting the clothing account")
        clothing()
    else:
        print("Sorry, I didn't get that, would you like to start again?")
        startAgain = input(">")
    if "y" in startAgain:
        restart()
    if "n" in startAgain:
        exit()
    else:
        restart()

def food():
    print("You are now making changes to your food account. Do you want to continue? ")
    foodanswer = input(">").lower
    if "n" in foodanswer:
        restart()
    else:
        print("What would you like to do? ")
        print("Deposit - select 1 ")
        print("Withdraw - select 2 ")
        print("Transfer - select 3 ")
        foodanswer2 = input(">")
        if foodanswer2 == 1:
            print("Making a deposit")
            fooddeposit = input(budgetApp.deposit)
            return fooddeposit
        elif foodanswer2 == 2:
            print("Making a withdrawl")
            foodwithdrawl = input(budgetApp.withdraw)
            return foodwithdrawl
        elif foodanswer2 == 3:
            print("Making a transfer")
            foodtransfer = input(budgetApp.transfer)
            return foodtransfer

def entertainment():
    print("You are now making changes to your entertainment account. Do you want to continue? ")
    entanswer = input(">").lower
    if "n" in entanswer:
        restart()
    else:
        print("What would you like to do? ")
        print("Deposit - select 1 ")
        print("Withdraw - select 2 ")
        print("Transfer - select 3 ")
        entanswer2 = input(">")
        if entanswer2 == 1:
            print("Making a deposit")
            entdeposit = input(budgetApp.deposit)
            return entdeposit
        elif entanswer2 == 2:
            print("Making a withdrawl")
            entwithdrawl = input(budgetApp.withdraw)
            return entwithdrawl
        elif entanswer2 == 3:
            print("Making a transfer")
            enttransfer = input(budgetApp.transfer)
            return enttransfer

def clothing():
    print("You are now making changes to your clothing account. Do you want to continue? ")
    clothinganswer = input(">").lower
    if "n" in clothinganswer:
        restart()
    elif "y" in clothinganswer:
        print("What would you like to do? ")
        print("Deposit - select 1 ")
        print("Withdraw - select 2 ")
        print("Transfer - select 3 ")
        clothinganswer2 = input(">")
    if clothinganswer2 == 1:
        print("Making a deposit")
        clothdeposit = input(budgetApp.deposit)
        return clothdeposit
    elif clothinganswer2 == 2:
        print("Making a withdrawl")
        clothwithdrawl = input(budgetApp.withdraw)
        return clothwithdrawl
    elif clothinganswer2 == 3:
        print("Making a transfer")
        clothtransfer = input(budgetApp.transfer)
        return clothtransfer
    else:
        restart()

def bills():
    print("You are now making changes to your bills account. Do you want to continue? ")
    billanswer = input(">").lower
    if "n" in billanswer:
        restart()
    elif "y" in billanswer:
        print("What would you like to do? ")
        print("Deposit - select 1 ")
        print("Withdraw - select 2 ")
        print("Transfer - select 3 ")
        billanswer2 = input(">")
    if billanswer2 == 1:
        print("Making a deposit")
        billsdeposit = input(budgetApp.deposit)
        return billsdeposit
    elif billanswer2 == 2:
        print("Making a withdrawl")
        billswithdrawl = input(budgetApp.withdraw)
        return billswithdrawl
    elif billanswer2 == 3:
        print("Making a transfer")
        billstransfer = input(budgetApp.transfer)
        return billstransfer
    else:
        restart()

def restart():
        print("Do you want to restart the process?")
        restartanswer = input(">")
        if "y" in restartanswer:
            start() # answer will send you to next function
        elif "m" in restartanswer:
            quit()
        else:
            print("Do you want to restart the process?")
            restart()

def quit():
    exit()


test = budgetApp("test")
start(test)
