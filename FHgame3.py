# default values

player_loc_x = 3
player_loc_y = 3

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
x3y3 = "X"
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

# grid display

def grid():
    global player_loc_x
    global player_loc_y
    
    global x1y5
    global x1y4
    global x1y3
    global x1y2
    global x1y1
    
    global x2y5
    global x2y4
    global x2y3
    global x2y2
    global x2y1
    
    global x3y5
    global x3y4
    global x3y3
    global x3y2
    global x3y1

    global x4y5
    global x4y4
    global x4y3
    global x4y2
    global x4y1
    
    global x5y5
    global x5y4
    global x5y3
    global x5y2
    global x5y1
    
    print("X: "+ str(player_loc_x) + " Y:" + str(player_loc_y))
    print()
    print("[" + x1y5 + "][" + x2y5 + "][" + x3y5 + "][" + x4y5 + "][" + x5y5 + "]")
    print("[" + x1y4 + "][" + x2y4 + "][" + x3y4 + "][" + x4y4 + "][" + x5y4 + "]")
    print("[" + x1y3 + "][" + x2y3 + "][" + x3y3 + "][" + x4y3 + "][" + x5y3 + "]")
    print("[" + x1y2 + "][" + x2y2 + "][" + x3y2 + "][" + x4y2 + "][" + x5y2 + "]")
    print("[" + x1y1 + "][" + x2y1 + "][" + x3y1 + "][" + x4y1 + "][" + x5y1 + "]")
    print()

def player_movement():
    global player_loc_x
    global player_loc_y
    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :")
        print()
        if player_choice == "n":
            player_loc_y = player_loc_y + 1
            break
        if player_choice == "s":
            player_loc_y = player_loc_y - 1
            break
        if player_choice == "e":
            player_loc_x = player_loc_x + 1
            break
        if player_choice == "w":
            player_loc_x = player_loc_x - 1
            break
        else:
            print("Invalid input..")
            print()

def room_check():
    global x1y5
    global x1y4
    global x1y3
    global x1y2
    global x1y1
    
    global x2y5
    global x2y4
    global x2y3
    global x2y2
    global x2y1
    
    global x3y5
    global x3y4
    global x3y3
    global x3y2
    global x3y1

    global x4y5
    global x4y4
    global x4y3
    global x4y2
    global x4y1
    
    global x5y5
    global x5y4
    global x5y3
    global x5y2
    global x5y1

    if player_loc_x == 1 and player_loc_y == 3:
        x1y3 = "X"
    else:
        x1y3 = " "
    if player_loc_x == 2 and player_loc_y == 3:
        x2y3 = "X"
    else:
        x2y3 = " "
    if player_loc_x == 3 and player_loc_y == 3:
        x3y3 = "X"
    else:
        x3y3 = " "
    if player_loc_x == 4 and player_loc_y == 3:
        x4y3 = "X"
    else:
        x4y3 = " "
    if player_loc_x == 5 and player_loc_y == 3:
        x5y3 = "X"
    else:
        x5y3 = " "    
    
    if player_loc_x == 1 and player_loc_y == 2:
        x1y2 = "X"
    else:
        x1y2 = " "
    if player_loc_x == 2 and player_loc_y == 2:
        x2y2 = "X"
    else:
        x2y2 = " "
    if player_loc_x == 3 and player_loc_y == 2:
        x3y2 = "X"
    else:
        x3y2 = " "
    if player_loc_x == 4 and player_loc_y == 2:
        x4y2 = "X"
    else:
        x4y2 = " "
    if player_loc_x == 5 and player_loc_y == 2:
        x5y2 = "X"
    else:
        x5y2 = " "    
  
    if player_loc_x == 1 and player_loc_y == 1:
        x1y1 = "X"
    else:
        x1y1 = " "
    if player_loc_x == 2 and player_loc_y == 1:
        x2y1 = "X"
    else:
        x2y1 = " "
    if player_loc_x == 3 and player_loc_y == 1:
        x3y1 = "X"
    else:
        x3y1 = " "
    if player_loc_x == 4 and player_loc_y == 1:
        x4y1 = "X"
    else:
        x4y1 = " "
    if player_loc_x == 5 and player_loc_y == 1:
        x5y1 = "X"
    else:
        x5y1 = " "

    if player_loc_x == 1 and player_loc_y == 4:
        x1y4 = "X"
    else:
        x1y4 = " "
    if player_loc_x == 2 and player_loc_y == 4:
        x2y4 = "X"
    else:
        x2y4 = " "
    if player_loc_x == 3 and player_loc_y == 4:
        x3y4 = "X"
    else:
        x3y4 = " "
    if player_loc_x == 4 and player_loc_y == 4:
        x4y4 = "X"
    else:
        x4y4 = " "
    if player_loc_x == 5 and player_loc_y == 4:
        x5y4 = "X"
    else:
        x5y4 = " "  

    if player_loc_x == 1 and player_loc_y == 5:
        x1y5 = "X"
    else:
        x1y5 = " "
    if player_loc_x == 2 and player_loc_y == 5:
        x2y5 = "X"
    else:
        x2y5 = " "
    if player_loc_x == 3 and player_loc_y == 5:
        x3y5 = "X"
    else:
        x3y5 = " "
    if player_loc_x == 4 and player_loc_y == 5:
        x4y5 = "X"
    else:
        x4y5 = " "
    if player_loc_x == 5 and player_loc_y == 5:
        x5y5 = "X"
    else:
        x5y5 = " "              

def game_loop():                     
    while True:
        grid()
        player_movement()
        room_check()

game_loop()