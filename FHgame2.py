# imported shit

import random

# default variables

player_axis_y = 1
player_axis_x = 3

x1y5z1 = " "
x1y4z1 = " "
x1y3z1 = " "
x1y2z1 = " "
x1y1z1 = " "
x2y5z1 = " "
x2y4z1 = " "
x2y3z1 = " "
x2y2z1 = " "
x2y1z1 = " "
x3y5z1 = " "
x3y4z1 = " "
x3y3z1 = " "
x3y2z1 = " "
x3y1z1 = " "
x4y5z1 = " "
x4y4z1 = " "
x4y3z1 = " "
x4y2z1 = " "
x4y1z1 = " "
x5y5z1 = " "
x5y4z1 = " "
x5y3z1 = " "
x5y2z1 = " "
x5y1z1 = " "

# map display

def map_display():
    print("[" + x1y5z1 + "][" + x2y5z1 + "][" + x3y5z1 + "][" + x4y5z1 + "][" + x5y5z1 + "]")
    print("[" + x1y4z1 + "][" + x2y4z1 + "][" + x3y4z1 + "][" + x4y4z1 + "][" + x5y4z1 + "]")
    print("[" + x1y3z1 + "][" + x2y3z1 + "][" + x3y3z1 + "][" + x4y3z1 + "][" + x5y3z1 + "]")
    print("[" + x1y2z1 + "][" + x2y2z1 + "][" + x3y2z1 + "][" + x4y2z1 + "][" + x5y2z1 + "]")
    print("[" + x1y1z1 + "][" + x2y1z1 + "][" + x3y1z1 + "][" + x4y1z1 + "][" + x5y1z1 + "]")
    print()

# player input

def player_coordinates():
    global player_axis_y
    global player_axis_x
    print("Location: X=[" + str(player_axis_x) + "] Y=[" + str(player_axis_y) + "]")
    print()
    while True:
        direction = input("(N)orth. (S)outh. (E)ast. (W)est. :")
        print()
        if direction == ("n"):
            player_axis_y = player_axis_y + 1
            break
        if direction == ("s"):
            player_axis_y = player_axis_y - 1
            break
        if direction == ("e"):
            player_axis_x = player_axis_x + 1
            break
        if direction == ("w"):
            player_axis_x = player_axis_x - 1
            break    
        print("Invalid input..")
        print()

# game loop    

def room_check():
    global player_axis_y
    global player_axis_x
    if player_axis_x == 1 and player_axis_y == 5:
        x1y5z1 = "X"
   

def game_loop():
    while True:
        room_check()
        map_display()
        player_coordinates()
        
    
# intitate game

game_loop()