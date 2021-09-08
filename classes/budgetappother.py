from budgetCalculator import budgetApp

food = budgetApp("Food")
#entertainment = budgetApp("Entertainment")
#clothes = budgetApp("Clothing")
bills = budgetApp("Bills")
food.withdraw(20)
#bills.withdraw(10)
food.transfer(bills, 20)
reciepts = food.reciepts
print(food.balance)
print(bills.balance)
print(reciepts)
#beer = food.withdraw(20)
#print(f"Your balance is: {food.")

#reciepts = food(reciepts)

#entertainment = budgetApp("Entertainment")

#cinema = entertainment.transfer(food, 20)