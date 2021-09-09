user_funds = 10.31

# this doesnt run because price is not defined. Need to do that first

def price(Burger):
    print("How much does it cost? ")
    Burger = int(input(">"))
    return Burger

item_price = price("Burger")

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
else: 
    print("Sorry you don't have enough money")