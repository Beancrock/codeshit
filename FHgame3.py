'''
Y
6┌───╥───┐
5│╔═╦╩╦═╗│
4│╠╦╩╦╩╦╣│
3╞╣╠═╬═╣╠╡
2│╠╩╦╩╦╩╣│
1│╚═╩╦╩═╝│
0└───╨───┘
/012345678X

if 0 < abs(guess - secret) <= 10:
'''

import random
global high_score
high_score = 0

# default values + introduction and instructions

def intro():
    global player_loc_x
    global player_loc_y
    global player_points
    global turns
    global player_location
    global treasure_location

    global creature_01_loc_x
    global creature_01_loc_y
    global creature_02_loc_x
    global creature_02_loc_y
    global creature_03_loc_x
    global creature_03_loc_y
    global creature_04_loc_x
    global creature_04_loc_y
    
    global creature_01_location
    global creature_02_location
    global creature_03_location
    global creature_04_location

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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1
    
    global n_exit
    global w_exit
    global e_exit
    global s_exit
 
    player_loc_x = 0
    player_loc_y = 0
    player_points = -1
    treasure_location = "x4y3"
    turns = 100
    
    creature_01_loc_x = 0
    creature_01_loc_y = 0
    creature_02_loc_x = 0
    creature_02_loc_y = 0
    creature_03_loc_x = 0
    creature_03_loc_y = 0
    creature_04_loc_x = 0
    creature_04_loc_y = 0
  
    creature_01_location = "void"
    creature_02_location = "void"
    creature_03_location = "void"
    creature_04_location = "void"

    x1y5 = "╔"
    x1y4 = "╠"
    x1y3 = "╣"
    x1y2 = "╠"
    x1y1 = "╚"
    
    x2y5 = "═"
    x2y4 = "╦"
    x2y3 = "╠"
    x2y2 = "╩"
    x2y1 = "═"
    
    x3y5 = "╦"
    x3y4 = "╩"
    x3y3 = "═"
    x3y2 = "╦"
    x3y1 = "╩"

    x4y5 = "╩"
    x4y4 = "╦"
    x4y3 = "╬"
    x4y2 = "╩"
    x4y1 = "╦"
    
    x5y5 = "╦"
    x5y4 = "╩"
    x5y3 = "═"
    x5y2 = "╦"
    x5y1 = "╩"

    x6y5 = "═"
    x6y4 = "╦"
    x6y3 = "╣"
    x6y2 = "╩"
    x6y1 = "═"

    x7y5 = "╗"
    x7y4 = "╣"
    x7y3 = "╠"
    x7y2 = "╣"
    x7y1 = "╝"

    n_exit = "╥"
    w_exit = "╞"
    e_exit = "╡"
    s_exit = "╨"

    print('''
        The object of this game is to navigate your smiley ("☻") through a maze collecting as many diamonds ("♦")
        as you can within the allotted amount of turns while evading the evil smilies ("☺"). Navigation is done by
        entering the letter that corresponds with the direction you wish to move and then by hitting enter. The
        game ends when turns run out or if an evil smiley reaches you.
          
          ''')
    input("Press 'enter' to start...")
    room_x4y3()          

# game loop

def game_loop():
    global turns

    treasure()
    lose_condition()
    creature_01_movement()
    creature_01_grid()
    creature_02_movement()
    creature_02_grid()
    creature_03_movement()
    creature_03_grid()
    creature_04_movement()
    creature_04_grid()
    lose_condition()
    grid_display()
    
    turns = turns - 1

# grid display
    
def grid_display():    
    global player_loc_x
    global player_loc_y
    global creature_01_loc_x
    global creature_01_loc_y
    global player_points
    global high_score
    global turns
    
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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit
    
    print()
    print("Score [" + str(player_points) + "] High [" + str(high_score) + "] Turns [" + str(turns) + "]")
    print()
    print("        ┌───" + n_exit + "───┐")
    print("        │" + x1y5 + x2y5 + x3y5 + x4y5 + x5y5 + x6y5 + x7y5 + "│")
    print("        │" + x1y4 + x2y4 + x3y4 + x4y4 + x5y4 + x6y4 + x7y4 + "│")
    print("        " + w_exit + x1y3 + x2y3 + x3y3 + x4y3 + x5y3 + x6y3 + x7y3 + e_exit)
    print("        │" + x1y2 + x2y2 + x3y2 + x4y2 + x5y2 + x6y2 + x7y2 + "│")
    print("        │" + x1y1 + x2y1 + x3y1 + x4y1 + x5y1 + x6y1 + x7y1 + "│")
    print("        └───" + s_exit + "───┘")
    print()
  
