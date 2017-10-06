import random, math, time, pokemonMoves

class Pokemon():
    learn_set = {} # holds the learnset of pokemon (key = level, value = move)

    def __init__(self, name, level, hp, attack, defense, special, speed, expYield, catchRate):
        self.name = name
        self.level = level
        self.move_set = []
        self.catchRate = catchRate

        # Exp and EFY yields after battle
        self.expYield = expYield
    
        # Base stats
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.base_special = special
        self.base_speed = speed

        # Intrinsic values
        self.IV_hp = random.randint(1, 15)
        self.IV_attack = random.randint(1, 15)
        self.IV_defense = random.randint(1, 15)
        self.IV_speed = random.randint(1, 15)
        self.IV_special = random.randint(1, 15)

        # Effort values
        self.EV_hp = 0
        self.EV_attack = 0
        self.EV_defense = 0
        self.EV_speed = 0
        self.EV_special = 0

        # Final stats
        self.hp = round(((((self.base_hp + self.IV_hp) * 2 + (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
        self.attack = round(((((self.base_attack + self.IV_attack) * 2 + (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
        self.defense = round(((((self.base_defense + self.IV_defense) * 2 + (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
        self.special = round(((((self.base_special + self.IV_special) * 2 + (math.sqrt(self.EV_special) / 4)) * self.level) / 100) + 5)
        self.speed = round(((((self.base_speed + self.IV_speed) * 2 + (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)

    def __str__(self):
        return self.name

    #
    # Fighting Methods
    #
    
    
    def opponentMove(self, yourPokemon):
        move = random.choice(self.move_set)
        damage = move.damagePoints(self, yourPokemon)
        yourPokemon.currentHP -= damage
        print()
        print("Enemy", self.name, "used", move.name)
        time.sleep(1)
        print("It did", damage, "damage")
        time.sleep(1)
        print(yourPokemon.name, "is now down to", yourPokemon.currentHP, "health")
        print()
        time.sleep(1)

    def checkForDefeat(self):
        return self.currentHP <= 0

    #
    # Level-up & Gain Methods
    #

    def gainExp(self, opponent):
        a = 1 # a is 1 if opponent is wild or 1.5 if owned by trainer
        b = opponent.expYield # b is base exp yield of opponent
        l = opponent.level # level of the enemy pokemon
        s = 1 # equal to number of Pokemon that have participated in battle and not fainted (do later)

        expGained = round((a * b * l) / (7 * s))
        self.exp += expGained
        print(self, "gained", expGained, "EXP points!")
        print()

    def gainEVs(self, opponent):
        self.EV_hp += opponent.EFY_hp
        self.EV_attack += opponent.EFY_attack
        self.EV_defense += opponent.EFY_defense
        self.EV_special += opponent.EFY_special
        self.EV_speed += opponent.EFY_speed


    def canLevelUp(self):
        raise NotImplementedError() 

    def levelUp(self):
        while self.canLevelUp():
            self.level += 1
            self.hp = round(((((self.base_hp + self.IV_hp) * 2 + (math.sqrt(self.EV_hp) / 4)) * self.level) / 100) + self.level + 10)
            self.attack = round(((((self.base_attack + self.IV_attack) * 2 + (math.sqrt(self.EV_attack) / 4)) * self.level) / 100) + 5)
            self.defense = round(((((self.base_defense + self.IV_defense) * 2 + (math.sqrt(self.EV_defense) / 4)) * self.level) / 100) + 5)
            self.special = round(((((self.base_special + self.IV_special) * 2 + (math.sqrt(self.EV_special) / 4)) * self.level) / 100) + 5)
            self.speed = round(((((self.base_speed + self.IV_speed) * 2 + (math.sqrt(self.EV_speed) / 4)) * self.level) / 100) + 5)
            print(self, "leveled up to level", self.level)
            print("\tHP:", self.hp)
            print("\tAttack:", self.attack)
            print("\tDefense:", self.defense)
            print("\tSpecial:", self.special)
            print("\tSpeed:", self.speed)
            print()

    def learnMove(self, move):
        self.move_set.append(move)
        return self.move_set

    def evolve(self):
        pass



#--------------------------------------------------------------------------------
    
##########
# Growth #
##########
class Fast(Pokemon):
    def __init__(self, name, level, hp, attack, defense, special, speed, expYield, catchRate):
        super().__init__(name, level, hp, attack, defense, special, speed, expYield, catchRate)
        if level == 1:
            self.exp = 0
        else:
            self.exp = int((4 * math.pow(level, 3)) / 5)

    def canLevelUp(self):
        # Returns a boolean of whether or not a Pokemon can level up
        return self.exp >= int((4 * math.pow(self.level + 1, 3)) / 5)
            

class MediumFast(Pokemon):
    def __init__(self, name, level, hp, attack, defense, special, speed, expYield, catchRate):
        super().__init__(name, level, hp, attack, defense, special, speed, expYield, catchRate)
        if level == 1:
            self.exp = 0
        else:
            self.exp = int(math.pow(level, 3))

    def canLevelUp(self):
        # Returns a boolean of whether or not a Pokemon can level up
        return self.exp >= int(math.pow(self.level + 1, 3))

class MediumSlow(Pokemon):
    def __init__(self, name, level, hp, attack, defense, special, speed, expYield, catchRate):
        super().__init__(name, level, hp, attack, defense, special, speed, expYield, catchRate)
        if level == 1:
            self.exp = 0
        else:
            self.exp = int(((6/5) * math.pow(level, 3)) - (15 * math.pow(level, 2)) + (100 * level) - 140)

    def canLevelUp(self):
        # Returns a boolean of whether or not a Pokemon can level up
        return self.exp >= int(((6/5) * math.pow(self.level + 1, 3)) - (15 * math.pow(self.level + 1, 2)) + (100 * (self.level + 1)) - 140)

class Slow(Pokemon):
    def __init__(self, name, level, hp, attack, defense, special, speed, expYield, catchRate):
        super().__init__(name, level, hp, attack, defense, special, speed, expYield, catchRate)
        if level == 1:
            self.exp = 0
        else:
            self.exp = int((5 * math.pow(level, 3)) / 4)

    def canLevelUp(self):
        # Returns a boolean of whether or not a Pokemon can level up
        return self.exp >= int((5 * math.pow(self.level + 1, 3)) / 4)



#--------------------------------------------------------------------------------



###########
# Pokemon #
###########

# 1
class Bulbasaur(MediumSlow):
    learn_set = {}
    learn_set[1] = pokemonMoves.Tackle()
    #learn_set[2] = pokemonMoves.Growl()
    #self.learn_set[7] = LeechSeed()
    #self.learn_set[13] = VineWhip()
    #self.learn_set[20] = PoisonPowder()
    #self.learn_set[27] = RazorLeaf()
    #self.learn_set[34] = Growth()
    #self.learn_set[41] = SleepPowder()
    #self.learn_set[48] = SolarBeam()

    # Effort value yields
    EFY_hp = 0
    EFY_attack = 0
    EFY_defense = 0
    EFY_special = 1
    EFY_speed = 0
        
    
    def __init__(self, level):
        self.type1 = "Grass"
        super().__init__(name = "BULBASAUR", level = level, hp = 45, attack = 49,
                         defense = 49, special = 65, speed = 45, expYield = 64,
                         catchRate = 45)
        for key in self.learn_set:
            if level >= key:
                self.learnMove(self.learn_set.get(key))
        

# 4
class Charmander(MediumSlow):
    learn_set = {}
    learn_set[1] = pokemonMoves.Scratch()
    #learn_set[2] = pokemonMoves.Growl()
    #self.learn_set[9] = Ember()
    #self.learn_set[15] = Leer()
    #self.learn_set[22] = Rage()
    #self.learn_set[30] = Slash()
    #self.learn_set[38] = Flamethrower()
    #self.learn_set[46] = FireSpin()

    # Effort value yields
    EFY_hp = 0
    EFY_attack = 0
    EFY_defense = 0
    EFY_special = 0
    EFY_speed = 1

    
    def __init__(self, level):
        self.type1 = "Fire"
        super().__init__(name = "CHARMANDER", level = level, hp = 39, attack = 52,
                         defense = 43, special = 50, speed = 65, expYield = 65,
                         catchRate = 45)
        for key in self.learn_set:
            if level >= key:
                self.learnMove(self.learn_set.get(key))
        
# 7
class Squirtle(MediumSlow):
    learn_set = {}
    learn_set[1] = pokemonMoves.Tackle()
    #learn_set[2] = pokemonMoves.TailWhip()
    #self.learn_set[8] = Bubble()
    #self.learn_set[15] = WaterGun()
    #self.learn_set[22] = Bite()
    #self.learn_set[28] = Withdraw()
    #self.learn_set[35] = SkullBash()
    #self.learn_set[42] = HydroPump()

    # Effort value yields
    EFY_hp = 0
    EFY_attack = 0
    EFY_defense = 1
    EFY_special = 0
    EFY_speed = 0

    
    def __init__(self, level):
        self.type1 = "Water"
        super().__init__(name = "SQUIRTLE", level = level, hp = 44, attack = 48,
                         defense = 65, special = 50, speed = 43, expYield = 66,
                         catchRate = 45)
        for key in self.learn_set:
            if level >= key:
                self.learnMove(self.learn_set.get(key))
        
# 16
class Pidgey(MediumSlow):
    learn_set = {}
    learn_set[1] = pokemonMoves.Gust()
    #self.learn_set[5] = SandAttack()
    #self.learn_set[12] = QuickAttack()
    #self.learn_set[19] = Whirlwind()
    #self.learn_set[28] = WingAttack()
    #self.learn_set[36] = Agility()
    #self.learn_set[44] = MirrorMove()

    # Effort value yields
    EFY_hp = 0
    EFY_attack = 0
    EFY_defense = 0
    EFY_special = 0
    EFY_speed = 1

    
    def __init__(self, level):
        self.type1 = "Flying"
        super().__init__(name = "PIDGEY", level = level, hp = 40, attack = 45,
                         defense = 40, special = 35, speed = 56, expYield = 55,
                         catchRate = 255)
        for key in self.learn_set:
            if level >= key:
                self.learnMove(self.learn_set.get(key))
        
# 19
class Rattata(MediumFast):
    learn_set = {}
    learn_set[1] = pokemonMoves.Tackle()
    #learn_set[2] = pokemonMoves.TailWhip()
    #self.learn_set[7] = QuickAttack()
    #self.learn_set[14] = HyperFang()
    #self.learn_set[23] = FocusEnergy()
    #self.learn_set[34] = SuperFang()

    # Effort value yields
    EFY_hp = 0
    EFY_attack = 0
    EFY_defense = 0
    EFY_special = 0
    EFY_speed = 1
    
    def __init__(self, level):
        self.type1 = "Normal"
        super().__init__(name = "RATTATA", level = level, hp = 30, attack = 56,
                         defense = 35, special = 25, speed = 72, expYield = 57,
                         catchRate = 45)
        for key in self.learn_set:
            if level >= key:
                self.learnMove(self.learn_set.get(key))
        




    

    

 
