# imported shit

import random

# default variables

turn = 0
player_axis_y = -3
player_axis_x = -3
player_axis_z = -3
player_direction = "↑N"
enemy_axis_y = 3
enemy_axis_x = 3
enemy_axis_z = 3
enemy_direction = "↓S"

# player input

def player_commands():
    global player_axis_y
    global player_axis_x
    global player_axis_z
    global player_direction
    global turn
    turn = turn + 1
    while True:
        print("Turn #" + str(turn))
        print("Location= X: " + str(player_axis_x) + " Y: " + str(player_axis_y) + " Z: " + str(player_axis_z) + " D: " + str(player_direction))
        print()
        player_choice = input("(F)oward. (L)elt. (R)ight. (D)escend. (A)scend. (S)can. (T)orpedo :")
        print()
    # turning left
        if player_choice == "l":
            print("Your vessel banks toward portside..")
            print()
        if player_choice == "l" and player_direction == "↑N":
            player_direction = "←W"
            break
        if player_choice == "l" and player_direction == "↓S":
            player_direction = "→E"
            break
        if player_choice == "l" and player_direction == "→E":
            player_direction = "↑N"
            break
        if player_choice == "l" and player_direction == "←W":
            player_direction = "↓S"
            break
    # turning right
        if player_choice == "r":
            print("Your vessel banks toward starboard..")
            print()
        if player_choice == "r" and player_direction == "↑N":
            player_direction = "→E"
            break
        if player_choice == "r" and player_direction == "↓S":
            player_direction = "←W"
            break
        if player_choice == "r" and player_direction == "→E":
            player_direction = "↓S"
            break
        if player_choice == "r" and player_direction == "←W":
            player_direction = "↑N"
            break
    # moving
        if player_choice == "f":
            print("Your vessel propels forth..")
            print()
        if player_choice == "f" and player_direction == "↑N":
            player_axis_y = player_axis_y + 1
            break
        if player_choice == "f" and player_direction == "↓S":
            player_axis_y = player_axis_y - 1
            break
        if player_choice == "f" and player_direction == "→E":
            player_axis_x = player_axis_x + 1
            break
        if player_choice == "f" and player_direction == "←W":
            player_axis_x = player_axis_x - 1
            break
        if player_choice == "a":
            print("Your vessel rises toward the surface..")
            print()
            player_axis_z = player_axis_z + 1
            break
        if player_choice == "d":
            print("Your vessel lowers into the depths..")
            print()
            player_axis_z = player_axis_z - 1
            break
    # scanning
        if player_choice == "s":
            print("Target coordinance aquired! X:" + str(enemy_axis_x) + " Y:" + str(enemy_axis_y) + " Z:" + str(enemy_axis_z))
            print()
            break
    # firing
        if player_choice == "t":
           print("Not yet implimented...")     
           print()
           break   
    # error
        else:
            print("Invalid input..")
            print()
            

        

# game loop    
 
def game_loop():
    print("╔═════════════════╗")
    print("║ Submarine Game. ║")
    print("╚═════════════════╝")
    print()
    while True:
        player_commands()
      
  
# intitate game

game_loop()