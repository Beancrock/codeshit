import random  # Import the random module for generating random numbers (used for damage calculation)

# Define a Character class to represent both the player and the monster
class Character:
    def __init__(self, name, health, attack):
        # Initialize character attributes
        self.name = name        # Name of the character
        self.health = health    # Character's health points (HP)
        self.attack = attack    # Character's attack power (maximum damage they can deal)

    def is_alive(self):
        # Check if the character's health is above 0
        return self.health > 0

    def take_damage(self, damage):
        # Reduce the character's health by the amount of damage taken
        self.health -= damage
        # Ensure health does not go below 0
        if self.health < 0:
            self.health = 0

    def attack_target(self, target):
        # Calculate a random damage amount between 0 and the character's maximum attack power
        damage = random.randint(0, self.attack)
        # Print the attack action and damage dealt
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        # Apply the damage to the target
        target.take_damage(damage)
        # Print the target's remaining health
        print(f"{target.name}'s health is now {target.health}\n")

# Define the Game class, which manages the game logic
class Game:
    def __init__(self):
        # Create the player character and an enemy monster character
        self.player = Character("Hero", health=30, attack=10)  # Player starts with 30 health, 10 attack
        self.monster = Character("Goblin", health=20, attack=6) # Monster has 20 health, 6 attack

    def play(self):
        # Print the opening message
        print("An RPG Battle Begins!")
        print(f"You encounter a {self.monster.name}!\n")

        # Main game loop: continues as long as both characters are alive
        while self.player.is_alive() and self.monster.is_alive():
            # Ask the player for their action each turn
            action = input("Choose an action (attack or run): ").strip().lower()
            
            # If the player chooses to attack
            if action == "attack":
                self.player.attack_target(self.monster)  # Player attacks the monster
                if not self.monster.is_alive():         # Check if the monster is defeated
                    print("You defeated the monster!")  # If monster's health is 0, the player wins
                    break
            elif action == "run":  # If the player chooses to run
                print("You ran away safely.")
                break              # End the game if the player runs
            else:
                # Invalid action (if the player inputs anything other than 'attack' or 'run')
                print("Invalid action. Please choose 'attack' or 'run'.\n")
                continue           # Skip to the next iteration of the loop

            # Monster's turn to attack, if it is still alive
            if self.monster.is_alive():
                self.monster.attack_target(self.player)  # Monster attacks the player
                if not self.player.is_alive():          # Check if the player is defeated
                    print("You were defeated by the monster. Game over!")  # Game over if player loses
                    break

# Start the game by creating a Game instance and calling its play method
if __name__ == "__main__":
    game = Game()
    game.play()

