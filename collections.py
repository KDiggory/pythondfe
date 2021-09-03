## collections ##

## dictionaries
books = {"The very hungry caterpillar":"Eric Carle", "Superworm":"Julia Donaldson", "The Goblin stories":"George Diggory", "The tiger who came for tea":"Judith Kerr"}
print(books["The very hungry caterpillar"]) # prints the value for this key

print(books["Eric Carle"]) ## gives a key error --> because this is a value not a key

books["Lord of the rings"] = " JRR Tolkein"


### Sets ####
# similar to lists but - unordered, not duplicated, not multi d

items = ["biro", "paper", "apple", "biro", "apple"]

set(items) ## duplicates removed and order changes each time you run this command

numSet = {1,2,3,4,5}
numSet.add(6)  ## this is two ways of adding to a set
numSet |= {7} ## this is the second one 

numSet.remove(5) ## this removes number 5
numSet.discard(6) ## also removes something, but doesnt error if not found
numSet -= {4} ## also removes

## operators
# & operator
print({1,2,3} & {1,2,4}) ## {1,2} - shows elements in both sets
print({1,2,3} | {1,2,4}) ## {1.2.3.4} - shpws elements in either set
## - is difference --> elements only in the 1st set
## ^ symmetric difference, elements contained in either set
print({1,2,3} >= {1,2}) ## prints true as >= (superset) - first set contains all elements from second set?
print({1,2,3} > {1,2,3,4}) ## prints false as some in 2nd are not in first
print({1,2,3} <= {1,2}) # prints false as not all from 2nd set are in first set
print({1,2,3} < {1,2,3}) # prints false. Strict subset
print({1,2,3} < {1,2} ) 
