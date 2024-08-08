'''potential additions:
Shotgun: starts with limited (3?) shells. only works one 'space' away. Player chooses direction to fire (n,s,e,w).
Doesn't kill or damage enemy, but makes them retreat for X amount of turns. Can't shoot in direction where
movement would be restricted (i.e can't hit enemy through walls).
Flare: 'stuns' enemy at spot where dropped for x amount of turns, maybe?
Enemy spawn randomized, likely to share spots with 'valves'.
'Vent crawling' for enemy under certain conditions (enemy moves without direction restrictions)
May add random start/exit positions for replayability's sake.'''


# imported shit

import random

# 'map' layout subject to change.

dungeon_map_01 = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "╥", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "╔", "═", "╩", "═", "╗", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "╔", "╩", "═", "╦", "═", "╩", "╗", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "║", " ", " ", "║", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "╔", "═", "╬", "═", "╦", "╩", "╦", "═", "╬", "═", "╗", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "╔", "╣", " ", "║", "╔", "╩", "╦", "╩", "╗", "║", " ", "╠", "╗", " ", " ", " ", " ", " ", " "],
        [" ", " ", "║", "║", " ", "╠", "╣", " ", "║", " ", "╠", "╣", " ", "║", "║", " ", " ", " ", " ", " ", " "],
        ["╞", "═", "╣", "╠", "═", "╣", "╠", "═", "⌂", "═", "╣", "╠", "═", "╣", "╠", "═", "╡", " ", " ", " ", " "],
        [" ", " ", "║", "║", " ", "╠", "╣", " ", "║", " ", "╠", "╣", " ", "║", "║", " ", " ", " ", " ", " ", " "],
        [" ", " ", "╚", "╣", " ", "║", "╚", "╦", "╩", "╦", "╝", "║", " ", "╠", "╝", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "╚", "═", "╬", "═", "╩", "╦", "╩", "═", "╬", "═", "╝", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "║", " ", " ", "║", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "╚", "╦", "═", "╩", "═", "╦", "╝", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "╚", "═", "╦", "═", "╝", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", "╨", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  
    ] 

# ascii symbols for copying and pasting purposes: ╬ ╩ ╦ ╣ ╠ ╝ ╚ ╗ ╔ ║ ═ ╡ ╞ ╨ ╥ ⌂

# variables and values

global player_direction
global x
global y
global enemy_direction
global zx
global zy
global p_e_x_distance
global p_e_y_distance
global p_e_t_distance

global player_location
global valve_1
global valve_2
global valve_3
global valve_4
global valve_count
global vlx
global v1y
global v2x
global v2y
global v3x
global v3y
global v4x
global v4y
global ex
global ey

player_direction = ["n","s","e","w"]
x = 8
y = 11
zx = 8
zy = 3
v1x = 8
v1y = 3
v2x = 16
v2y = 11
v3x = 8
v3y = 19
v4x = 0
v4y = 11
ex = 8
ey = 11
p_e_x_distance = 100
p_e_y_distance = 100
p_e_t_distance = 100
valve_count = 4    
valve_1 = True
valve_2 = True
valve_3 = True
valve_4 = True

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
    print()

# game loop

def gameloop():
    map_display()
    encounter_check()
    valve_check()
    player_movement()
    encounter_check()
    enemy_movement()
    gameloop()

# player map and detector (player's means of perceiving game environment) 

def map_display():
    global p_e_x_distance
    global p_e_y_distance
    global p_e_t_distance
    global x
    global y
    global zx
    global zy

