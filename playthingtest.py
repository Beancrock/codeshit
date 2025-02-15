import random

def roll_dice():
    return random.randint(1,6)

print("Welcome to the dice roller!")
num_rolls = int(input("How many times would you like to roll the dice? "))
for _ in range(num_rolls):
    print(f"You rolled a {roll_dice()}")