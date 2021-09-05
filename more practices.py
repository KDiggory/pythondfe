## write a function that takes an ordered list of numbers and another number. The function decides whether
## or not the given number is insite the list and returns the approipriate boolean

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#number = int(input("What number would you like to check? "))
# this didnt work :( )
check = [] 
inList = list.count(number)
for i in range(inList):
    if i >= 1:
         print(True)
    else: 
        i < 1 == False
        print(False)

check[4]


# this is the answer
def find(ordered_list, element_to_find): # define the function
  for element in ordered_list: # for each element in the list
    if element == element_to_find: #if the element is the same as the input
      return True #return true
  return False  #else return false
  
if __name__=="__main__": ## what does this do????
  l = [2, 4, 6, 8, 10] ## this is the list 
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  print(find(list, 10)) # prints True
  print(find(list, -1)) # prints False
  print(find(list, 2)) # prints True

   ##Implement a function that takes input of 3 variables and returns the largest of the 3 without using the max() function
# will need variables and if statements
var1 = int(input("first number pleaase "))
var2 = int(input("Second number please "))
var3 = int(input("And your last number "))

if 
