from budgetCalculator import budgetApp

food = budgetApp("Food")
#entertainment = budgetApp("Entertainment")
clothes = budgetApp("Clothing")
bills = budgetApp("Bills")
food.withdraw(1)
#bills.withdraw(10)
bills.transfer(clothes, 2)
bills.deposit()

reciepts = food.reciepts

print(f"Food balance: {food.balance}")
print(f"Bills balance: {bills.balance}")
print(reciepts)

