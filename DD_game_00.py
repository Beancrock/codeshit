# imported

import random
import os

# map array

def map_display_refresh():

    global dungeon_map_01

    dungeon_map_01 = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "╥", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "╔", "═", "╩", "═", "╗", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "╔", "╩", "═", "╦", "═", "╩", "╗", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "║", " ", "╔", "╩", "╗", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "╔", "═", "╬", "═", "╣", " ", "╠", "═", "╬", "═", "╗", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", "╔", "╣", " ", "║", "╔", "╩", "╦", "╩", "╗", "║", " ", "╠", "╗", " ", " ", " ", " ", " ", " "],
            [" ", " ", "║", "║", "╔", "╩", "╣", " ", "║", " ", "╠", "╩", "╗", "║", "║", " ", " ", " ", " ", " ", " "],
            ["╞", "═", "╣", "╠", "╣", " ", "╠", "═", "⌂", "═", "╣", " ", "╠", "╣", "╠", "═", "╡", " ", " ", " ", " "],
            [" ", " ", "║", "║", "╚", "╦", "╣", " ", "║", " ", "╠", "╦", "╝", "║", "║", " ", " ", " ", " ", " ", " "],
            [" ", " ", "╚", "╣", " ", "║", "╚", "╦", "╩", "╦", "╝", "║", " ", "╠", "╝", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "╚", "═", "╬", "═", "╣", " ", "╠", "═", "╬", "═", "╝", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "║", " ", "╚", "╦", "╝", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "╚", "╦", "═", "╩", "═", "╦", "╝", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "╚", "═", "╦", "═", "╝", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "╨", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  
    ]    


# class

class Character:
    
# initualization

    def __init__(self, direction, location, choice, spawn, x, y):
        self.direction = direction
        self.location = location
        self.choice = choice
        self.spawn = spawn
        self.x = x
        self.y = y

    def map_display(self):
    
# map diplay

        os.system('cls')
        print()
        print("¦" + dungeon_map_01[self.y-2][self.x-2] + "¦" + dungeon_map_01[self.y-2][self.x-1] + "¦" + dungeon_map_01[self.y-2][self.x] + "¦" + dungeon_map_01[self.y-2][self.x+1] + "¦" + dungeon_map_01[self.y-2][self.x+2] + "¦")
        print("¦" + dungeon_map_01[self.y-1][self.x-2] + "¦" + dungeon_map_01[self.y-1][self.x-1] + "¦" + dungeon_map_01[self.y-1][self.x] + "¦" + dungeon_map_01[self.y-1][self.x+1] + "¦" +  dungeon_map_01[self.y-1][self.x+2] + "¦")
        print("¦" + dungeon_map_01[self.y][self.x-2] + "¦" + dungeon_map_01[self.y][self.x-1] + "¦+¦" + dungeon_map_01[self.y][self.x+1] + "¦" + dungeon_map_01[self.y][self.x+2] + "¦")
        print("¦" + dungeon_map_01[self.y+1][self.x-2] + "¦" + dungeon_map_01[self.y+1][self.x-1] + "¦" + dungeon_map_01[self.y+1][self.x] + "¦" + dungeon_map_01[self.y+1][self.x+1] + "¦" +  dungeon_map_01[self.y+1][self.x+2] + "¦")
        print("¦" + dungeon_map_01[self.y+2][self.x-2] + "¦" + dungeon_map_01[self.y+2][self.x-1] + "¦" + dungeon_map_01[self.y+2][self.x] + "¦" + dungeon_map_01[self.y+2][self.x+1] + "¦" +  dungeon_map_01[self.y+2][self.x+2] + "¦")
        print()
        #print(f"Player: {player.direction}, {player.location}, {player.choice}, {player.spawn}, {player.x}, {player.y}")
        #print(f"Enemy: {enemy.direction}, {enemy.location}, {enemy.choice}, {enemy.spawn}, {enemy.x}, {enemy.y}")
        #print()

# enemy appearance on map

    def map_blip(self):

        dungeon_map_01[self.y][self.x] = "◌"
           

# movement

    def movement(self):

        self.location = dungeon_map_01[self.y][self.x]
        
        if self.location == "╬" or self.location == "⌂":
            self.direction = ["n","s","e","w"]
        elif self.location == "╩":
            self.direction = ["n","e","w"]
        elif self.location == "╦":
            self.direction = ["s","e","w"]
        elif self.location == "╣":
            self.direction = ["n","s","w"]            
        elif self.location == "╠":
            self.direction = ["n","s","e"]
        elif self.location == "╝":
            self.direction = ["n","w"]
        elif self.location == "╚":
            self.direction = ["n","e"]        
        elif self.location == "╗":
            self.direction = ["s","w"]
        elif self.location == "╔":
            self.direction = ["s","e"]
        elif self.location == "║":
            self.direction = ["n","s"]
        elif self.location == "═":
            self.direction = ["e","w"]
        elif self.location == "╨":
            self.direction = ["n"]            
        elif self.location == "╥":
            self.direction = ["s"]
        elif self.location == "╡":
            self.direction = ["w"]
        elif self.location == "╞":
            self.direction = ["e"]        
        else:
            print()
            input("Error!")
            print()

