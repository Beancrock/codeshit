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


# player input

def player_commands():
    global player_axis_y
    global player_axis_x
    global player_axis_z
    global player_direction
    global player_choice
    global turn
    turn = turn + 1
    while True:
        print("Turn #" + str(turn))
        print("Location= X: " + str(player_axis_x) + " Y: " + str(player_axis_y) + " Z: " + str(player_axis_z) + " D: " + str(player_direction))
        print()
        player_choice = input("(F)oward (L)elt (R)ight (D)escend (A)scend (S)can (T)orpedo (Q)uit :")
        print()
    # exit
        if player_choice == "q":
            print("Thanks for playing!")
            exit()
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
            
def enemy_movement():
    global player_axis_y
    global player_axis_x
    global player_axis_z
    global player_direction
    global player_choice
    global enemy_axis_y
    global enemy_axis_x
    global enemy_axis_z
    while True:
        if player_axis_x > enemy_axis_x:
            enemy_axis_x = enemy_axis_x + 1
            break
        if player_axis_x < enemy_axis_x:
            enemy_axis_x = enemy_axis_x - 1
            break
        if player_axis_y > enemy_axis_y:
            enemy_axis_y = enemy_axis_y + 1
            break
        if player_axis_y < enemy_axis_y:
            enemy_axis_y = enemy_axis_y - 1
            break
        if player_axis_z > enemy_axis_z:
            enemy_axis_z = enemy_axis_z + 1
            break
        if player_axis_z < enemy_axis_z:
            enemy_axis_z = enemy_axis_z - 1
            break
        else:
            print("Your vessel shakes violenty. Alarm systems blare. Wires and panels hiss and crackle")
            print("with sparks. Pipes and hoses hiss and rupture. The hull echos with the horrible")
            print("sound of contorting and buckling metal. Frigid water spills into the interior,")
            print("flooding it. The lights flicker and go dark. Game over...")
            print()
            while True:
                player_choice = input("Do you wish to try again? Y/N")
                print()
                if player_choice == "y":
                    game_loop() 
                if player_choice == "n":
                    exit()
                else:
                    print("Invalid input..")
                    print()








    
        

# game loop    
 
def game_loop():
    global turn
    turn = 0
    print("╔═════════════════╗")
    print("║ Submarine Game. ║")
    print("╚═════════════════╝")
    print()
    while True:
        player_commands()
        enemy_movement()
  
# intitate game

game_loop()