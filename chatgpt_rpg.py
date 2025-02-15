import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

def battle(player, monster):
    print(f"The Battle between {player.name} and {monster.name} shall commence!\n")
    print(f"{player.name}'s HP: {player.hp} AP: {player.attack} | {monster.name}'s HP: {monster.hp} AP: {monster.attack}")
    
    while player.hp > 0 and monster.hp > 0:
        player_attack = random.randint(1, player.attack)
        monster_attack = random.randint(1, monster.attack)
#pause
        print()
        input()

        print(f"{player.name} attacks {monster.name} for {player_attack} damage!")
        monster.take_damage(player_attack)
        print(f"{monster.name} attacks {player.name} for {monster_attack} damage!")
        player.take_damage(monster_attack)
        
        print(f"{player.name}'s HP: {player.hp} | {monster.name}'s HP: {monster.hp}")
        if player.hp <= 0:
            print(f"{player.name} has been defeated. {monster.name} is Victorious!")
        elif monster.hp <= 0:
            print(f"{monster.name} has been defeated. {player.name} is victorious!")
    
    print("Vae victis....")

# Create player and monster instances
player = Character("Hero", 100, 100)
monster = Character("Villain", 100, 100)

# Start the battle
battle(player, monster)