# map diplay

    print("¦" + dungeon_map_01[y-2][x-2] + "¦" + dungeon_map_01[y-2][x-1] + "¦" + dungeon_map_01[y-2][x] + "¦" + dungeon_map_01[y-2][x+1] + "¦" + dungeon_map_01[y-2][x+2] + "¦")
    print("¦" + dungeon_map_01[y-1][x-2] + "¦" + dungeon_map_01[y-1][x-1] + "¦" + dungeon_map_01[y-1][x] + "¦" + dungeon_map_01[y-1][x+1] + "¦" +  dungeon_map_01[y-1][x+2] + "¦")
    print("¦" + dungeon_map_01[y][x-2] + "¦" + dungeon_map_01[y][x-1] + "¦☻¦" + dungeon_map_01[y][x+1] + "¦" + dungeon_map_01[y][x+2] + "¦")
    print("¦" + dungeon_map_01[y+1][x-2] + "¦" + dungeon_map_01[y+1][x-1] + "¦" + dungeon_map_01[y+1][x] + "¦" + dungeon_map_01[y+1][x+1] + "¦" +  dungeon_map_01[y+1][x+2] + "¦")
    print("¦" + dungeon_map_01[y+2][x-2] + "¦" + dungeon_map_01[y+2][x-1] + "¦" + dungeon_map_01[y+2][x] + "¦" + dungeon_map_01[y+2][x+1] + "¦" +  dungeon_map_01[y+2][x+2] + "¦")
    print()
    
 # enemy detection

    if x >= zx:
        p_e_x_distance = x - zx
    elif x < zx:
        p_e_x_distance = zx - x
    elif y < zy:
        p_e_y_distance = zy - y
    elif y >= zy:
        p_e_y_distance = y - zy 
  
    p_e_t_distance = p_e_y_distance + p_e_x_distance
    if p_e_t_distance < 6:
        print("Warning! Activity detected within range [" + str(p_e_t_distance) + "]")
        print()

# handles how player navigates map

def player_movement():
    global player_direction
    global player_location
    global x
    global y
    global hide

# player direction restriction

    player_location = dungeon_map_01[y][x]
    hide = False # 'hide' reset

    if player_location == "╬":
        player_direction = ["n","s","e","w"]
    elif player_location == "╩":
        player_direction = ["n","x","e","w"]
    elif player_location == "╦":
        player_direction = ["x","s","e","w"]
    elif player_location == "╣":
        player_direction = ["n","s","x","w"]            
    elif player_location == "╠":
        player_direction = ["n","s","e","x"]
    elif player_location == "╝":
        player_direction = ["n","x","x","w"]
    elif player_location == "╚":
        player_direction = ["n","x","e","x"]        
    elif player_location == "╗":
        player_direction = ["x","s","x","w"]
    elif player_location == "╔":
        player_direction = ["x","s","e","x"]
    elif player_location == "║":
        player_direction = ["n","s","x","x"]
    elif player_location == "═":
        player_direction = ["x","x","e","w"]
    elif player_location == "╨":
        player_direction = ["n","x","x","x"]            
    elif player_location == "╥":
        player_direction = ["x","s","x","x"]
    elif player_location == "╡":
        player_direction = ["x","x","x","w"]
    elif player_location == "╞":
        player_direction = ["x","x","e","x"]        
    else:
        player_direction = ["n","s","e","w"]
        
# player movement choice

    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est (H)ide :").lower()
        
        print()
        if player_choice == "n" and player_direction[0] == "n":
            y = y - 1
            print("You travel north.")
            print()
            break
        if player_choice == "s" and player_direction[1] == "s":
            y = y + 1
            print("You travel south.")
            print()
            break
        if player_choice == "e" and player_direction[2] == "e":
            x = x + 1
            print("You travel east.")
            print()
            break 
        if player_choice == "w" and player_direction[3] == "w":
            x = x - 1
            print("You travel west.")
            print()
            break
        if player_choice == "h":
            hide = True
            print("You hide and wait.")
            print()
            break     
        else:
            print("Invalid input..")
            print()          

# handles how enemy navigates map

def enemy_movement():
    global enemy_direction
    global enemy_location
    global zx
    global zy
    global hide
    
