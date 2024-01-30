'''
if 0 < abs(guess - secret) <= 10:
'''

import random

# default values

player_loc_x = 0
player_loc_y = 0
player_points = 0
creature_01_loc_x = 0
creature_01_loc_y = 0

creature_01_location = "void"

x5y1 = "╝"
x4y1 = "╚"
x3y1 = "╨"
x2y1 = "╝"
x1y1 = "╚"

x5y2 = "╣"
x4y2 = "╦"
x3y2 = "╬"
x2y2 = "╦"
x1y2 = "╠"

x5y3 = "╗"
x4y3 = "╩"
x3y3 = "╦"
x2y3 = "╩"
x1y3 = "╔"

x5y4 = "╝"
x4y4 = "╬"
x3y4 = "╩"
x2y4 = "╬"
x1y4 = "╚"

x5y5 = "╗"
x4y5 = "╔"
x3y5 = "╥"
x2y5 = "╗"
x1y5 = "╔"

# game loop

def game_loop():
    lose_condition()
    creature_01_movement()
    creature_01_grid()
    lose_condition()
    grid_display()
    
# introduction and instructions
    
def intro():
    print('''
          The object of this game is to navigate your smiley ("☻") through a maze while evading the evil smiley ("☺").
          Navigation is done by entering the letter that corresponds with the direction you wish to move and then by
          hitting enter. 
          
          ''')
    input("Press 'enter' to start...")
    room_x3y1()          
# grid display
    
def grid_display():    
    global player_loc_x
    global player_loc_y
    global creature_01_loc_x
    global creature_01_loc_y
    global player_points
    
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
    
    print()
    print("    Score:" + str(player_points))
    print("    " + x1y5 + x2y5 + x3y5 + x4y5 + x5y5)
    print("    " + x1y4 + x2y4 + x3y4 + x4y4 + x5y4)
    print("    " + x1y3 + x2y3 + x3y3 + x4y3 + x5y3)
    print("    " + x1y2 + x2y2 + x3y2 + x4y2 + x5y2)
    print("    " + x1y1 + x2y1 + x3y1 + x4y1 + x5y1)
    print()

# creature movement

