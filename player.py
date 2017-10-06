import time, random
import items, world, pokemon, pokemonMoves

class Player():
    def __init__(self):
        self.pokemon_set = []  # stores Pokemon
        self.inventory = []    # stores items, like potions & pokeballs
        self.location_x, self.location_y = world.starting_position
        self.game_finished = False 
        self.money = 0  # stores money

    def addPokemon(self, pokemon):
        self.pokemon_set.append(pokemon)

    def addItem(self, item):
        self.inventory.append(item)

    def print_inventory(self):
        print()
        if self.inventory == []:
            print("You currently have no items")
        else:
            print("Inventory:")
            for item in self.inventory:
                print("   ", item)
        print()

    def print_pokemon(self):
        print()
        if self.pokemon_set == []:
            print("You currently have no pokemon")
        else:
            print("Pokemon:")
            for pokemon in self.pokemon_set:
                print("   ", pokemon)
        print()

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx = 0, dy = -1)

    def move_south(self):
        self.move(dx = 0, dy = 1)

    def move_right(self):
        self.move(dx = 1, dy = 0)

    def move_left(self):
        self.move(dx = -1, dy = 0)

    def move_downstairs(self):
        self.move(dx = 1, dy = 1)

    def move_upstairs(self):
        self.move(dx = -1, dy = -1)

    #def talk(self, npc): # talk to someone
#        if npc.hasFirstSpeech == True and npc.firstSpeechFinished == False:
#            print(npc.firstSpeech())
#        else:
#            print(npc.speech())

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def endBattle(self, yourPokemon, opponent):
        pass

    def fight(self, yourPokemon, opponent):
        #:param opponent: either a wild Pokemon or the opponent's pokemon
        # returns True if player wins, False if opponent wins

        print("Go, " + yourPokemon.name + "!")
        yourPokemon.currentHP = yourPokemon.hp
        opponent.currentHP = opponent.hp

        while not yourPokemon.checkForDefeat() and not opponent.checkForDefeat():

            # Determines who moves first
            if yourPokemon.speed >= opponent.speed:
                self.playerMove(yourPokemon, opponent)
                if not opponent.checkForDefeat():
                    # Opponent's move
                    opponent.opponentMove(yourPokemon)
            else:
                opponent.opponentMove(yourPokemon)
                if not yourPokemon.checkForDefeat():
                    self.playerMove(yourPokemon, opponent)
                    
        # End of the battle
        if yourPokemon.checkForDefeat(): # if player's Pokemon faints
            print(self, "fainted!")
            print()
        else:  # if opponent's Pokemon faints
            print("Enemy", opponent, "fainted!")
            print()
            yourPokemon.gainExp(opponent) # gain experience points
            yourPokemon.gainEVs(opponent) # gain EVs
            if yourPokemon.canLevelUp(): # see if Pokemon can level up
                yourPokemon.levelUp()

    def playerMove(self, yourPokemon, opponent):
        choice = "A"

        while choice in "ABCDEIP":
            # displays the move choices
            self.print_battle_choices(yourPokemon)
            choice = input("Choice: ")
            print()

            # error checking for choices
            while choice not in "ABCDIP":
                print("Move not available. Try again")
                choice = input("")
                print()

            # If player chooses to use an item
            if choice == "I":
                self.print_inventoryBattle()
                choice = input("Choice: ")
                if choice != "E": # if player chooses to use an item
                    if int(choice) <= len(self.inventory):
                        item = self.inventory[int(choice) - 1]
                        self.useItem(yourPokemon, item)
                        return # end move
                    else:
                        print("Item is not here. Returning to main menu.")
                        continue
                else: # if player chooses to exit
                    continue


            # If player chooses to switch Pokemon
            if choice == "P": 
                self.print_pokemonBattle()
                return #end move
                # switch pokemon

            else: # if player chooses a battle move
                break
                            
        if choice == "A":
            move = yourPokemon.move_set[0]
        elif choice == "B":
            move = yourPokemon.move_set[1]
        elif choice == "C":
            move = yourPokemon.move_set[2]
        elif choice == "D":
            move = yourPokemon.move_set[3]
        else:
            pass
            
        damage = move.damagePoints(yourPokemon, opponent)
        opponent.currentHP -= damage

        # displays and execute player's move
        print(yourPokemon.name, "used", move.name)
        time.sleep(1)
        print("It did", damage, "damage")
        time.sleep(1)
        if opponent.currentHP > 0:
            print("Enemy", opponent.name, "is now down to", opponent.currentHP, "health")
        else:
            print("Enemy", opponent.name, "is now down to 0 health")
        print()
        time.sleep(1)

    
    def print_inventoryBattle(self):
        print()
        if self.inventory == []:
            print("You currently have no items")
            print("E. Exit")
        else:
            print("Which item would you like to use?")
            for i in range(len(self.inventory)):
                print("   " + str(i+1) + ". " + str(self.inventory[i]))
            print("   E. Exit")
        print()

    def print_pokemonBattle(self):
        print()
        print("Which Pokemon would you like to use?")
        for i in range(len(self.pokemon_set)):
            print("   " + str(i+1) + ". " + str(self.pokemon_set[i]))
        print("   E. Exit")
        print()

    def print_battle_choices(self, yourPokemon):
        print()
        print("Which move would you like to use?")
        print()
        print("Fighting:")
        for i in range(len(yourPokemon.move_set)):
            move = yourPokemon.move_set[i]
            print("   ", chr(ord('A') + i) + ".", move.name)

        print("Other:")
        print("   I. Items")
        print("   P. Pokemon")
        print()

    def useItem(self, yourPokemon, item): # general use item
        if isinstance(item, items.HPPotion): # if item is a potion
            self.usePotion(yourPokemon, item)
        #if isinstance(item, items.PokeBall): # if item is a PokeBall
            #caught = self.usePokeBall(opponent, item)
            #if caught:
#                pass
#            else:
                # do nothing?
#                pass
            
        self.inventory.remove(item) # remove item from inventory

    def usePotion(self, yourPokemon, potion):
        print("You used " + str(potion) + "!")
        yourPokemon.currentHP += potion.value
        if yourPokemon.currentHP > yourPokemon.hp:
            yourPokemon.currentHP = yourPokemon.hp
        print(str(yourPokemon) + "'s health is now " + str(yourPokemon.currentHP) + "!")
"""    
    #def usePokeBall(self, opponent, item):
#        if isinstance(item, items.MasterBall): # Master Ball
#            # pokemon is caught
#        elif isinstance(item, items.RegularBall): # Regular PokeBall
#            n = random.randint(0, 255)
#            ball = 12
#            missedBall = 255
#        elif isinstance(item, items.GreatBall): # Great Ball
#            n = random.randint(0, 200)
#            ball = 8
#            missedBall = 200
#        else: # Ultra Ball
#            n = random.randint(0, 150)
#            ball = 12
#            missedBall = 150

        # The Pokemon is caught if:
        #     it is asleep or frozen and N is less than 25
        #     it's paralyzed, burned, or poisoned, and N is less than 12
        # Otherwise, if N - status threshold (above) is greater than the Pokemon's catch rate,
        # the Pokemon breaks free

        m = random.randint(0, 255)
        f = int((opponent.hp * 255 * 4) / (opponent.curentHP * ball))

        if f >= m: # Pokemon is caught
            self.pokemon_set.append(opponent)
            
            time.sleep(1)
            print("Shake 1...")
            time.sleep(1)
            print("Shake 2...")
            time.sleep(1)
            print("Shake 3...")
            time.sleep(3)
            print("Gotcha!", opponent, "was caught!")

            return True
        
        else: # Pokemon breaks free
            
            # Calculates how many times the ball will shake
            d = opponent.catchRate * (100 / missedBall)

            if d >= 256: # the ball will shake 3 times before breaking
                time.sleep(1)
                print("Shake 1...")
                time.sleep(1)
                print("Shake 2...")
                time.sleep(1)
                print("Shake 3...")
                time.sleep(3)
                print("The Pokemon broke free!")
                time.sleep(.5)
                print("Shoot! It was so close too!")
            else:
                x = d * (f / 255)
                if x < 10: # Ball misses the Pokemon completely
                    time.sleep(.5)
                    print("You missed the Pokemon!")
                elif x < 30: # Ball shakes once
                    time.sleep(1)
                    print("Shake 1...")
                    time.sleep(2)
                    print("The Pokemon broke free!")
                    time.sleep(.5)
                    print("Aww! It appeared to be caught!")
                elif x < 70: # Ball shakes twice
                    time.sleep(1)
                    print("Shake 1...")
                    time.sleep(1)
                    print("Shake 2...")
                    time.sleep(2)
                    print("The Pokemon broke free!")
                    time.sleep(.5)
                    print("Aargh! Almost had it!")
                else:
                    time.sleep(1)
                    print("Shake 1...")
                    time.sleep(1)
                    print("Shake 2...")
                    time.sleep(1)
                    print("Shake 3...")
                    time.sleep(3)
                    print("The Pokemon broke free!")
                    time.sleep(.5)
                    print("Shoot! It was so close too!")

            return False
                    
                
 """                   
            
                    
                    
            
        




"""

def main():
    p = Player()
    p.addPokemon(pokemon.Bulbasaur(5))
    p.addItem(items.Potion())
    r = pokemon.Rattata(6)
    p.fight(p.pokemon_set[0], r)

main()
"""



    


    