# choices

    def selection(self):

        while True:    
            self.choice = input("(N)orth (S)outh (E)ast (W)est (H)ide :").lower()
            print()
    
            if self.choice in self.direction:
                if self.choice == "n":
                    self.y -= 1
                    player.map_display()
                    print("You travel north.")
                    print()
                    break
                elif self.choice == "s":
                    self.y += 1
                    player.map_display()
                    print("You travel south.")
                    print()
                    break
                elif self.choice == "e":
                    self.x += 1
                    player.map_display()
                    print("You travel east.")
                    print()
                    break
                elif self.choice == "w":
                    self.x -= 1
                    player.map_display()
                    print("You travel west.")
                    print()
                    break

    
            elif self.choice == "h":
                player.map_display()
                print("You hide and wait.")
                print()
                break
      
            else:
                player.map_display()
                print("Invalid input. Please enter a valid direction.")
                print()


# randomized movement

    def rng_selection(self):

        self.choice = random.choice(self.direction)

        if self.choice == "n":
            self.y -= 1
        elif self.choice == "s":
            self.y += 1
        elif self.choice == "e":
            self.x += 1
        elif self.choice == "w":
                self.x -= 1

            
                            

# encounter check

    def encounter_check(self):
        
        if self.y == player.y and self.x == player.x:
            player.map_display() 
            print("You done got gobbled up.")
            print()
            print("Game over.")
            input()
            exit()        

# Introduction and instruction                               
  
def intro():
    
    print()
    print('''
    Hi. Thanks for trying my untitled game. It's a text/ascii turn based game.
    This project's purpose is for learning and practicing the python programming
    language. I've no doubt that my coding is a rough mess, but I hope to improve.
    I'm certainly open to corrections and suggestions.
    
                                           - Daring Dragoon a.k.a. Father Heathen      
    ''')
    
    input("Press enter.")
    os.system('cls')      
    
    print('''
    Story: You're a member of a space colony that's located on one of three moons orbiting
          a lonely gas giant in an obscure and remote system that, aside from an asteroid belt,
          is otherwise empty. The planet, its moons, and its star are all known only by a series
          of numerals and hyphens. Unless you count the automated mining operation in the belt,
          your colony is the soul sign of humanity within the system, but not the only sign of
          life. Your colony is a scientific expedition tasked with the study of the flora and
          fauna discovered upon the moon. You're not a member of the science team yourself, but
          one of the grunts tasked with maintenance and upkeep. Then one day, an "incident"
          occurs. Emergency lights flash. Alarms blare. A crowd gathers. You overhear whispers
          of "something" escaping from one of the laboratories and is now loose somewhere on the 
          station. You're grabbed by your superior and ordered to descend into the maintenance
          tunnels and instructed to turn 4 valves in order to bring some back-up system online. 
          You're handed a device that scans and gives a read-out of your general proximity. It 
          can also detect nearby activity. As you descend into the tunnels you immediately notice
          that it's pitch black. You turn on your device's built-in flash light, but all you can
          see is a thick fog of steam and moisture, rendering your light source useless. The hatch
          closes and locks behind you. Your radio crackles, "We'll let you out as soon as the
          task is complete." You firmly grip your device and steel your nerves, and venture forth.
          ''')
    
    input("Press enter.")
    os.system('cls')

    print('''
    Intructions: Navigate the maze of tunnels by typing and entering the letter that corresponds
          with the direction you wish to move, or the action you wish to take. Try to avoid
          contact with the creature. When it gets close, it begins to pursue the player. Hiding
          will stop it from pursuing (but it may still discover you while wondering about.) Locate
          and 'turn' 4 valves located at dead-ends. This is done automatically by moving onto the
          designated spaces. Once completed, exit the maze by returning to the starting point.
          Good luck!      
          ''')
    
    input("Press enter.")
    os.system('cls')

# characters

player = Character(" ", " ", " ", 1, 8, 11)
enemy1 = Character(" ", " ", " ", 1, 8, 3)
enemy2 = Character(" ", " ", " ", 1, 16, 11)
enemy3 = Character(" ", " ", " ", 1, 8, 19)
enemy4 = Character(" ", " ", " ", 1, 0, 11)

def game_loop():
    enemy1.map_blip()
    enemy2.map_blip()
    enemy3.map_blip()
    enemy4.map_blip()
    enemy1.encounter_check()
    enemy2.encounter_check()
    enemy3.encounter_check()
    player.movement()
    player.selection()
    enemy1.encounter_check()
    enemy2.encounter_check()
    enemy3.encounter_check()
    map_display_refresh()
    enemy1.movement()
    enemy1.rng_selection()
    enemy2.movement()
    enemy2.rng_selection()
    enemy3.movement()
    enemy3.rng_selection()
    enemy4.movement()
    enemy4.rng_selection()
    game_loop() 


intro()
map_display_refresh()
player.map_display()
game_loop()