# creature no.1 movement

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
    
    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit

    if creature_01_location == "void":
        creature_01_location = "x1y5"
    elif creature_01_location == "x1y1":
        x1y1 = "╚"
        choices = ["x2y1", "x1y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y1":
        x2y1 = "═"
        choices = ["x1y1", "x3y1"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y1":
        x3y1 = "╩"
        choices = ["x2y1", "x4y1", "x3y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y1":
        x4y1 = "╦"
        choices = ["s_exit", "x3y1", "x5y1"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y1":
        x5y1 = "╩"
        choices = ["x4y1", "x5y1"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y2":
        x1y2 = "╠"
        choices = ["x1y1", "x2y2", "x1y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y2":
        x2y2 = "╩"
        choices = ["x1y2", "x2y3", "x3y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y2":
        x3y2 = "╦"
        choices = ["x2y2", "x3y1", "x4y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y2":
        x4y2 = "╩"
        choices = ["x3y2", "x4y3", "x5y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y2":
        x5y2 = "╦"
        choices = ["x4y2", "x5y1", "x6y2"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y3":
        x1y3 = "╣"
        choices = ["w_exit", "x1y2", "x1y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y3":
        x2y3 = "╠"
        choices = ["x2y2", "x2y4", "x3y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y3":
        x3y3 = "═"
        choices = ["x2y3", "x4y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y3":
        x4y3 = "╬"
        choices = ["x3y3", "x4y4", "x5y3", "x4y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y3":
        x5y3 = "═"
        choices = ["x4y3", "x6y3"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y4":
        x1y4 = "╠"
        choices = ["x1y5", "x2y4", "x1y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y4":
        x2y4 = "╦"
        choices = ["x1y4", "x3y4", "x2y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y4":
        x3y4 = "╩"
        choices = ["x2y4", "x3y5", "x4y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y4":
        x4y4 = "╦"
        choices = ["x4y3", "x3y4", "x5y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y4":
        x5y4 = "╩"
        choices = ["x4y4", "x5y5", "x6y4"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x1y5":
        x1y5 = "╔"
        choices = ["x2y5", "x1y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x2y5":
        x2y5 = "═"
        choices = ["x1y5", "x3y5"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x3y5":
        x3y5 = "╦"
        choices = ["x2y5", "x3y4", "x4y5"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x4y5":
        x4y5 = "╩"
        choices = ["x3y5", "n_exit", "x5y5"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x5y5":
        x5y5 = "╦"
        choices = ["x4y5", "x5y4", "x6y5"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x6y1":
        x6y1 = "═"
        choices = ["x5y1", "x7y1"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x6y2":
        x6y2 = "╩"
        choices = ["x5y2", "x7y2", "x6y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x6y3":
        x6y3 = "╣"
        choices = ["x5y3", "x6y2", "x6y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x6y4":
        x6y4 = "╦"
        choices = ["x5y4", "x6y3", "x7y4"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x6y5":
        x6y5 = "═"
        choices = ["x5y5", "x7y5"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "x7y1":
        x7y1 = "╝"
        choices = ["x6y1", "x7y2"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x7y2":
        x7y2 = "╣"
        choices = ["x6y2", "x7y1", "x7y3"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x7y3":
        x7y3 = "╠"
        choices = ["x7y2", "x7y4", "e_exit"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x7y4":
        x7y4 = "╣"
        choices = ["x7y3", "x7y5"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "x7y5":
        x7y5 = "╗"
        choices = ["x6y5", "x7y4"]
        creature_01_location = random.choice(choices)

    elif creature_01_location == "n_exit":
        n_exit = "╥"
        choices = ["x4y5", "s_exit"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "s_exit":
        s_exit = "╨"
        choices = ["x4y1", "n_exit"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "w_exit":
        w_exit = "╞"
        choices = ["x1y3", "e_exit"]
        creature_01_location = random.choice(choices)
    elif creature_01_location == "e_exit":
        e_exit = "╡"
        choices = ["x7y3", "w_exit"]
        creature_01_location = random.choice(choices)
          
# creature no.1 display

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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit
     
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
    if creature_01_location == "x6y1":
        x6y1 = "☺"
    if creature_01_location == "x7y1":
        x7y1 = "☺"    
           
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
    if creature_01_location == "x6y2":  
        x6y2 = "☺"
    if creature_01_location == "x7y2":
        x7y2 = "☺"    
               
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
    if creature_01_location == "x6y3":
        x6y3 = "☺"
    if creature_01_location == "x7y3":
        x7y3 = "☺"    
  
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
    if creature_01_location == "x6y4":
        x6y4 = "☺"
    if creature_01_location == "x7y4":
        x7y4 = "☺"    
      
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
    if creature_01_location == "x6y5":
        x6y5 = "☺"
    if creature_01_location == "x7y5":
        x7y5 = "☺"

    if creature_01_location == "n_exit":
        n_exit = "☺"
    if creature_01_location == "s_exit":
        s_exit = "☺"
    if creature_01_location == "w_exit":
        w_exit = "☺"
    if creature_01_location == "e_exit":
        e_exit = "☺"        

# creature no.2 movement

def creature_02_movement():
    global creature_02_location
    global creature_02_loc_x
    global creature_02_loc_y
        
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
    
    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit

    if creature_02_location == "void":
        creature_02_location = "x7y5"
    elif creature_02_location == "x1y1":
        x1y1 = "╚"
        choices = ["x2y1", "x1y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x2y1":
        x2y1 = "═"
        choices = ["x1y1", "x3y1"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x3y1":
        x3y1 = "╩"
        choices = ["x2y1", "x4y1", "x3y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x4y1":
        x4y1 = "╦"
        choices = ["s_exit", "x3y1", "x5y1"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x5y1":
        x5y1 = "╩"
        choices = ["x4y1", "x6y1"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x1y2":
        x1y2 = "╠"
        choices = ["x1y1", "x2y2", "x1y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x2y2":
        x2y2 = "╩"
        choices = ["x1y2", "x2y3", "x3y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x3y2":
        x3y2 = "╦"
        choices = ["x2y2", "x3y1", "x4y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x4y2":
        x4y2 = "╩"
        choices = ["x3y2", "x4y3", "x5y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x5y2":
        x5y2 = "╦"
        choices = ["x4y2", "x5y1", "x6y2"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x1y3":
        x1y3 = "╣"
        choices = ["w_exit", "x1y2", "x1y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x2y3":
        x2y3 = "╠"
        choices = ["x2y2", "x2y4", "x3y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x3y3":
        x3y3 = "═"
        choices = ["x2y3", "x4y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x4y3":
        x4y3 = "╬"
        choices = ["x3y3", "x4y4", "x5y3", "x4y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x5y3":
        x5y3 = "═"
        choices = ["x4y3", "x6y3"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x1y4":
        x1y4 = "╠"
        choices = ["x1y5", "x2y4", "x1y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x2y4":
        x2y4 = "╦"
        choices = ["x1y4", "x3y4", "x2y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x3y4":
        x3y4 = "╩"
        choices = ["x2y4", "x3y5", "x4y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x4y4":
        x4y4 = "╦"
        choices = ["x4y3", "x3y4", "x5y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x5y4":
        x5y4 = "╩"
        choices = ["x4y4", "x5y5", "x6y4"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x1y5":
        x1y5 = "╔"
        choices = ["x2y5", "x1y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x2y5":
        x2y5 = "═"
        choices = ["x1y5", "x3y5"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x3y5":
        x3y5 = "╦"
        choices = ["x2y5", "x3y4", "x4y5"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x4y5":
        x4y5 = "╩"
        choices = ["x3y5", "n_exit", "x5y5"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x5y5":
        x5y5 = "╦"
        choices = ["x4y5", "x5y4", "x6y5"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x6y1":
        x6y1 = "═"
        choices = ["x5y1", "x7y1"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x6y2":
        x6y2 = "╩"
        choices = ["x5y2", "x7y2", "x6y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x6y3":
        x6y3 = "╣"
        choices = ["x5y3", "x6y2", "x6y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x6y4":
        x6y4 = "╦"
        choices = ["x5y4", "x6y3", "x7y4"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x6y5":
        x6y5 = "═"
        choices = ["x5y5", "x7y5"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "x7y1":
        x7y1 = "╝"
        choices = ["x6y1", "x7y2"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x7y2":
        x7y2 = "╣"
        choices = ["x6y2", "x7y1", "x7y3"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x7y3":
        x7y3 = "╠"
        choices = ["x7y2", "x7y4", "e_exit"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x7y4":
        x7y4 = "╣"
        choices = ["x7y3", "x7y5"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "x7y5":
        x7y5 = "╗"
        choices = ["x6y5", "x7y4"]
        creature_02_location = random.choice(choices)

    elif creature_02_location == "n_exit":
        n_exit = "╥"
        choices = ["x4y5", "s_exit"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "s_exit":
        s_exit = "╨"
        choices = ["x4y1", "n_exit"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "w_exit":
        w_exit = "╞"
        choices = ["x1y3", "e_exit"]
        creature_02_location = random.choice(choices)
    elif creature_02_location == "e_exit":
        e_exit = "╡"
        choices = ["x7y3", "w_exit"]
        creature_02_location = random.choice(choices)
            

# creature no.2 display

def creature_02_grid():
    global creature_02_location
    global creature_02_loc_x
    global creature_02_loc_y

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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit
     
    if creature_02_location == "x1y1":
        x1y1 = "☺"
    if creature_02_location == "x2y1":
        x2y1 = "☺"
    if creature_02_location == "x3y1":
        x3y1 = "☺"
    if creature_02_location == "x4y1":
        x4y1 = "☺"
    if creature_02_location == "x5y1":
        x5y1 = "☺"
    if creature_02_location == "x6y1":
        x6y1 = "☺"
    if creature_02_location == "x7y1":
        x7y1 = "☺"    
           
    if creature_02_location == "x1y2":
        x1y2 = "☺"
    if creature_02_location == "x2y2":
        x2y2 = "☺"
    if creature_02_location == "x3y2":
        x3y2 = "☺"
    if creature_02_location == "x4y2":  
        x4y2 = "☺"
    if creature_02_location == "x5y2":
        x5y2 = "☺"
    if creature_02_location == "x6y2":  
        x6y2 = "☺"
    if creature_02_location == "x7y2":
        x7y2 = "☺"    
               
    if creature_02_location == "x1y3":
        x1y3 = "☺"
    if creature_02_location == "x2y3":
        x2y3 = "☺"
    if creature_02_location == "x3y3":
        x3y3 = "☺"
    if creature_02_location == "x4y3":
        x4y3 = "☺"
    if creature_02_location == "x5y3":
        x5y3 = "☺"
    if creature_02_location == "x6y3":
        x6y3 = "☺"
    if creature_02_location == "x7y3":
        x7y3 = "☺"    

    if creature_02_location == "x1y4":
        x1y4 = "☺"
    if creature_02_location == "x2y4":
        x2y4 = "☺"
    if creature_02_location == "x3y4":
        x3y4 = "☺"
    if creature_02_location == "x4y4":
        x4y4 = "☺"
    if creature_02_location == "x5y4":
        x5y4 = "☺"
    if creature_02_location == "x6y4":
        x6y4 = "☺"
    if creature_02_location == "x7y4":
        x7y4 = "☺"    
      
    if creature_02_location == "x1y5":
        x1y5 = "☺"
    if creature_02_location == "x2y5":
        x2y5 = "☺"
    if creature_02_location == "x3y5":
        x3y5 = "☺"
    if creature_02_location == "x4y5":
        x4y5 = "☺"
    if creature_02_location == "x5y5":
        x5y5 = "☺"
    if creature_02_location == "x6y5":
        x6y5 = "☺"
    if creature_02_location == "x7y5":
        x7y5 = "☺"

    if creature_02_location == "n_exit":
        n_exit = "☺"
    if creature_02_location == "s_exit":
        s_exit = "☺"
    if creature_02_location == "w_exit":
        w_exit = "☺"
    if creature_02_location == "e_exit":
        e_exit = "☺"        

# creature no.3 movement

def creature_03_movement():
    global creature_03_location
    global creature_03_loc_x
    global creature_03_loc_y
        
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
    
    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit

    if creature_03_location == "void":
        creature_03_location = "x1y1"
    elif creature_03_location == "x1y1":
        x1y1 = "╚"
        choices = ["x2y1", "x1y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x2y1":
        x2y1 = "═"
        choices = ["x1y1", "x3y1"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x3y1":
        x3y1 = "╩"
        choices = ["x2y1", "x4y1", "x3y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x4y1":
        x4y1 = "╦"
        choices = ["s_exit", "x3y1", "x5y1"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x5y1":
        x5y1 = "╩"
        choices = ["x4y1", "x6y1"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x1y2":
        x1y2 = "╠"
        choices = ["x1y1", "x2y2", "x1y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x2y2":
        x2y2 = "╩"
        choices = ["x1y2", "x2y3", "x3y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x3y2":
        x3y2 = "╦"
        choices = ["x2y2", "x3y1", "x4y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x4y2":
        x4y2 = "╩"
        choices = ["x3y2", "x4y3", "x5y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x5y2":
        x5y2 = "╦"
        choices = ["x4y2", "x5y1", "x6y2"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x1y3":
        x1y3 = "╣"
        choices = ["w_exit", "x1y2", "x1y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x2y3":
        x2y3 = "╠"
        choices = ["x2y2", "x2y4", "x3y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x3y3":
        x3y3 = "═"
        choices = ["x2y3", "x4y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x4y3":
        x4y3 = "╬"
        choices = ["x3y3", "x4y4", "x5y3", "x4y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x5y3":
        x5y3 = "═"
        choices = ["x4y3", "x6y3"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x1y4":
        x1y4 = "╠"
        choices = ["x1y5", "x2y4", "x1y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x2y4":
        x2y4 = "╦"
        choices = ["x1y4", "x3y4", "x2y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x3y4":
        x3y4 = "╩"
        choices = ["x2y4", "x3y5", "x4y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x4y4":
        x4y4 = "╦"
        choices = ["x4y3", "x3y4", "x5y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x5y4":
        x5y4 = "╩"
        choices = ["x4y4", "x5y5", "x6y4"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x1y5":
        x1y5 = "╔"
        choices = ["x2y5", "x1y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x2y5":
        x2y5 = "═"
        choices = ["x1y5", "x3y5"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x3y5":
        x3y5 = "╦"
        choices = ["x2y5", "x3y4", "x4y5"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x4y5":
        x4y5 = "╩"
        choices = ["x3y5", "n_exit", "x5y5"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x5y5":
        x5y5 = "╦"
        choices = ["x4y5", "x5y4", "x6y5"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x6y1":
        x6y1 = "═"
        choices = ["x5y1", "x7y1"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x6y2":
        x6y2 = "╩"
        choices = ["x5y2", "x7y2", "x6y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x6y3":
        x6y3 = "╣"
        choices = ["x5y3", "x6y2", "x6y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x6y4":
        x6y4 = "╦"
        choices = ["x5y4", "x6y3", "x7y4"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x6y5":
        x6y5 = "═"
        choices = ["x5y5", "x7y5"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "x7y1":
        x7y1 = "╝"
        choices = ["x6y1", "x7y2"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x7y2":
        x7y2 = "╣"
        choices = ["x6y2", "x7y1", "x7y3"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x7y3":
        x7y3 = "╠"
        choices = ["x7y2", "x7y4", "e_exit"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x7y4":
        x7y4 = "╣"
        choices = ["x7y3", "x7y5"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "x7y5":
        x7y5 = "╗"
        choices = ["x6y5", "x7y4"]
        creature_03_location = random.choice(choices)

    elif creature_03_location == "n_exit":
        n_exit = "╥"
        choices = ["x4y5", "s_exit"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "s_exit":
        s_exit = "╨"
        choices = ["x4y1", "n_exit"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "w_exit":
        w_exit = "╞"
        choices = ["x1y3", "e_exit"]
        creature_03_location = random.choice(choices)
    elif creature_03_location == "e_exit":
        e_exit = "╡"
        choices = ["x7y3", "w_exit"]
        creature_03_location = random.choice(choices)
            
# creature no.3 display

def creature_03_grid():
    global creature_03_location
    global creature_03_loc_x
    global creature_03_loc_y

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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit
     
    if creature_03_location == "x1y1":
        x1y1 = "☺"
    if creature_03_location == "x2y1":
        x2y1 = "☺"
    if creature_03_location == "x3y1":
        x3y1 = "☺"
    if creature_03_location == "x4y1":
        x4y1 = "☺"
    if creature_03_location == "x5y1":
        x5y1 = "☺"
    if creature_03_location == "x6y1":
        x6y1 = "☺"
    if creature_03_location == "x7y1":
        x7y1 = "☺"    
           
    if creature_03_location == "x1y2":
        x1y2 = "☺"
    if creature_03_location == "x2y2":
        x2y2 = "☺"
    if creature_03_location == "x3y2":
        x3y2 = "☺"
    if creature_03_location == "x4y2":  
        x4y2 = "☺"
    if creature_03_location == "x5y2":
        x5y2 = "☺"
    if creature_03_location == "x6y2":  
        x6y2 = "☺"
    if creature_03_location == "x7y2":
        x7y2 = "☺"    
               
    if creature_03_location == "x1y3":
        x1y3 = "☺"
    if creature_03_location == "x2y3":
        x2y3 = "☺"
    if creature_03_location == "x3y3":
        x3y3 = "☺"
    if creature_03_location == "x4y3":
        x4y3 = "☺"
    if creature_03_location == "x5y3":
        x5y3 = "☺"
    if creature_03_location == "x6y3":
        x6y3 = "☺"
    if creature_03_location == "x7y3":
        x7y3 = "☺"    
  
    if creature_03_location == "x1y4":
        x1y4 = "☺"
    if creature_03_location == "x2y4":
        x2y4 = "☺"
    if creature_03_location == "x3y4":
        x3y4 = "☺"
    if creature_03_location == "x4y4":
        x4y4 = "☺"
    if creature_03_location == "x5y4":
        x5y4 = "☺"
    if creature_03_location == "x6y4":
        x6y4 = "☺"
    if creature_03_location == "x7y4":
        x7y4 = "☺"    
        
    if creature_03_location == "x1y5":
        x1y5 = "☺"
    if creature_03_location == "x2y5":
        x2y5 = "☺"
    if creature_03_location == "x3y5":
        x3y5 = "☺"
    if creature_03_location == "x4y5":
        x4y5 = "☺"
    if creature_03_location == "x5y5":
        x5y5 = "☺"
    if creature_03_location == "x6y5":
        x6y5 = "☺"
    if creature_03_location == "x7y5":
        x7y5 = "☺"

    if creature_03_location == "n_exit":
        n_exit = "☺"
    if creature_03_location == "s_exit":
        s_exit = "☺"
    if creature_03_location == "w_exit":
        w_exit = "☺"
    if creature_03_location == "e_exit":
        e_exit = "☺"        

# creature no.4 movement

def creature_04_movement():
    global creature_04_location
    global creature_04_loc_x
    global creature_04_loc_y
        
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
    
    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit

    if creature_04_location == "void":
        creature_04_location = "x7y1"
    elif creature_04_location == "x1y1":
        x1y1 = "╚"
        choices = ["x2y1", "x1y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x2y1":
        x2y1 = "═"
        choices = ["x1y1", "x3y1"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x3y1":
        x3y1 = "╩"
        choices = ["x2y1", "x4y1", "x3y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x4y1":
        x4y1 = "╦"
        choices = ["s_exit", "x3y1", "x5y1"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x5y1":
        x5y1 = "╩"
        choices = ["x4y1", "x6y1"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x1y2":
        x1y2 = "╠"
        choices = ["x1y1", "x2y2", "x1y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x2y2":
        x2y2 = "╩"
        choices = ["x1y2", "x2y3", "x3y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x3y2":
        x3y2 = "╦"
        choices = ["x2y2", "x3y1", "x4y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x4y2":
        x4y2 = "╩"
        choices = ["x3y2", "x4y3", "x5y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x5y2":
        x5y2 = "╦"
        choices = ["x4y2", "x5y1", "x6y2"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x1y3":
        x1y3 = "╣"
        choices = ["w_exit", "x1y2", "x1y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x2y3":
        x2y3 = "╠"
        choices = ["x2y2", "x2y4", "x3y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x3y3":
        x3y3 = "═"
        choices = ["x2y3", "x4y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x4y3":
        x4y3 = "╬"
        choices = ["x3y3", "x4y4", "x5y3", "x4y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x5y3":
        x5y3 = "═"
        choices = ["x4y3", "x6y3"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x1y4":
        x1y4 = "╠"
        choices = ["x1y5", "x2y4", "x1y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x2y4":
        x2y4 = "╦"
        choices = ["x1y4", "x3y4", "x2y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x3y4":
        x3y4 = "╩"
        choices = ["x2y4", "x3y5", "x4y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x4y4":
        x4y4 = "╦"
        choices = ["x4y3", "x3y4", "x5y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x5y4":
        x5y4 = "╩"
        choices = ["x4y4", "x5y5", "x6y4"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x1y5":
        x1y5 = "╔"
        choices = ["x2y5", "x1y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x2y5":
        x2y5 = "═"
        choices = ["x1y5", "x3y5"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x3y5":
        x3y5 = "╦"
        choices = ["x2y5", "x3y4", "x4y5"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x4y5":
        x4y5 = "╩"
        choices = ["x3y5", "n_exit", "x5y5"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x5y5":
        x5y5 = "╦"
        choices = ["x4y5", "x5y4", "x6y5"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x6y1":
        x6y1 = "═"
        choices = ["x5y1", "x7y1"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x6y2":
        x6y2 = "╩"
        choices = ["x5y2", "x7y2", "x6y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x6y3":
        x6y3 = "╣"
        choices = ["x5y3", "x6y2", "x6y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x6y4":
        x6y4 = "╦"
        choices = ["x5y4", "x6y3", "x7y4"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x6y5":
        x6y5 = "═"
        choices = ["x5y5", "x7y5"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "x7y1":
        x7y1 = "╝"
        choices = ["x6y1", "x7y2"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x7y2":
        x7y2 = "╣"
        choices = ["x6y2", "x7y1", "x7y3"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x7y3":
        x7y3 = "╠"
        choices = ["x7y2", "x7y4", "e_exit"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x7y4":
        x7y4 = "╣"
        choices = ["x7y3", "x7y5"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "x7y5":
        x7y5 = "╗"
        choices = ["x6y5", "x7y4"]
        creature_04_location = random.choice(choices)

    elif creature_04_location == "n_exit":
        n_exit = "╥"
        choices = ["x4y5", "s_exit"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "s_exit":
        s_exit = "╨"
        choices = ["x4y1", "n_exit"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "w_exit":
        w_exit = "╞"
        choices = ["x1y3", "e_exit"]
        creature_04_location = random.choice(choices)
    elif creature_04_location == "e_exit":
        e_exit = "╡"
        choices = ["x7y3", "w_exit"]
        creature_04_location = random.choice(choices)
         
# creature no.4 display

def creature_04_grid():
    global creature_04_location
    global creature_04_loc_x
    global creature_04_loc_y

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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1

    global n_exit
    global w_exit
    global e_exit
    global s_exit
     
    if creature_04_location == "x1y1":
        x1y1 = "☺"
    if creature_04_location == "x2y1":
        x2y1 = "☺"
    if creature_04_location == "x3y1":
        x3y1 = "☺"
    if creature_04_location == "x4y1":
        x4y1 = "☺"
    if creature_04_location == "x5y1":
        x5y1 = "☺"
    if creature_04_location == "x6y1":
        x6y1 = "☺"
    if creature_04_location == "x7y1":
        x7y1 = "☺"    
           
    if creature_04_location == "x1y2":
        x1y2 = "☺"
    if creature_04_location == "x2y2":
        x2y2 = "☺"
    if creature_04_location == "x3y2":
        x3y2 = "☺"
    if creature_04_location == "x4y2":  
        x4y2 = "☺"
    if creature_04_location == "x5y2":
        x5y2 = "☺"
    if creature_04_location == "x6y2":  
        x6y2 = "☺"
    if creature_04_location == "x7y2":
        x7y2 = "☺"    
               
    if creature_04_location == "x1y3":
        x1y3 = "☺"
    if creature_04_location == "x2y3":
        x2y3 = "☺"
    if creature_04_location == "x3y3":
        x3y3 = "☺"
    if creature_04_location == "x4y3":
        x4y3 = "☺"
    if creature_04_location == "x5y3":
        x5y3 = "☺"
    if creature_04_location == "x6y3":
        x6y3 = "☺"
    if creature_04_location == "x7y3":
        x7y3 = "☺"    
  
    if creature_04_location == "x1y4":
        x1y4 = "☺"
    if creature_04_location == "x2y4":
        x2y4 = "☺"
    if creature_04_location == "x3y4":
        x3y4 = "☺"
    if creature_04_location == "x4y4":
        x4y4 = "☺"
    if creature_04_location == "x5y4":
        x5y4 = "☺"
    if creature_04_location == "x6y4":
        x6y4 = "☺"
    if creature_04_location == "x7y4":
        x7y4 = "☺"    
     
    if creature_04_location == "x1y5":
        x1y5 = "☺"
    if creature_04_location == "x2y5":
        x2y5 = "☺"
    if creature_04_location == "x3y5":
        x3y5 = "☺"
    if creature_04_location == "x4y5":
        x4y5 = "☺"
    if creature_04_location == "x5y5":
        x5y5 = "☺"
    if creature_04_location == "x6y5":
        x6y5 = "☺"
    if creature_04_location == "x7y5":
        x7y5 = "☺"

    if creature_04_location == "n_exit":
        n_exit = "☺"
    if creature_04_location == "s_exit":
        s_exit = "☺"
    if creature_04_location == "w_exit":
        w_exit = "☺"
    if creature_04_location == "e_exit":
        e_exit = "☺"                

# scoring

def treasure():
    global treasure_location
    global player_location
    global player_points
    global high_score


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

    global x6y5
    global x6y4
    global x6y3
    global x6y2
    global x6y1

    global x7y5
    global x7y4
    global x7y3
    global x7y2
    global x7y1
      
    if treasure_location == player_location:
        player_points = player_points + 1
        choices = ["x1y1", "x2y1", "x3y1", "x4y1", "x5y1", "x6y1", "x7y1", "x1y2", "x2y2", "x3y2", "x4y2", "x5y2", "x6y2", "x7y2", "x1y3", "x2y3", "x3y3", "x4y3", "x5y3", "x6y3", "x7y3", "x1y4", "x2y4", "x3y4", "x4y4", "x5y4", "x6y4", "x7y4", "x1y5", "x2y5", "x3y5", "x4y5", "x5y5", "x6y5", "x7y5"]
        treasure_location = random.choice(choices)

    if player_points > high_score:
        high_score = player_points
      
    if treasure_location == "x1y1":
        x1y1 = "♦"
    if treasure_location == "x2y1":
        x2y1 = "♦"
    if treasure_location == "x3y1":
        x3y1 = "♦"
    if treasure_location == "x4y1":
        x4y1 = "♦"
    if treasure_location == "x5y1":
        x5y1 = "♦"
    if treasure_location == "x6y1":
        x6y1 = "♦"
    if treasure_location == "x7y1":
        x7y1 = "♦"    
           
    if treasure_location == "x1y2":
        x1y2 = "♦"
    if treasure_location == "x2y2":
        x2y2 = "♦"
    if treasure_location == "x3y2":
        x3y2 = "♦"
    if treasure_location == "x4y2":  
        x4y2 = "♦"
    if treasure_location == "x5y2":
        x5y2 = "♦"
    if treasure_location == "x6y2":  
        x6y2 = "♦"
    if treasure_location == "x7y2":
        x7y2 = "♦"    
               
    if treasure_location == "x1y3":
        x1y3 = "♦"
    if treasure_location == "x2y3":
        x2y3 = "♦"
    if treasure_location == "x3y3":
        x3y3 = "♦"
    if treasure_location == "x4y3":
        x4y3 = "♦"
    if treasure_location == "x5y3":
        x5y3 = "♦"
    if treasure_location == "x6y3":
        x6y3 = "♦"
    if treasure_location == "x7y3":
        x7y3 = "♦"    
  
    if treasure_location == "x1y4":
        x1y4 = "♦"
    if treasure_location == "x2y4":
        x2y4 = "♦"
    if treasure_location == "x3y4":
        x3y4 = "♦"
    if treasure_location == "x4y4":
        x4y4 = "♦"
    if treasure_location == "x5y4":
        x5y4 = "♦"
    if treasure_location == "x6y4":
        x6y4 = "♦"
    if treasure_location == "x7y4":
        x7y4 = "♦"    
     
    if treasure_location == "x1y5":
        x1y5 = "♦"
    if treasure_location == "x2y5":
        x2y5 = "♦"
    if treasure_location == "x3y5":
        x3y5 = "♦"
    if treasure_location == "x4y5":
        x4y5 = "♦"
    if treasure_location == "x5y5":
        x5y5 = "♦"
    if treasure_location == "x6y5":
        x6y5 = "♦"
    if treasure_location == "x7y5":
        x7y5 = "♦"

# collision and turn check

def lose_condition():
    global player_location
    global creature_01_location
    global creature_02_location
    global turns
    
    if player_location == creature_01_location or player_location == creature_02_location or player_location == creature_03_location or player_location == creature_04_location or turns == 0:
        grid_display()
        while True:
            player_choice = input("Game over. Play again? (Y)es/(N)o :").lower()
            print()
            if player_choice == "y":
                intro()
            if player_choice == "n":
                exit()
            else:
                print("Invalid input..")

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
    x2y5 = "═"
    while True:
        player_choice = input("(W)est (E)ast:").lower()
        print()
        if player_choice == "e":
            room_x3y5()
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
    x3y5 = "╦"
    while True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x3y4()
        if player_choice == "w":
            room_x2y5()
        if player_choice == "e":
            room_x4y5()       
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
    x4y5 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast :").lower()
        print()
        if player_choice == "n":
            north_warp()
        if player_choice == "w":
            room_x3y5()
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
    x5y5 = "╦"
    while True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x5y4()
        if player_choice == "w":
            room_x4y5()
        if player_choice == "e":
            room_x6y5()    
        else:
            print("Invalid input..")
            print()

def room_x6y5():
    global player_loc_x
    global player_loc_y
    global x6y5
    global player_location
    player_location = "x6y5"
    player_loc_x = 6
    player_loc_y = 5
    x6y5 = "☻"
    game_loop()
    x6y5 = "═"
    while True:
        player_choice = input("(W)est (E)ast :").lower()
        print()
        if player_choice == "w":
            room_x5y5()
        if player_choice == "e":
            room_x7y5()
        else:
            print("Invalid input..")
            print()

def room_x7y5():
    global player_loc_x
    global player_loc_y
    global x7y5
    global player_location
    player_location = "x7y5"
    player_loc_x = 7
    player_loc_y = 5
    x7y5 = "☻"
    game_loop()
    x7y5 = "╗"
    while True:
        player_choice = input("(S)outh (W)est :").lower()
        print()
        if player_choice == "s":
            room_x7y4()
        if player_choice == "w":
            room_x6y5()
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
    x1y4 = "╠"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x1y5()
        if player_choice == "s":
            room_x1y3()    
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
    x2y4 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :").lower()
        print()
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
        player_choice = input("(N)orth (E)ast (W)est :").lower()
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
    x4y4 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :").lower()
        print()
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
    x5y4 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x5y5()
        if player_choice == "w":
            room_x4y4()
        if player_choice == "e":
            room_x6y4()    
        else:
            print("Invalid input..")
            print()

def room_x6y4():
    global player_loc_x
    global player_loc_y
    global x6y4
    global player_location
    player_location = "x6y4"
    player_loc_x = 6
    player_loc_y = 4
    x6y4 = "☻"
    game_loop()
    x6y4 = "╦"
    while True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x6y3()
        if player_choice == "w":
            room_x5y4()
        if player_choice == "e":
            room_x7y4()    
        else:
            print("Invalid input..")
            print()

def room_x7y4():
    global player_loc_x
    global player_loc_y
    global x7y4
    global player_location
    player_location = "x7y4"
    player_loc_x = 7
    player_loc_y = 4
    x7y4 = "☻"
    game_loop()
    x7y4 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :").lower()
        print()
        if player_choice == "n":
            room_x7y5()
        if player_choice == "s":
            room_x7y3()    
        if player_choice == "w":
            room_x6y4()
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
    x1y3 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :").lower()
        print()
        if player_choice == "n":
            room_x1y4()
        if player_choice == "s":
            room_x1y2()
        if player_choice == "w":
            west_warp()
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
    x2y3 = "╠"
    while True:
        player_choice = input("(N)orth (E)ast (S)outh :").lower()
        print()
        if player_choice == "n":
            room_x2y4()
        if player_choice == "s":
            room_x2y2()
        if player_choice == "e":
            room_x3y3()
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
    x3y3 = "═"
    while True:
        player_choice = input("(E)ast (W)est :").lower()
        print()
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
    x4y3 = "╬"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x4y4()
        if player_choice == "s":
            room_x4y2()    
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
    x5y3 = "═"
    while True:
        player_choice = input("(W)est (E)ast :").lower()
        print()
        if player_choice == "w":
            room_x4y3()
        if player_choice == "e":
            room_x6y3()
        else:
            print("Invalid input..")
            print()

def room_x6y3():
    global player_loc_x
    global player_loc_y
    global x6y3
    global player_location
    player_location = "x6y3"
    player_loc_x = 6
    player_loc_y = 3
    x6y3 = "☻"
    game_loop()
    x6y3 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :").lower()
        print()
        if player_choice == "n":
            room_x6y4()
        if player_choice == "s":
            room_x6y2()    
        if player_choice == "w":
            room_x5y3()
        else:
            print("Invalid input..")
            print()

def room_x7y3():
    global player_loc_x
    global player_loc_y
    global x7y3
    global player_location
    player_location = "x7y3"
    player_loc_x = 7
    player_loc_y = 3
    x7y3 = "☻"
    game_loop()
    x7y3 = "╠"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x7y4()
        if player_choice == "s":
            room_x7y2()    
        if player_choice == "e":
            east_warp()
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
    x2y2 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x2y3()
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
    x3y2 = "╦"
    while  True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
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
    x4y2 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x4y3()
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
    x5y2 = "╦"
    while True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
        if player_choice == "s":
            room_x5y1()
        if player_choice == "e":
            room_x6y2()
        if player_choice == "w":
            room_x4y2()
        else:
            print("Invalid input..")
            print()

def room_x6y2():
    global player_loc_x
    global player_loc_y
    global x6y2
    global player_location
    player_location = "x6y2"
    player_loc_x = 6
    player_loc_y = 2
    x6y2 = "☻"
    game_loop()
    x6y2 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast :").lower()
        print()
        if player_choice == "n":
            room_x6y3()
        if player_choice == "w":
            room_x5y2()
        if player_choice == "e":
            room_x7y2()    
        else:
            print("Invalid input..")
            print()

def room_x7y2():
    global player_loc_x
    global player_loc_y
    global x7y2
    global player_location
    player_location = "x7y2"
    player_loc_x = 7
    player_loc_y = 2
    x7y2 = "☻"
    game_loop()
    x7y2 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :").lower()
        print()
        if player_choice == "n":
            room_x7y3()
        if player_choice == "s":
            room_x7y1()    
        if player_choice == "w":
            room_x6y2()
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
    x2y1 = "═"
    while True:
        player_choice = input("(W)est (E)ast :").lower()
        print()
        if player_choice == "w":
            room_x1y1()
        if player_choice == "e":
            room_x3y1()
        else:
            print("Invalid input..")
            print()

def room_x3y1():
    global player_loc_x
    global player_loc_y
    global x3y1
    global player_location
    player_location = "x3y1"
    player_loc_x = 3
    player_loc_y = 1
    x3y1 = "☻"
    game_loop()
    x3y1 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            room_x3y2()
        if player_choice == "w":
            room_x2y1()
        if player_choice == "e":
            room_x4y1()    
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
    x4y1 = "╦"
    while True:
        player_choice = input("(S)outh (W)est (E)ast :").lower()
        print()
        if player_choice == "w":
            room_x3y1()
        if player_choice == "e":
            room_x5y1()
        if player_choice == "s":
            south_warp()    
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
    x5y1 = "╩"
    while True:
        player_choice = input("(N)orth (W)est (E)ast:").lower()
        print()
        if player_choice == "n":
            room_x5y2()
        if player_choice == "w":
            room_x4y1()
        if player_choice == "e":
            room_x6y1()    
        else:
            print("Invalid input..")
            print()            

def room_x6y1():
    global player_loc_x
    global player_loc_y
    global x6y1
    global player_location
    player_location = "x6y1"
    player_loc_x = 6
    player_loc_y = 1
    x6y1 = "☻"
    game_loop()
    x6y1 = "═"
    while True:
        player_choice = input("(W)est (E)ast :").lower()
        print()
        if player_choice == "w":
            room_x5y1()
        if player_choice == "e":
            room_x7y1()
        else:
            print("Invalid input..")
            print()

def room_x7y1():
    global player_loc_x
    global player_loc_y
    global x7y1
    global player_location
    player_location = "x7y1"
    player_loc_x = 7
    player_loc_y = 1
    x7y1 = "☻"
    game_loop()
    x7y1 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :").lower()
        print()
        if player_choice == "n":
            room_x7y2()
        if player_choice == "w":
            room_x6y1()
        else:
            print("Invalid input..")
            print()

def north_warp():
    global player_loc_x
    global player_loc_y
    global n_exit
    global player_location
    player_location = "n_exit"
    player_loc_x = 4
    player_loc_y = 6
    n_exit = "☻"
    game_loop()
    n_exit = "╥"
    while True:
        player_choice = input("(S)outh (T)eleport :").lower()
        print()
        if player_choice == "s":
            room_x4y5()
        if player_choice == "t":
            south_warp()
        else:
            print("Invalid input..")
            print()

def south_warp():
    global player_loc_x
    global player_loc_y
    global s_exit
    global player_location
    player_location = "s_exit"
    player_loc_x = 4
    player_loc_y = 0
    s_exit = "☻"
    game_loop()
    s_exit = "╨"
    while True:
        player_choice = input("(N)orth (T)eleport :").lower()
        print()
        if player_choice == "n":
            room_x4y1()
        if player_choice == "t":
            north_warp()
        else:
            print("Invalid input..")
            print()

def west_warp():
    global player_loc_x
    global player_loc_y
    global w_exit
    global player_location
    player_location = "w_exit"
    player_loc_x = 0
    player_loc_y = 3
    w_exit = "☻"
    game_loop()
    w_exit = "╞"
    while True:
        player_choice = input("(E)ast (T)eleport :").lower()
        print()
        if player_choice == "e":
            room_x1y3()
        if player_choice == "t":
            east_warp()
        else:
            print("Invalid input..")
            print()

def east_warp():
    global player_loc_x
    global player_loc_y
    global e_exit
    global player_location
    player_location = "e_exit"
    player_loc_x = 8
    player_loc_y = 3
    e_exit = "☻"
    game_loop()
    e_exit = "╡"
    while True:
        player_choice = input("(W)est (T)eleport :").lower()
        print()
        if player_choice == "w":
            room_x7y3()
        if player_choice == "t":
            west_warp()
        else:
            print("Invalid input..")
            print()                                                                        

# initiate

intro()