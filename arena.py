from character import Character
from app import roster

class Team:
    def __init__(self, name):
        self.name = name
        self.roster = roster
    def add_character(self, character):
        self.roster.append(character)
    def remove_character(self, name):
        try:
            self.roster.pop(name)
        except:
            return 0
    def view_all_characters(self):
        index = 0
        for list_item in checklist:
            print(str(index) + " " + list_item)
            index += 1
    def attack(self, other_team):
        if len(other_team.roster) > 0:
            for opponent in other_team.roster:
                current_opponent = other_team.roster[random.randint(0, len(other_team.roster)-1)]
        else:
            print("You Win!")
            pass
        if len(self.roster) > 0:
            for character in self.roster:
                current_character = self.roster[random.randint(0, len(self.roster)-1)]
                current_character.fight(current_opponent)
        else:
            print("You Lose!")
            pass
    def revive_characters(self, health=100):
        for character in self.roster:
            self.current_health = health

class Arena:
    def __init__(self):
        self.team_one = Team("team one")
        self.team_two = Team("team two")
    def create_ability(self):
        ability_name = input("What will you name your ability: ")
        ability_strength = input("What is the power level: ")
        return Ability(ability_name, ability_strength)
    def create_armor(self):
        armor_name = input("What will you name your armor: ")
        armor_strength = input("What is the defense: ")
        return Armor(armor_name, armor_strength)

    #def create_character(self):
    #    character_name = input("What will you name your character: ")
    #    character = Character(character_name)
    #    is_ability = input("Do they have an ability? (y/n) ")
    #    while is_ability != "n":
    #        if is_ability == "y":
    #            hero.add_ability(self.create_ability())
    #        else:
    #            print("please type y/n")
    #        is_ability = input("Do they have another ability? (y/n) ")
        # is_weapon = input("Do they have a weapon? (y/n) ")
        # while is_weapon != "n":
        #     if is_weapon == "y":
        #         hero.add_weapon(self.create_weapon())
        #     else:
        #         print("please type y/n")
        #     is_weapon = input("Do they have another weapon? (y/n) ")
        # is_armor = input("Do they have an armor? (y/n) ")
        # while is_armor != "n":
        #     if is_armor == "y":
        #         hero.add_armor(self.create_armor())
        #     else:
        #         print("please type y/n")
        #     is_armor = input("Do they have another armor? (y/n) ")
        # return hero 
    def build_team_one(self):
        size = False
        while size == False:
            team_one_size = input("How many characters on team one?")
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