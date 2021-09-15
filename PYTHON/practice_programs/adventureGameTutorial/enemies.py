#make a new class for enemies - a new class as you dont call the parent class when you make it

class Enemies:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive():
        return self.hp >0

class GiantSpider(Enemies):
    def __init__(self):
        super().__init__(name="Giant Spider", hp = 10, damage = -2)

class Ogre(Enemies):
    def __init__(self):
        super().__init__(name="Ogre", hp = 30, damage = -10)
# dont have to include the is_alive method as they inherit that from the parent class

