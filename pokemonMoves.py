import random, math

class Move():

    def __init__(self, name, category, moveType, power, accuracy, pp):
        self.name = name
        self.category = category
        self.type = moveType
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

    def damagePoints(self, your_pokemon, opponent_pokemon):
        A = your_pokemon.level
        C = self.power

        if self.category == "physical":
            B = your_pokemon.attack
            D = opponent_pokemon.defense
        else:
            B = your_pokemon.special
            D = opponent_pokemon.special
            
        RANDOM = (random.randint(217, 255)) / 255
        STAB = 1    # Same-type attack bonus (update later)
        Y = 1       # Type modifiers (update later)
        
        modifier = RANDOM * STAB * Y

        damage = (((((2*A/5) + 2) *C*(B/D))/50)+2) * modifier

        return math.floor(damage)


#
# Normal-type Moves
#
class Tackle(Move):
    def __init__(self):
        super().__init__(name = "Tackle", category = "Physical",
                 moveType = "Normal", power = 35, accuracy = 95, pp = 35)

class Scratch(Move):
    def __init__(self):
        super().__init__(name = "Scratch", category = "Physical",
                 moveType = "Normal", power = 40, accuracy = 100, pp = 35)

class Gust(Move):
    def __init__(self):
        super().__init__(name = "Gust", category = "Special",
                 moveType = "Normal", power = 40, accuracy = 100, pp = 35)


#
# Status
#

class Growl(Move):
    def __init__(self):
        super().__init__(name = "Growl", category = "Status",
                 moveType = "Normal", power = None, accuracy = 100, pp = 40)

class TailWhip(Move):
    def __init__(self):
        super().__init__(name = "Tail Whip", category = "Status",
                 moveType = "Normal", power = None, accuracy = 100, pp = 30)


