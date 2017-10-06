from player import Player
import NPC

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super().__init__(method = Player.move_north, name = "Go north", hotkey = 's')

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method = Player.move_south, name = "Go south", hotkey = 'x')

class MoveRight(Action):
    def __init__(self):
        super().__init__(method = Player.move_right, name = "Go right", hotkey = 'c')

class MoveLeft(Action):
    def __init__(self):
        super().__init__(method = Player.move_left, name = "Go left", hotkey = 'z')

class MoveDownstairs(Action):
    def __init__(self):
        super().__init__(method = Player.move_downstairs, name = "Go downstairs", hotkey = 'd')

class MoveUpstairs(Action):
    def __init__(self):
        super().__init__(method = Player.move_upstairs, name = "Go upstairs", hotkey = 'a')

class GoOutside(Action):
    def __init__(self, direction):
        if direction == "north":
            super().__init__(method = Player.move_north, name = "Go outside", hotkey = 's')
        if direction == "south":
            super().__init__(method = Player.move_south, name = "Go outside", hotkey = 'x')
        if direction == "left":
            super().__init__(method = Player.move_left, name = "Go outside", hotkey = 'z')
        if direction == "right":
            super().__init__(method = Player.move_right, name = "Go outside", hotkey = 'c')


class ViewInventory(Action):
    # Print's the player's inventory
    def __init__(self):
        super().__init__(method = Player.print_inventory, name = "View Inventory", hotkey = 'i')
        
class ViewPokemon(Action):
    # Print's the player's pokemon
    def __init__(self):
        super().__init__(method = Player.print_pokemon, name = "View Pokemon", hotkey = 'p')
"""
class Talk(Action):
    # Talks to an NPC
    def __init_(self, NPC):
        NAME = "Talk to " + NPC.getName()
        super().__init__(method = Player.talk, name = "Talk to NPC", hotkey = 't', npc = NPC)
"""

        
