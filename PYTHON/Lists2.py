##Lists

foodshoppingList = ["chicken", "carrotts", "sausages", "beer", "pies", "pasta"]

print(foodshoppingList[1:3]) ## prints the values at index 1 and 2, number 3 is not included

homeList = ["spray", "loo roll", "bedding"]
funList = ["chocolate", "wine", "new clothes"] 

shopping = [foodshoppingList, homeList, funList] ## makes a multi d. list 

print(shopping[0][0]) ## prints chicken
print(shopping[0][3]) ## prints beer
print(shopping[1][2]) ## prints bedding
print(shopping[2][0]) ## prints chocolate

foodshoppingList.append("bananas") ## add to the end
funList.insert(3, "gin") ## insert at index 3
print(foodshoppingList)

jobs = "tidy kitchen", "washing", "make doors" ##this is a tuple - not used that often

#### Key values lists ####


user1 = {'name':"Katie", 'age':33} # the keys are name and age, the values are Katie and 33
user2 = {'name':"George", 'age':32}
user3 = {'name':"Huxley", 'age':3}
user4 = {'name':"Oswin", 'age':1}
print(user1['name']) # prints the key for that entry
print(user2.values()) # prints the values for that entry
print(user3.keys()) # prints the keys for that entry

user1['name'] = "Katherine" ## changes the value at that key for the particular entry 
print(user1['name']) # prints the key for that entry

user1['role'] = "mum"
user2['role'] = "dad"

print(user2.values()) # prints the values for that entry
print(user2.keys()) # prints the keys for that entry







