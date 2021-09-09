from abc import ABC, abstractmethod


class vegetation(ABC):
    @abstractmethod
    def location(self):
        pass
    @abstractmethod
    def growthSpeed(self):
        pass
    @abstractmethod
    def latinName(self):
        pass

class tree(vegetation):
    def location(self):
        self.location = location
        if location == "tropical":
            print("Grows in tropical regions")
        elif location == "temperate":
            print("Grows in temporate regions")
        elif location == "cold":
            print("Grows in cold regions")
        elif location == "artic":
            print("Grows in the artic conditions!")
        else:
            print("Sorry I didnt catch that, please try and enter location again")

    
    def latinName(self, latinName):
        self.latinName = latinName
        print(f"The latin name for this tree is {latinName}")

    def growthSpeed(self, speed):
        self.speed = speed
        if speed == "fast":
            print("This is a fast growing species of tree")
        elif speed == "medium":
            print("This is a medium speed growing species of tree")
        elif speed == "slow":
            print("This is a slow growing species of tree")
        else:
            print("Sorry I didnt catch that, please try and speed of growth again")

    def seasonal(self, type):
        self.type = type
        if "dec" in type:
            print("A deciduous tree")
        elif "ever" in type:
            print("An evergreen tree")
        else:
            print("Sorry I didnt catch that, please try and enter seasonal type again")

    def fruit(self, bearsFruit):
        self.bearsFruit = bearsFruit
        if bearsFruit == False:
            print("This tree isnt a fruit tree")
        elif bearsFruit == True:
            print("This is a fruit tree")
        else:
            print("I'm not sure if that tree bears fruit")
    
    def foliage(self, colour):
        self.colour = colour
        print(f"This tree has {colour} leaves")

apple = tree()
leaves = apple.foliage("light green")
fruit = apple.fruit(True)
latin = apple.latinName("Malus domestica")
growth = apple.growthSpeed("medium")
season = apple.seasonal("deciduous")
zone = apple.location("temperate")


print(leaves)
print(fruit)
print(latin)
print(growth)
print(season)
print(zone)
#class flowers():
    #def __init__(self):
    
   # def location(self):

   # def growthSpeed(self):
#  def prennial(self):

  #  def colour(self):

   # def foliage(self):

#def shrubs():
  #  def __init__(self):
    
   # def location():

    #def growthSpeed():

    #def height():

   # def spiky():