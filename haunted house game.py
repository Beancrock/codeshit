import random

location_phantom = "z2"
location_wraith = "e3"
health_points = 5
item_key = False
item_sigil = False
medical_1 = True
medical_2 = True

# Health Display

def health_display():
    global health_points
    global item_key
    global item_sigil
    if health_points == 5:
        print("\u2665 \u2665 \u2665 \u2665 \u2665")
    if health_points == 4:
        print("\u2665 \u2665 \u2665 \u2665")
    if health_points == 3:
        print("\u2665 \u2665 \u2665")
    if health_points == 2:
        print("\u2665 \u2665")
    if health_points == 1:
        print("\u2665")
    if health_points <= 0:
        print("*dead*\n")
        game_over()
    if item_key == False:
        show_key = ("")
    if item_key == True:
        show_key = ("🗝")
    if item_sigil == False:
        show_sigil = ("")
    if item_sigil == True:
        show_sigil = ("⛧")
    print(show_sigil + show_key)            

# Game Over

def game_over():
    print("-Game Over-\n")
    input("Thanks for playing (I'm sorry)! ⏎\n")
    exit()

# Phantom Movement

def phantom_movement():
    global location_phantom
    if location_phantom == "a1":
      choices = ["a2", "b1"]
      location_phantom = random.choice(choices)
    elif location_phantom == "a2":
      print("You hear footsteps in the living room.\n")
      choices = ["a1", "a3", "b2"]
      location_phantom = random.choice(choices)
    elif location_phantom == "a3":
      location_phantom = "a2"
    elif location_phantom == "b1":
      print("You hear the stairs creak.\n")
      choices = ["b2", "a1", "e1", "y1"]
      location_phantom = random.choice(choices)
    elif location_phantom == "b2":
      choices = ["b1", "b3", "a2", "c2"]
      location_phantom = random.choice(choices)
    elif location_phantom == "b3":
       choices = ["c3", "b2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "c1":
       print("You hear raspy chanting from the washroom.\n")
       choices = ["c2", "f1"]
       location_phantom = random.choice(choices)
    elif location_phantom == "c2":
       choices = ["c1", "c3", "b2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "c3":
       print("You hear plates rattle in the kitchen.\n")
       choices = ["c2", "b3"]
       location_phantom = random.choice(choices)
    elif location_phantom == "d1":
       location_phantom = "d2"
    elif location_phantom == "d2":
       print("You hear a shriek from the lounge.\n")
       choices = ["d1", "d3", "e2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "d3":
       choices = ["d2", "e3"]
       location_phantom = random.choice(choices)
    elif location_phantom == "e1":
       print("You hear the stairs creak.\n")
       choices = ["e2", "b1", "q1"]
       location_phantom = random.choice(choices)
    elif location_phantom == "e2":
       choices = ["e1", "d2", "f2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "e3":
       location_phantom = "d3"
    elif location_phantom == "f1":
       print("You hear raspy chanting from the bathroom.\n")
       choices = ["c1", "f2"]
       location_wraith = random.choice(choices)
    elif location_phantom == "f2":
       print("You hear footsteps in the corridor.\n")
       choices = ["f1", "f3", "e2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "f3":
       location_phantom = "f2"
    elif location_phantom == "q1":
       print("You hear the stairs creak.\n")
       choices = ["e1", "q2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "q2":
       choices = ["q1", "q3", "r2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "q3":
       print("You hear Wailing from the garret.\n")
       location_phantom = "q2"
    elif location_phantom == "r2":
       location_phantom = "q2"   
    elif location_phantom == "x1":
       print("You hear bottles shattering in the wine cellar.\n")
       choices = ["y1", "x2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "x2":
       choices = ["x1", "y2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "y1":
       print("You hear the stairs creak.\n")
       choices = ["x1", "y2", "b1"]
       location_phantom = random.choice(choices)
    elif location_phantom == "y2":
       choices = ["y1", "x2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "z1":
       choices = ["y1", "z2"]
       location_phantom = random.choice(choices)
    elif location_phantom == "z2":
       location_phantom = "z1"

# Wraith Movement

def wraith_movement():
    global location_wraith
    if location_wraith == "a1":
      choices = ["a2", "b1"]
      location_phantom = random.choice(choices)
    elif location_wraith == "a2":
      print("You hear footsteps in the living room.\n")
      choices = ["a1", "a3", "b2"]
      location_wraith = random.choice(choices)
    elif location_wraith == "a3":
      location_wraith = "a2"
    elif location_wraith == "b1":
      print("You hear the stairs creak.\n")
      choices = ["b2", "a1", "e1", "y1"]
      location_wraith = random.choice(choices)
    elif location_wraith == "b2":
      choices = ["b1", "b3", "a2", "c2"]
      location_wraith = random.choice(choices)
    elif location_wraith == "b3":
       choices = ["c3", "b2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "c1":
       print("You hear raspy chanting from the washroom.\n")
       choices = ["c2", "f1"]
       location_wraith = random.choice(choices)
    elif location_wraith == "c2":
       choices = ["c1", "c3", "b2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "c3":
       choices = ["c2", "b3"]
       location_wraith = random.choice(choices)
    elif location_wraith == "d1":
       location_wraith = "d2"
    elif location_wraith == "d2":
       print("You hear a shriek from the lounge.\n")
       choices = ["d1", "d3", "e2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "d3":
       choices = ["d2", "e3"]
       location_wraith = random.choice(choices)
    elif location_wraith == "e1":
       print("You hear the stairs creak.\n")
       choices = ["e2", "b1", "q1"]
       location_wraith = random.choice(choices)
    elif location_wraith == "e2":
       choices = ["e1", "d2", "f2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "e3":
       location_wraith = "d3"
    elif location_wraith == "f1":
       print("You hear raspy chanting from the bathroom.\n")
       choices = ["c1", "f2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "f2":
       print("You hear footsteps in the corridor.\n")
       choices = ["f1", "f3", "e2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "f3":
       location_wraith = "f2"
    elif location_wraith == "q1":
       print("You hear the stairs creak.\n")
       choices = ["e1", "q2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "q2":
       choices = ["q1", "q3"]
       location_wraith = random.choice(choices)
    elif location_wraith == "q3":
       print("You hear wailing from the garret.\n")
       location_wraith = "q2"
    elif location_wraith == "x1":
       print("You hear bottles shattering in the win cellar.")
       choices = ["y1", "x2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "x2":
       choices = ["x1", "y2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "y1":
       print("You hear the stairs creak.\n")
       choices = ["x1", "y2", "b1"]
       location_wraith = random.choice(choices)
    elif location_wraith == "y2":
       choices = ["y1", "x2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "z1":
       choices = ["y1", "z2"]
       location_wraith = random.choice(choices)
    elif location_wraith == "z2":
       location_wraith = "z1"

# Ghost Activity 

def ghost_activity():
    global location_phantom
    global location_wraith
    global location_player
    global health_points
    global location_key
    global item_key
    if location_key == location_player:
        item_key = True
        location_key = "void"
        print ("You've found the key!\n")
    if location_phantom == location_player:    
        print("You're attacked by a phantom!\n")
        health_points = health_points - 1
    if location_wraith == location_player:    
        print("You're attacked by a wraith!\n")
        health_points = health_points - 1
    if location_phantom == location_wraith:    
        print("You hear a voice whisper in your ear, 'Speak the Beast's number beneath the steps...'\n")        
    phantom_movement()
    wraith_movement()   
    if location_phantom == location_player:    
        print("You're attacked by a phantom!\n")
        health_points = health_points - 1
    if location_wraith == location_player:    
        print("You're attacked by a wraith!\n")
        health_points = health_points - 1
    if location_phantom == location_wraith:    
        print("You hear a voice whisper in your ear, 'Speak the Beast's number beneath the steps...'\n")
                     
# Game Start

print("""

   ╔══════════════════════════════════════════╗
   ║  Welcome to...                           ║
   ║                                          ║
   ║ ┤SHITTY TEXT-BASED SURVIVAL HORROR GAME├ ║
   ║                                          ║
   ║                    ©1985 Father Heathen  ║
   ╚══════════════════════════════════════════╝
      
""")

input("Instructions: Type the numerical value that corrisponds with chosen direction, and then hit 'Enter'. ⏎\n")
def area_start():
    global location_key
    global location_
    choices = ["x2", "d1", "d3", "f3", "q3", "r2"]
    location_key = random.choice(choices)
    input("You enter the haunted house. The door slams shut and locks behind you. ⏎\n")
    area_c2()

# The First Floor

def area_a1():
    global location_player
    location_player = "a1"
    ghost_activity()
    health_display()
    print("[x][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Billiards Room\n")
    ghost_activity()
    travel_player = input("Actions: 1.) East 2.) South #\n")
    if travel_player == "1":
        area_a2()
    if travel_player == "2":
        area_b1()    
    else:
        area_a1()
    
def area_a2():
    global location_player
    location_player = "a2"
    ghost_activity()
    health_display()
    print("[ ][x][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Living Room\n")
    ghost_activity()
    travel_player = input("Actions: 1.) West 2.) South 3.) East #\n")
    if travel_player == "1":
        area_a1()
    if travel_player == "2":
        area_b2()
    if travel_player == "3":
        area_a3()
    else:
        area_a2()
    
def area_a3():
    global location_player
    global item_sigil
    location_player = "a3"
    ghost_activity()
    health_display()
    print("[ ][ ][x]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Alcove\n")
    if item_sigil == False:
        print ("You found a silver sigil.\n")
        item_sigil = True
    travel_player = input("Actions: 1.) West #\n")
    if travel_player == "1":
        area_a2()    
    else:
        area_a3()

def area_b1():
    global location_player
    location_player = "b1"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[x][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Stairwell (1st)\n")
    travel_player = input("Actions: 1.) East 2.) North. 3.) Up 4.) Down #\n")
    if travel_player == "1":
        area_b2()
    if travel_player == "2":
        area_a1()    
    if travel_player == "3":
        print("You ascend to the second floor.\n")
        area_e1()
    if travel_player == "4":
        print("You descend to the basement.\n")
        area_y1()
    else:
        area_b1()

def area_b2():
    global location_player
    location_player = "b2"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][x][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Parlor\n")
    travel_player = input("Actions: 1.) West. 2.) South 3.) East 4.) North #\n")
    if travel_player == "1":
        area_b1()
    if travel_player == "2":
        area_c2()
    if travel_player == "3":
        area_b3()
    if travel_player == "4":
        area_a2()
    else:
        area_b2()

def area_b3():
    global location_player
    location_player = "b3"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][x]")
    print("[ ][ ][ ]\n")
    print("Location: Dining Room\n")
    travel_player = input("Actions: 1.) West 2.) South #\n")
    if travel_player == "1":
        area_b2()
    if travel_player == "2":
        area_c3()
    else:
        area_b3()
    
def area_c1():
    global location_player
    global health_points
    global medical_1
    location_player = "c1"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[x][ ][ ]\n")
    print("Location: Washroom\n")
    if health_points < 5 and medical_1 == True:
        health_points = health_points + 1
        medical_1 = False
        print("You find and apply first-aid.\n")
    travel_player = input("Actions: 1.) East #\n")
    if travel_player == "1":
        area_c2()    
    else:
        area_c1()
        
def area_c2():
    global location_player
    global item_key
    location_player = "c2"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][x][ ]\n")
    print("Location: Foyer\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) East 4.) South #\n")
    if travel_player == "1":
        area_c1()
    if travel_player == "2":
        area_b2()
    if travel_player == "3":
        area_c3()
    if travel_player == "4":
        if item_key == False:
            print("The door is locked.\n")
            area_c2()
        if item_key == True:
            print("You've escaped!\n")
            game_over()
    else:
        area_c2()

def area_c3():
    global location_player
    location_player = "c3"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][x]\n")
    print("Location: Kitchen\n")
    travel_player = input("Actions: 1.) West 2.) North #\n")
    if travel_player == "1":
        area_c2()
    if travel_player == "2":
        area_b3()
    else:
        area_c3()

# The Basement

def area_x1():
    global location_player
    location_player = "x1"
    ghost_activity()
    health_display()
    print("[x][ ]")
    print("[ ][ ]")
    print("[ ]\n")
    print("Location: Wine Cellar\n")
    travel_player = input("Actions: 1.) South 2.) East #\n")
    if travel_player == "1":
        area_y1()
    if travel_player == "2":
        area_x2()    
    else:
        area_x1()

def area_x2():
    global location_player
    location_player = "x2"
    ghost_activity()
    health_display()
    print("[ ][x]")
    print("[ ][ ]")
    print("[ ]\n")
    print("Location: Storage Room\n")
    travel_player = input("Actions: 1.) West 2.) South #\n")
    if travel_player == "1":
        area_x1()
    if travel_player == "2":
        area_y2()    
    else:
        area_x2()

def area_y1():
    global location_player
    location_player = "y1"
    ghost_activity()
    health_display()
    print("[ ][ ]")
    print("[x][ ]")
    print("[ ]\n")
    print("Location: Stairwell (B)\n")
    travel_player = input("Actions: 1.) North 2.) East 3.) South 4.) Up #\n")
    if travel_player == "1":
        area_x1()
    if travel_player == "2":
        area_y2()
    if travel_player == "3":
        area_z1()
    if travel_player == "4":
        print("You ascend to the first floor.\n")
        area_b1()
    else:
        area_y1()

def area_y2():
    global location_player
    location_player = "y2"
    ghost_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][x]")
    print("[ ]\n")
    print("Location: Laundry Room\n")
    travel_player = input("Actions: 1.) North 2.) West \n#")
    if travel_player == "1":        
        area_x2()
    if travel_player == "2":
        area_y1()    
    else:
        area_y2()

def area_z1():
    global location_player
    location_player = "z1"
    ghost_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][ ]")
    print("[x]\n")
    print("Location: Spandrel\n")
    travel_player = input("Actions: 1.) North. #\n")
    if travel_player == "1":        
        area_y1()
    if travel_player == "666":
        area_z2()
    else:
        area_z1()

def area_z2():
    global location_player
    
    location_player = "z2"
    ghost_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][ ]")
    print("[ ] x \n")
    print("Location: Hidden Chamber\n")
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⠤⠀⠀⠤⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡆⠈⢠⣾⣷⡄⠁⢰⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠆⠈⠋⠀⠶⠄⠙⠋⠠⠶⠀⠙⠁⠰⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡉⠹⣿⠏⠉⢿⡿⠉⠉⢿⡿⠉⠹⣿⠏⢉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⠀⡿⠀⡇⠸⡇⢸⡇⢸⠇⢸⠀⢿⠀⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣦⣤⣼⣿⣤⣤⣾⣷⣤⣤⣿⣧⣤⣴⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⣤⣤⡤⠀⡀⠠⣤⣤⣤⣤⠄⢀⠀⢤⣤⣤⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⠋⣤⣾⣿⣷⡌⠛⠛⢡⣾⣿⣷⣤⠙⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        """)
    travel_player = input("Actions: 1.) West #\n")
    if travel_player == "1":        
        area_z1()
    else:
        area_z2()        

# The Second Floor

def area_d1():
    global location_player 
    location_player = "d1"
    ghost_activity()
    health_display()
    print("[x][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Guest Bedroom\n")
    travel_player = input("Actions: 1.) East #\n")
    if travel_player == "1":
        area_d2()
    else:
        area_d1()

def area_d2():
    global location_player 
    location_player = "d2"
    ghost_activity()
    health_display()
    print("[ ][x][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Lounge\n")
    travel_player = input("Actions: 1.) West 2.) East 3.) South #\n")
    if travel_player == "1":
        area_d1()
    if travel_player == "2":
        area_d3()
    if travel_player == "3":
        area_e2()        
    else:
        area_d2()

def area_d3():
    global location_player 
    location_player = "d3"
    ghost_activity()
    health_display()
    print("[ ][ ][x]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Master Bedroom\n")
    travel_player = input("Actions: 1.) West 2.) South #\n")
    if travel_player == "1":
        area_d2()
    if travel_player == "2":
        area_e3()    
    else:
        area_d3()

def area_e1():
    global location_player 
    location_player = "e1"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[x][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Stairwell (2nd)\n")
    travel_player = input("Actions: 1.) Up 2.) Down 3.) East #\n")
    if travel_player == "1":
        print("You ascend to the attic.\n")
        area_q1()
    if travel_player == "2":
        print("You descend to the first floor.\n")
        area_b1()
    if travel_player == "3":
        area_e2()        
    else:
        area_e1()

def area_e2():
    global location_player 
    location_player = "e2"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][x][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Hallway\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) South #\n")
    if travel_player == "1":
        area_e1()
    if travel_player == "2":
        area_d2()
    if travel_player == "3":
        area_f2()        
    else:
        area_e2()

def area_e3():
    global location_player
    global location_wraith
    global item_sigil 
    location_player = "e3"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][x]")
    print("[ ][ ][ ]\n")
    print("Location: Altar Room\n")
    if item_sigil == True:
        print ("You place the sigil upon the altar, banishing the wraith!\n")
        item_sigil = False
        location_wraith = "hell"
    travel_player = input("Actions: 1.) North #\n")
    if travel_player == "1":
        area_d3()
    else:
        area_e3()

def area_f1():
    global location_player
    global health_points
    global medical_2 
    location_player = "f1"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[x][ ][ ]\n")
    print("Location: Bathroom\n")
    if health_points < 5 and medical_2 == True:
        health_points = health_points + 1
        medical_2 = False
        print("You find and apply first-aid.\n")
    travel_player = input("Actions: 1.) East #\n")
    if travel_player == "1":
        area_f2()
    else:
        area_f1()

def area_f2():
    global location_player 
    location_player = "f2"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][x][ ]\n")
    print("Location: Corridor\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) East #\n")
    if travel_player == "1":
        area_f1()
    if travel_player == "2":
        area_e2()
    if travel_player == "3":
        area_f3()        
    else:
        area_f2()

def area_f3():
    global location_player 
    location_player = "f3"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][x]\n")
    print("Location: Study\n")
    travel_player = input("Actions: 1.) West#\n")
    if travel_player == "1":
        area_f2()
    else:
        area_f3()                                        

# The Attic

def area_q1():
    global location_player
    location_player = "q1"
    ghost_activity()
    health_display()
    print("[x][ ][ ]")
    print("   [ ]\n")
    print("Location: Stairwell (A)\n")
    travel_player = input("Actions: 1.) Down 2.) East #\n")
    if travel_player == "1":
        print("You descend to the second floor.\n")
        area_e1()
    if travel_player == "2":
        area_q2()    
    else:
        area_q1()

def area_q2():
    global location_player
    location_player = "q2"
    ghost_activity()
    health_display()
    print("[ ][x][ ]")
    print("   [ ]\n")
    print("Location: Landing\n")
    travel_player = input("Actions: 1.) West 2.) East 3.) South #\n")
    if travel_player == "1":
        area_q1()
    if travel_player == "2":
        area_q3()
    if travel_player == "3":
        area_r2()        
    else:
        area_q2()

def area_q3():
    global location_player
    location_player = "q3"
    ghost_activity()
    health_display()
    print("[ ][ ][x]")
    print("   [ ]\n")
    print("Location: Garret\n")
    travel_player = input("Actions: 1.) West #\n")
    if travel_player == "1":
        area_q2()
    else:
        area_q3()                        

def area_r2():
    global location_player
    location_player = "r2"
    ghost_activity()
    health_display()
    print("[ ][ ][ ]")
    print("   [x]\n")
    print("Location: Loft\n")
    travel_player = input("Actions: 1.) North #\n")
    if travel_player == "1":
        area_q2()
    else:
        area_r2()

area_start()