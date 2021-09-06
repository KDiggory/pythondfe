# looping

listVar = ["bananas", "screwdriver", "pies", "keys", 100, 1000001]

for itemVar in listVar:
    print(itemVar)

# strings as lists
strVar = "Bannnnnnnnnnnnnna" ## because a string is a list of letters

for s in strVar:
    print(s.upper())

# tuples

tupleVar = ("bananas", "screwdriver", "pies", "keys", 100, 1000001)
for t in tupleVar:
    print(t)

# dictionaries - harder to use loops are dictionaries arent held in a particular order
dictVar = {"name":"Katie", "age": 33, "address":"Inglenook"}
print(dictVar.keys()) # cant use a dictionary directly but you can use methods indirectly
# this takes the keys and turns them into a list, which can then be used to iterate over to print each
for d in dictVar.keys():
    print(dictVar[d])
   
# using range with for loops - job is to produce a list of numbers

for n in range(0,101,10): ## the 3rd part of this range is the stride -- the step between things to do 
    print(n) # prints to 100 in 10s

# key words
# break

for n in range(1,50):
    print(n)
    if n == 42:
        break ##this stops the output when the conditional is met

listVar2 = [ "go", "go","go","go","go","go","go","go","stop","go","go","go","go",]

for l in listVar2:
    print(l)
    if l == "stop":
        break ##this stops the output when the conditional is met

for l in listVar2:
    if l == "go":
        continue
    print(l) ## just prints stop as it isnt go

# for loop is most useful if you know how many things you are iterating through.

       