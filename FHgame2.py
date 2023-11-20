#imported shit

import random

#default variables

player_axis_y = 1
player_axis_x = 3

x1y5 = " "
x1y4 = " "
x1y3 = " "
x1y2 = " "
x1y1 = " "
x2y5 = " "
x2y4 = " "
x2y3 = " "
x2y2 = " "
x2y1 = " "
x3y5 = " "
x3y4 = " "
x3y3 = " "
x3y2 = " "
x3y1 = " "
x4y5 = " "
x4y4 = " "
x4y3 = " "
x4y2 = " "
x4y1 = " "
x5y5 = " "
x5y4 = " "
x5y3 = " "
x5y2 = " "
x5y1 = " "

# map display

def map_display():
    print("[" + x1y5 + "][" + x2y5 + "][" + x3y5 + "][" + x4y5 + "][" + x5y5 + "]")
    print("[" + x1y4 + "][" + x2y4 + "][" + x3y4 + "][" + x4y4 + "][" + x5y4 + "]")
    print("[" + x1y3 + "][" + x2y3 + "][" + x3y3 + "][" + x4y3 + "][" + x5y3 + "]")
    print("[" + x1y2 + "][" + x2y2 + "][" + x3y2 + "][" + x4y2 + "][" + x5y2 + "]")
    print("[" + x1y1 + "][" + x2y1 + "][" + x3y1 + "][" + x4y1 + "][" + x5y1 + "]")
    print()

# player input

def player_movement():
    global player_axis_y
    global player_axis_x
    print("Location: X=[" + str(player_axis_x) + "] Y=[" + str(player_axis_y) + "]")
    print()
    while True:
        direction = input("(n)orth. (s)outh. (e)ast. (w)est. :")
        print()
        if direction == ("n"):
            player_axis_y = player_axis_y + 1
            break
        if direction == ("s"):
            player_axis_y = player_axis_y - 1
            break
        if direction == ("e"):
            player_axis_x = player_axis_x - 1
            break
        if direction == ("w"):
            player_axis_x = player_axis_x + 1
            break    
        print("Invalid input..")
        print()


# game loop    


def game_loop():
    while True:
        map_display()
        player_movement()
        

# intitate game

game_loop()