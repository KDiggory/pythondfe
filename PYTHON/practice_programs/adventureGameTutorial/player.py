import items

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Dagger()] # could put anything in starting inventory but only if youve already made the object type in items! 
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp >0

    def print_inventory(self):
        for item in self.inventory:
            print(item, "\n") # this will print each inventory item on a new line

# can now add actions

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        