def creature_01_movement():
    global creature_01_location
    global creature_01_loc_x
    global creature_01_loc_y
        
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

    if creature_01_location == "void":
        creature_01_location = "x3y5"
    elif creature_01_location == "x1y1":
        x1y1 = "╚"
        choices = ["x2y1", "x1y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y1":
        x2y1 = "╝"
        choices = ["x1y1", "x2y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y1":
        x3y1 = "╨"
        creature_01_location = "x3y2"
    elif creature_01_location == "x4y1":
        x4y1 = "╚"
        choices = ["x4y2", "x5y1"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y1":
        x5y1 = "╝"
        choices = ["x4y1", "x5y2"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y2":
        x1y2 = "╠"
        choices = ["x1y1", "x2y2", "x1y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y2":
        x2y2 = "╦"
        choices = ["x1y2", "x2y1", "x3y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y2":
        x3y2 = "╬"
        choices = ["x2y2", "x3y3", "x3y1", "x4y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y2":
        x4y2 = "╦"
        choices = ["x3y2", "x4y1", "x5y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y2":
        x5y2 = "╣"
        choices = ["x4y2", "x5y1", "x5y3"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y3":
        x1y3 = "╔"
        choices = ["x1y2", "x2y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y3":
        x2y3 = "╩"
        choices = ["x1y3", "x2y4", "x3y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y3":
        x3y3 = "╦"
        choices = ["x2y3", "x3y2", "x4y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y3":
        x4y3 = "╩"
        choices = ["x3y3", "x4y4", "x5y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y3":
        x5y3 = "╗"
        choices = ["x4y3", "x5y2"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y4":
        x1y4 = "╚"
        choices = ["x1y5", "x2y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y4":
        x2y4 = "╬"
        choices = ["x1y4", "x3y4", "x2y5", "x2y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y4":
        x3y4 = "╩"
        choices = ["x2y4", "x3y5", "x4y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y4":
        x4y4 = "╬"
        choices = ["x4y3", "x4y5", "x3y4", "x5y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y4":
        x5y4 = "╝"
        choices = ["x4y4", "x5y5"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y5":
        x1y5 = "╔"
        choices = ["x2y5", "x1y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y5":
        x2y5 = "╗"
        choices = ["x1y5", "x2y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y5":
        x3y5 = "╥"
        creature_01_location = "x3y4"
    elif creature_01_location == "x4y5":
        x4y5 = "╔"
        choices = ["x4y4", "x5y5"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y5":
        x5y5 = "╗"
        choices = ["x4y5", "x5y4"]
        creature_01_location = random.choice(choices)                        

# creature display

def creature_01_grid():
    global creature_01_location
    global creature_01_loc_x
    global creature_01_loc_y

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
     
    if creature_01_location == "x1y1":
        x1y1 = "☺"
    if creature_01_location == "x2y1":
        x2y1 = "☺"
    if creature_01_location == "x3y1":
        x3y1 = "☺"
    if creature_01_location == "x4y1":
        x4y1 = "☺"
    if creature_01_location == "x5y1":
        x5y1 = "☺"
           
    if creature_01_location == "x1y2":
        x1y2 = "☺"
    if creature_01_location == "x2y2":
        x2y2 = "☺"
    if creature_01_location == "x3y2":
        x3y2 = "☺"
    if creature_01_location == "x4y2":  
        x4y2 = "☺"
    if creature_01_location == "x5y2":
        x5y2 = "☺"
               
    if creature_01_location == "x1y3":
        x1y3 = "☺"
    if creature_01_location == "x2y3":
        x2y3 = "☺"
    if creature_01_location == "x3y3":
        x3y3 = "☺"
    if creature_01_location == "x4y3":
        x4y3 = "☺"
    if creature_01_location == "x5y3":
        x5y3 = "☺"
  

    if creature_01_location == "x1y4":
        x1y4 = "☺"
    if creature_01_location == "x2y4":
        x2y4 = "☺"
    if creature_01_location == "x3y4":
        x3y4 = "☺"
    if creature_01_location == "x4y4":
        x4y4 = "☺"
    if creature_01_location == "x5y4":
        x5y4 = "☺"
        

    if creature_01_location == "x1y5":
        x1y5 = "☺"
    if creature_01_location == "x2y5":
        x2y5 = "☺"
    if creature_01_location == "x3y5":
        x3y5 = "☺"
    if creature_01_location == "x4y5":
        x4y5 = "☺"
    if creature_01_location == "x5y5":
        x5y5 = "☺"
                                            

# collision check

def lose_condition():
    if creature_01_location == player_location:
        grid_display()
        input("Game over.")
        exit()

# "rooms"

def room_x1y5():
    global player_loc_x
    global player_loc_y
    global x1y5
    global player_location
    player_location = "x1y5"
    player_loc_x = 1
    player_loc_y = 5
    x1y5 = "☻"
    game_loop()
    x1y5 = "╔"
    while True:
        player_choice = input("(S)outh (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x1y4()
        if player_choice == "e":
            room_x2y5()
        else:
            print("Invalid input..")
            print()

def room_x2y5():
    global player_loc_x
    global player_loc_y
    global x2y5
    global player_location
    player_location = "x2y5"
    player_loc_x = 2
    player_loc_y = 5
    x2y5 = "☻"
    game_loop()
    x2y5 = "╗"
    while True:
        player_choice = input("(S)outh (W)est :").lower()
        print()
        if player_choice == "s":
            room_x2y4()
        if player_choice == "w":
            room_x1y5()
        else:
            print("Invalid input..")
            print()

def room_x3y5():
    global player_loc_x
    global player_loc_y
    global x3y5
    global player_location
    player_location = "x3y5"
    player_loc_x = 3
    player_loc_y = 5
    x3y5 = "☻"
    game_loop()
    x3y5 = "╥"
    while True:
        player_choice = input("(S)outh :").lower()
        print()
        if player_choice == "s":
            room_x3y4()
        else:
            print("Invalid input..")
            print()

def room_x4y5():
    global player_loc_x
    global player_loc_y
    global x4y5
    global player_location
    player_location = "x4y5"
    player_loc_x = 4
    player_loc_y = 5
    x4y5 = "☻"
    game_loop()
    x4y5 = "╔"
    while True:
        player_choice = input("(S)outh (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x4y4()
        if player_choice == "e":
            room_x5y5()
        else:
            print("Invalid input..")
            print()

def room_x5y5():
    global player_loc_x
    global player_loc_y
    global x5y5
    global player_location
    player_location = "x5y5"
    player_loc_x = 5
    player_loc_y = 5
    x5y5 = "☻"
    game_loop()
    x5y5 = "╗"
    while True:
        player_choice = input("(S)outh (W)est: ").lower()
        print()
        if player_choice == "s":
            room_x5y4()
        if player_choice == "w":
            room_x4y5()
        else:
            print("Invalid input..")
            print()

def room_x1y4():
    global player_loc_x
    global player_loc_y
    global x1y4
    global player_location
    player_location = "x1y4"
    player_loc_x = 1
    player_loc_y = 4
    x1y4 = "☻"
    game_loop()
    x1y4 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x1y5()
        if player_choice == "e":
            room_x2y4()
        else:
            print("Invalid input..")
            print()

def room_x2y4():
    global player_loc_x
    global player_loc_y
    global x2y4
    global player_location
    player_location = "x2y4"
    player_loc_x = 2
    player_loc_y = 4
    x2y4 = "☻"
    game_loop()
    x2y4 = "╬"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x2y5()
        if player_choice == "s":
            room_x2y3()
        if player_choice == "e":
            room_x3y4()    
        if player_choice == "w":
            room_x1y4()
        else:
            print("Invalid input..")
            print()

def room_x3y4():
    global player_loc_x
    global player_loc_y
    global x3y4
    global player_location
    global player_choice
    player_location = "x3y4"
    player_loc_x = 3
    player_loc_y = 4
    x3y4 = "☻"
    game_loop()
    x3y4 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :")
        print()
        if player_choice == "n":
            room_x3y5()
        if player_choice == "e":
            room_x4y4()    
        if player_choice == "w":
            room_x2y4()
        else:
            print("Invalid input..")
            print()

def room_x4y4():
    global player_loc_x
    global player_loc_y
    global x4y4
    global player_location
    player_location = "x4y4"
    player_loc_x = 4
    player_loc_y = 4
    x4y4 = "☻"
    game_loop()
    x4y4 = "╬"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x4y5()
        if player_choice == "s":
            room_x4y3()
        if player_choice == "e":
            room_x5y4()
        if player_choice == "w":
            room_x3y4()    
        else:
            print("Invalid input..")
            print()

def room_x5y4():
    global player_loc_x
    global player_loc_y
    global x5y4
    global player_location
    player_location = "x5y4"
    player_loc_x = 5
    player_loc_y = 4
    x5y4 = "☻"
    game_loop()
    x5y4 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :").lower()
        print()
        if player_choice == "n":
            room_x5y5()
        if player_choice == "w":
            room_x4y4()
        else:
            print("Invalid input..")
            print()

def room_x1y3():
    global player_loc_x
    global player_loc_y
    global x1y3
    global player_location
    player_location = "x1y3"
    player_loc_x = 1
    player_loc_y = 3
    x1y3 = "☻"
    game_loop()
    x1y3 = "╔"
    while True:
        player_choice = input("(S)outh (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x1y2()
        if player_choice == "e":
            room_x2y3()
        else:
            print("Invalid input..")
            print()

def room_x2y3():
    global player_loc_x
    global player_loc_y
    global x2y3
    global player_location
    player_location = "x2y3"
    player_loc_x = 2
    player_loc_y = 3
    x2y3 = "☻"
    game_loop()
    x2y3 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x2y4()
        if player_choice == "e":
            room_x3y3()
        if player_choice == "w":
            room_x1y3()
        else:
            print("Invalid input..")
            print()

def room_x3y3():
    global player_loc_x
    global player_loc_y
    global x3y3
    global player_location
    player_location = "x3y3"
    player_loc_x = 3
    player_loc_y = 3
    x3y3 = "☻"
    game_loop()
    x3y3 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "s":
            room_x3y2()
        if player_choice == "e":
            room_x4y3()
        if player_choice == "w":
            room_x2y3()
        else:
            print("Invalid input..")
            print()

def room_x4y3():
    global player_loc_x
    global player_loc_y
    global x4y3
    global player_location
    player_location = "x4y3"
    player_loc_x = 4
    player_loc_y = 3
    x4y3 = "☻"
    game_loop()
    x4y3 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x4y4()
        if player_choice == "e":
            room_x5y3()
        if player_choice == "w":
            room_x3y3()
        else:
            print("Invalid input..")
            print()

def room_x5y3():
    global player_loc_x
    global player_loc_y
    global x5y3
    global player_location
    player_location = "x5y3"
    player_loc_x = 5
    player_loc_y = 3
    x5y3 = "☻"
    game_loop()
    x5y3 = "╗"
    while True:
        player_choice = input("(S)outh (W)est :").lower()
        print()
        if player_choice == "s":
            room_x5y2()
        if player_choice == "w":
            room_x4y3()
        else:
            print("Invalid input..")
            print()                        


def room_x1y2():
    global player_loc_x
    global player_loc_y
    global x1y2
    global player_location
    player_location = "x1y2"
    player_loc_x = 1
    player_loc_y = 2
    x1y2 = "☻"
    game_loop()
    x1y2 = "╠"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast: ").lower()
        print()
        if player_choice == "n":
            room_x1y3()
        if player_choice == "s":
            room_x1y1()
        if player_choice == "e":
            room_x2y2()
        else:
            print("Invalid input..")
            print()

def room_x2y2():
    global player_loc_x
    global player_loc_y
    global x2y2
    global player_location
    player_location = "x2y2"
    player_loc_x = 2
    player_loc_y = 2
    x2y2 = "☻"
    game_loop()
    x2y2 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "s":
            room_x2y1()
        if player_choice == "e":
            room_x3y2()
        if player_choice == "w":
            room_x1y2()
        else:
            print("Invalid input..")
            print()

def room_x3y2():
    global player_loc_x
    global player_loc_y
    global x3y2
    global player_location
    player_location = "x3y2"
    player_loc_x = 3
    player_loc_y = 2
    x3y2 = "☻"
    game_loop()
    x3y2 = "╬"
    while  True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x3y3()
        if player_choice == "s":
            room_x3y1()
        if player_choice == "e":
            room_x4y2()
        if player_choice == "w":
            room_x2y2()
        else:
            print("Invalid input..")
            print()

def room_x4y2():
    global player_loc_x
    global player_loc_y
    global x4y2
    global player_location
    player_location = "x4y2"
    player_loc_x = 4
    player_loc_y = 2
    x4y2 = "☻"
    game_loop()
    x4y2 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "s":
            room_x4y1()
        if player_choice == "e":
            room_x5y2()
        if player_choice == "w":
            room_x3y2()
        else:
            print("Invalid input..")
            print()

def room_x5y2():
    global player_loc_x
    global player_loc_y
    global x5y2
    global player_location
    player_location = "x5y2"
    player_loc_x = 5
    player_loc_y = 2
    x5y2 = "☻"
    game_loop()
    x5y2 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :").lower()
        print()
        if player_choice == "n":
            room_x5y3()
        if player_choice == "s":
            room_x5y1()
        if player_choice == "w":
            room_x4y2()
        else:
            print("Invalid input..")
            print()                        

def room_x1y1():
    global player_loc_x
    global player_loc_y
    global x1y1
    global player_location
    player_location = "x1y1"
    player_loc_x = 1
    player_loc_y = 1
    x1y1 = "☻"
    game_loop()
    x1y1 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x1y2()
        if player_choice == "e":
            room_x2y1()
        else:
            print("Invalid input..")
            print()

def room_x2y1():
    global player_loc_x
    global player_loc_y
    global x2y1
    global player_location
    player_location = "x2y1"
    player_loc_x = 2
    player_loc_y = 1
    x2y1 = "☻"
    game_loop()
    x2y1 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :").lower()
        print()
        if player_choice == "n":
            room_x2y2()
        if player_choice == "w":
            room_x1y1()
        else:
            print("Invalid input..")
            print()

def room_x3y1():
    global player_loc_x
    global player_loc_y
    global x3y1
    global player_location
    global treasure_hold
    global player_choice
    global player_points
    player_location = "x3y1"
    player_loc_x = 3
    player_loc_y = 1
    x3y1 = "☻"
    game_loop()
    x3y1 = "╨"
    while True:
        player_choice = input("(N)orth :").lower()
        print()
        if player_choice == "n":
            room_x3y2()
        else:
            print("Invalid input..")
            print()

def room_x4y1():
    global player_loc_x
    global player_loc_y
    global x4y1
    global player_location
    player_location = "x4y1"
    player_loc_x = 4
    player_loc_y = 1
    x4y1 = "☻"
    game_loop()
    x4y1 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x4y2()
        if player_choice == "e":
            room_x5y1()
        else:
            print("Invalid input..")
            print()

def room_x5y1():
    global player_loc_x
    global player_loc_y
    global x5y1
    global player_location
    player_location = "x5y1"
    player_loc_x = 5
    player_loc_y = 1
    x5y1 = "☻"
    game_loop()
    x5y1 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :").lower()
        print()
        if player_choice == "n":
            room_x5y2()
        if player_choice == "w":
            room_x4y1()
        else:
            print("Invalid input..")
            print()            

# initiate

intro()