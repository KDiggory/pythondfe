import items, enemies 

class MapTile: # will provide a template for all the tiles in our world. which means we need to define the methods all tiles will need. 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError() # this will be shown if we try and directly implement a map tile - we will always want them to be a subclass!

    def modify_player(self, player): # the player parameter is acting as a placeholder here. will crash the program if run now - but tells us where we will want it later. 
        raise NotImplementedError()

    # the first tile class
class StartingRoom(MapTile): # a subclass of the MapTile class
    def intro_text(self):
        return """ You awake to find yourself in a darkened room, a flickering torch on the wall.
            You can see 4 possible routes out of the room. Each is dark and foreboding"""
    def modify_player(self, player):
            # room has no action on player
        pass # tells python not to do anything - needs to be there because if the superclass modify_player isnt overridden then it will show the error
    # this is the starting maptile - we will override the intro_text in the rest of them!
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot():
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player) # overriding the superclass method with an actual method rather than pass

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
    
    def modify_player(self, the_player):
        if self.enemy.is_alive(): ## this is there so that the enemy doesnt respawn if you go back to that tile! 
            the_player.hp = the_player.hp - self.enemy.damage
            print(f"The Enemy does {} damage. You have {} health remaining".format(self.enemy.damage, the_player.hp))
    
class EmptyCave(MapTile):
    def intro_text(self):
        return""" More empty cave, you move forwards into the darkness
        """
    
    def modify_player(self, player):
        pass

class EmptyDampCave(MapTile):
    def intro_text(self):
        return """ This part of the cave is very wet, better move on else your gear will get wet!
        """
    def modify_player(self, player):
        pass

class GiantSpiderRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return""" A gigantic spider drops from the ceiling of the cave to the ground in front of you
            """
        else:
            return """
            The corpse of a recently killed spider lays on the ground infront of you"""

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
    
    def intro_text(self):
        return """
        You notice a dull dagger on the floor, examining it you see it is a very good weapon if
        in need of a little tlc"""

class OgreRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre)

    def intro_text(self):
        if self.enemy.is_alive():
            return """
        You walk into the room and a giant ogre looks up from what it was doing, which you see was knawing on bones that look suspiciously human.
        The beast slowly gets to its feet and starts to lumber towards you making a low grumble"""
        else:
            return """ The body of the vanquished ogre lies on the ground before you"""

class GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold())

    def intro_text(self):
        return """You find a small pouch of gold! Yippee"""

    

    