# enemy direction restriction

    enemy_location = dungeon_map_01[zy][zx]
    
    if enemy_location == "╬":
        enemy_direction = ["n","s","e","w"]
    elif enemy_location == "╩":
        enemy_direction = ["n","e","w"]
    elif enemy_location == "╦":
        enemy_direction = ["s","e","w"]
    elif enemy_location == "╣":
        enemy_direction = ["n","s","w"]            
    elif enemy_location == "╠":
        enemy_direction = ["n","s","e"]
    elif enemy_location == "╝":
        enemy_direction = ["n","w"]
    elif enemy_location == "╚":
        enemy_direction = ["n","e"]        
    elif enemy_location == "╗":
        enemy_direction = ["s","w"]
    elif enemy_location == "╔": 
        enemy_direction = ["s","e"]
    elif enemy_location == "║":
        enemy_direction = ["n","s"]
    elif enemy_location == "═":
        enemy_direction = ["e","w"]
    elif enemy_location == "╨":
        enemy_direction = ["n"]            
    elif enemy_location == "╥":
        enemy_direction = ["s"]
    elif enemy_location == "╡":
        enemy_direction = ["w"]
    elif enemy_location == "╞":
        enemy_direction = ["e"]        
    else:
        enemy_direction = ["n","s","e","w"]

 # enemy movement RNG
 
    enemy_choice = random.choice(enemy_direction)

# enemy chases player when close

    while hide == False and p_e_t_distance < 4:

        if zy > y and "n" in enemy_direction:
            zy = zy - 1
            break
        if zy < y and "s" in enemy_direction:
            zy = zy + 1
            break
        if zx > x and "e" in enemy_direction:
            zx = zx - 1
            break
        if zx < x and "w" in enemy_direction:
            zx = zx + 1
            break 
        else:
            break

# enemy randomly roams when far (or player 'hides')

    while p_e_t_distance >= 4 or hide == True:    
        
        if enemy_choice == "n":
            zy = zy - 1
            break
        if enemy_choice == "s":
            zy = zy + 1
            break
        if enemy_choice == "e":
            zx = zx + 1
            break 
        if enemy_choice == "w":
            zx = zx - 1
            break
                  
# checks to see if 'player' and 'enemy' occupy same spot, thus resulting in a loss.                

def encounter_check():
    global x
    global y
    global zx
    global zy
    
    if y == zy and x == zx:
        print("First you hear ear piercing shrieks, then you feel skull piercing fangs,")
        print("and finally you both hear and feel skull crushing jaws,")
        print("albeit within one of the final beats of your heart.")
        print("Game over.")
        print()
        input()
        exit()

# valve and exit check

def valve_check():
    global player_location
    global valve_count
    global valve_1
    global valve_2
    global valve_3
    global valve_4
    global vlx
    global v1y
    global v2x
    global v2y
    global v3x
    global v3y
    global v4x
    global v4y
    global ex
    global ey

    if x == v1x and y == v1y and valve_1 == True:
        valve_1 = False
        valve_count = valve_count - 1
        if valve_count > 0:
            print("You quickly turn the valve. " + str(valve_count) + " more to go...")
            print()
        if valve_count == 0:
            print("You quickly turn the valve. That was the last one. Time to leave...")
            print()
    elif x == v2x and y == v2y and valve_2 == True:
        valve_2 = False
        valve_count = valve_count - 1
        if valve_count > 0:
            print("You quickly turn the valve. " + str(valve_count) + " more to go...")
            print()
        if valve_count == 0:
            print("You quickly turn the valve. That was the last one. Time to leave...")
            print()
    elif x == v3x and y == v3y and valve_3 == True:
        valve_3 = False
        valve_count = valve_count - 1
        if valve_count > 0:
            print("You quickly turn the valve. " + str(valve_count) + " more to go...")
            print()
        if valve_count == 0:
            print("You quickly turn the valve. That was the last one. Time to leave...")
            print()
    elif x == v4x and y == v4y and valve_4 == True:
        valve_4 = False
        valve_count = valve_count - 1
        if valve_count > 0:
            print("You quickly turn the valve. " + str(valve_count) + " more to go...")
            print()
        if valve_count == 0:
            print("You quickly turn the valve. That was the last one. Time to leave...")
            print()                            
    elif x == ex and y == ey and valve_count == 0:
        print("You've ecaped. Oddly, the hatch was not only left unlocked, but opened.")
        print("You ascend from the tunnels, only to be greeted with more darkness and silence.")
        print("Game over.")
        print()
        input()
        exit()

intro()
gameloop()

