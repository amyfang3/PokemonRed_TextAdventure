class Item():
    # The base class for all items
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

##############
# HP Potions #
##############
class HPPotion(Item):
    def __init__(self, name, description, value):
        self.value = value
        super().__init__(name, description)

class Potion(HPPotion):
    def __init__(self):
        super().__init__(name = "Potion",
                     description = "Heals a Pokemon by 20 HP",
                     value = 20)
        

class SuperPotion(HPPotion):
    def __init__(self):
        super().__init__(name = "Super Potion",
                     description = "Heals a Pokemon by 50 HP",
                     value = 50)

class MoomooMilk(HPPotion):
    def __init__(self):
        super().__init__(name = "Moomoo milk",
                     description = "Heals a Pokemon by 100 HP",
                     value = 100)

class HyperPotion(HPPotion):
    def __init__(self):
        super().__init__(name = "Hyper Potion",
                     description = "Heals a Pokemon by 200 HP",
                     value = 200)

#############
# PokeBalls #
#############
class PokeBall(Item):
    def __init__(self, name, description, catchRate, buy_price, sell_price):
        self.catchRateMultiplier = catchRate
        self.buy_price = buy_price
        self.sell_price = sell_price
        super().__init__(name, description)

class RegularBall(PokeBall):
    def __init__(self):
        super().__init__(name = "PokeBall",
                     description = "A BALL thrown at wild Pokemon to catch them.",
                     catchRate = 1,
                     buy_price = 200,
                     sell_price = 100)

class GreatBall(PokeBall):
    def __init__(self):
        super().__init__(name = "Great Ball",
                     description = "A BALL thrown at wild Pokemon to catch them. More effective than a PokeBall.",
                     catchRate = 1.5,
                     buy_price = 600,
                     sell_price = 300)

class UltraBall(PokeBall):
    def __init__(self):
        super().__init__(name = "Ultra Ball",
                     description = "A BALL thrown at wild Pokemon to catch them. More effective than a Great Ball.",
                     catchRate = 2,
                     buy_price = 1200,
                     sell_price = 600)

class MasterBall(PokeBall):
    def __init__(self):
        super().__init__(name = "Master Ball",
                     description = "A BALL that captures any wild Pokemon without fail.",
                     catchRate = 255,
                     buy_price = None,
                     sell_price = None)




        
        
