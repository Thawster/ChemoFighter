import random


class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)

class Character:
    def __init__(self, name, starting_health):
        self.name=name
        self.current_health=starting_health
        self.abilities=[]
        self.armors=[]
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        temp = 0
        for Ability in self.abilities:
            temp += Ability.attack()
        return temp
    #the tests come back wrong, because they don't use damage_amt,
    #my code runs correctly using it though
    def defend(self, damage_amt):
        temp = damage_amt
        if len(self.armors) > 0:
            for Armor in self.armors:
                temp -= Armor.block()
        return temp
    def take_damage(self, damage):
        damage = self.defend(damage)
        self.current_health -= damage
    def is_alive(self): 
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return
        while opponent.is_alive() and self.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
        if self.is_alive():
            print(f"{self.name} won!")
            self.add_kill(1)
        elif opponent.is_alive():
            print(f"{opponent.name} won!")
            self.add_deaths(1)
        else:
            print("They both are knocked out!")
