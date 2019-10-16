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
class Weapon(Ability):
    def attack(self):
        return random.randint((self.attack_strength//2), self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        self.name=name
        self.current_health=starting_health
        self.abilities=[]
        self.armors=[]
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    def add_armor(self, armor):
        self.armors.append(armor)
    def add_kill(self, num_kills):
        self.kills += num_kills
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
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

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        try:
            self.heroes.pop(name)
        except:
            return 0
    def view_all_heroes(self):
        index = 0
        for list_item in checklist:
            print(str(index) + " " + list_item)
            index += 1
    def attack(self, other_team):
        if len(other_team.heroes) > 0:
            for opponent in other_team.heroes:
                current_villian = other_team.heroes[random.randint(0, len(other_team.heroes)-1)]
        else:
            print("heroes win!")
            pass
        if len(self.heroes) > 0:
            for hero in self.heroes:
                current_hero = self.heroes[random.randint(0, len(self.heroes)-1)]
                current_hero.fight(current_villian)
        else:
            print("Villians win!")
            pass
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            self.current_health = health
    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} has {hero.kills} kills and has died {hero.deaths} times.")

class Arena:
    def __init__(self):
        self.team_one = Team("team one")
        self.team_two = Team("team two")
    def create_ability(self):
        ability_name = input("What will you name your ability: ")
        ability_strength = input("What is the power level: ")
        return Ability(ability_name, ability_strength)
    def create_weapon(self):
        weapon_name = input("What will you name your weapon: ")
        weapon_strength = input("What is the strength: ")
        return Weapon(weapon_name, weapon_strength)
    def create_armor(self):
        armor_name = input("What will you name your armor: ")
        armor_strength = input("What is the defense: ")
        return Armor(armor_name, armor_strength)

    def create_hero(self):
        hero_name = input("What will you name your character: ")
        hero = Hero(hero_name)
        is_ability = input("Do they have an ability? (y/n) ")
        while is_ability != "n":
            if is_ability == "y":
                hero.add_ability(self.create_ability())
            else:
                print("please type y/n")
            is_ability = input("Do they have another ability? (y/n) ")
        is_weapon = input("Do they have a weapon? (y/n) ")
        while is_weapon != "n":
            if is_weapon == "y":
                hero.add_weapon(self.create_weapon())
            else:
                print("please type y/n")
            is_weapon = input("Do they have another weapon? (y/n) ")
        is_armor = input("Do they have an armor? (y/n) ")
        while is_armor != "n":
            if is_armor == "y":
                hero.add_armor(self.create_armor())
            else:
                print("please type y/n")
            is_armor = input("Do they have another armor? (y/n) ")
        return hero 
    def build_team_one(self):
        size = False
        while size == False:
            team_one_size = input("How many heroes on team one?")
            try:
                team_one_size = int(team_one_size)
                size = True
            except ValueError:
               print("That's not a usable number.")
        for amount in range(0,team_one_size):
            self.team_one.add_hero(self.create_hero())
    def build_team_two(self):
        size = False
        while size == False:
            team_two_size = input("How many villians on team two?")
            try:
                team_two_size = int(team_two_size)
                size = True
            except ValueError:
               print("That's not a usable number.")
        for amount in range(0,team_two_size):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):

        self.team_one.stats()
        self.team_two.stats()
        for hero in self.team_one.heroes:
            if hero.is_alive:
                print(f"{hero.name} is still alive.")
        for hero in self.team_two.heroes:
            if hero.is_alive:
                print(f"{hero.name} is still alive.")

        

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        play_answer = False

        while play_answer == False:
            #Check for Player Input
            if play_again.lower() == "n":
                game_is_running = False
                play_answer = True

            elif play_again.lower() == "y":
                #Revive heroes to play again
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
                play_answer = True
            
            else:
                print("Please type y/n:")