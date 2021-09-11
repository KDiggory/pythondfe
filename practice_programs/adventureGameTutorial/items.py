
class Character():
    ## This is a class that represents the main character in a game.
    def __init__(self):
        # This is a method that sets up the variables in the object.
        self.name = "Link"
        self.sex = "Male"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8

class Item:
    # this will be the base class for all items
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
# the __str__ method allows us to print an object and see some useful information
    def __str__(self):
        return "{}\n=====: {}\n".format(self.name, self.description, self.value, self.weight)

#make a child class of the Item class. 
class Gold(Item):
    def __init__(self, amt): # extra parameter is the amount of gold
        self.amt = amt
        # superclass constructor is called here. We set the values for the variables. If the constructors are the same it will be done automatically, else we have to do it
        super().__init__(name = "Gold", description = "A round coin with {} stamped on it".format(str(self.amt)), value = self.amt, weight= (self.value/5))

# another class for weapons as these will have an extra attribute - damage and type
# extend the Item class again
class Weapon(Item):
    def __init__(self, name, description, value, damage_type, damage):
        self.damage = damage
        self.damage_type = damage_type
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDamage Type: {}".format(self.name, self.description, self.value, self.damage, self.damage_type) 

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger", description = "A small metal dagger, very common", value= 5, damage=1, damage_type = "stabbing")

class Short_sword(Weapon):
    def __init__(self):
        super().__init__(name="A metal short sword with carved bone pommel, seen better days", value = 10, damage = 5, damage_type = "slashing" )


    

    
