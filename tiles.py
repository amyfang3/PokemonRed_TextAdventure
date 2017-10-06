# Describes the tiles in the world space

import random, items, pokemon, actions, world, NPC

#########################
# Abstract Base Classes #
#########################
class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.npc = []

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    # Returns all move actions for adjacent tiles
    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveRight())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveLeft())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        
                    
        return moves

    # Returns all of the available actions in this room
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewPokemon())
        #if self.npc != []:
#            for npc in self.npc:
#                moves.append(actions.Talk(npc))

        return moves

class Inside(MapTile):
    # Basis for indoors
    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveRight())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveLeft())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())        

        return moves

class FirstFloor(Inside):
    def adjacent_moves(self):
        moves = super().adjacent_moves()
        if isinstance(world.getTile(self.x - 1, self.y - 1), SecondFloor) and world.tile_exists(self.x - 1, self.y - 1):
            moves.append(actions.MoveUpstairs())

        return moves

class SecondFloor(Inside):
    def adjacent_moves(self):
        moves = super().adjacent_moves()
        if isinstance(world.getTile(self.x + 1, self.y + 1), FirstFloor) and world.tile_exists(self.x + 1, self.y + 1):
            moves.append(actions.MoveDownstairs())

        return moves

class WildGrass(MapTile):
    # May or may not contain a wild pokemon
    # Basis for all routes
    
    CHANCE_OF_WILD_POKEMON = 75 # There's a 75% chance of encountering wild Pokemon
    
    def __init__(self, x, y, wildPokemon):
        super().__init__(x, y)
        self.wildPokemon = wildPokemon
        self.hasPokemon = False

    def modify_player(self, player):
        if player.pokemon_set == []:
            print("You don't have Pokemon! It's not safe here! Go back to town!")
        else:
            enemy = random.choice(self.wildPokemon)
            chance = random.randint(1, 100)
            if chance <= 50:
                print("A wild", enemy.name, "has appeared!")
                print()
                player.fight(player.pokemon_set[0], enemy)


##################
# Specific Tiles #
##################


#
# Pallet Town
# 

class PlayerBedroom(SecondFloor):
    def intro_text(self):
        return """
        You are in your bedroom. Light shines in through the window.
        There's a PC in the corner and a SNES in front of your TV.
        There's some stairs in the east leading downstairs to the living room.
        """
    
    def modify_player(self, player):
        # Room has no action on the player
        pass

class PlayerHouse(FirstFloor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.npc.append(NPC.PlayerMom())
        
    def intro_text(self):
        return """
        You walk downstairs to the living room. Your mom is sitting at the table.

        There's a door leading outside.
        """
    def modify_player(self, player):
        pass

class PalletTown(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return """
        You're in the center of Pallet Town. There's a sign that says:
        
        PALLET TOWN
        Shades of your journey await!

        You can see your house, Gary's house, and Professor Oak's laboratory.
        """

    def modify_player(self, player):
        pass

class OakLaboratory(FirstFloor):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return """
        You walk into Oak's laboratory. Assistants are all around working on something.
        You see PROF. OAK in the distance.
        """

    def modify_player(self, player):
        if player.pokemon_set == []:
            choice = input("""There are 3 Pokemon on the table.
        There is a Bulbasaur, a Charmander, and a Squirtle.
        Which one would you like?
                     """)
            if choice == "Bulbasaur":
                print("You received a BULBASAUR!")
                player.addPokemon(pokemon.Bulbasaur(5))
            elif choice == "Charmander":               
                print("You received a CHARMANDER!")
                player.addPokemon(pokemon.Charmander(5))
            else:
                print("You received a SQUIRTLE!")
                player.addPokemon(pokemon.Squirtle(5))


class GaryHouse(FirstFloor):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return """
        You walk into Gary's House. Gary's sister is sitting at the table, looking at a piece of paper
        """

    def modify_player(self, player):
        pass


#
# Route 1
#

class Route1(WildGrass):
    wildPokemon = [pokemon.Pidgey(2), pokemon.Pidgey(3), pokemon.Pidgey(4), pokemon.Pidgey(5),
                   pokemon.Rattata(2), pokemon.Rattata(3), pokemon.Rattata(4)]
    
    def __init__(self, x, y):
        # Tile where wild pokemon live
        # :param x: x-coordinate
        # :param y: y-coordinate
        super().__init__(x, y, wildPokemon = self.wildPokemon)

    def intro_text(self):
        return """
            You are on Route 1.
            A pleasant breeze blows through the grass.
            """

    
            

    


