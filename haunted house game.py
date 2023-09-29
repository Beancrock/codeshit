import random

location_phantom = "a3"
turn_count = 0
health_points = 3

# Health Display

def health_display():
    global health_points
    if health_points == 3:
        print("\u2665\u2665\u2665")
    if health_points == 2:
        print("\u2665\u2665")
    if health_points == 1:
        print("\u2665")
    if health_points == 0:
        print("*dead*\n")
        game_over()
        
# Game Over

def game_over():
    print("-Game Over-\n")
    input()
    exit()

# Phantom Activity

def phantom_activity():
    global turn_count
    global location_phantom
    global location_player
    global health_points
    if location_phantom == location_player:    
        print("You're attacked by a phantom!\n")
        health_points = health_points - 1
    turn_count = turn_count + 1
    if turn_count == 1:
        location_phantom = "a3"
    if turn_count == 2:
        location_phantom = "a2"
    if turn_count == 3:
        location_phantom = "a1"
    if turn_count == 4:
        location_phantom = "b1"
    if turn_count == 5:
        location_phantom = "b2"    
    if turn_count == 6:
        location_phantom = "b3"
    if turn_count == 7:
        location_phantom = "c3"
    if turn_count == 8:
        location_phantom = "c2"
    if turn_count == 9:
        location_phantom = "c1"
    if turn_count == 10:
        location_phantom = "c2"
    if turn_count == 11:
        location_phantom = "c3"
    if turn_count == 12:
        location_phantom = "b3"
    if turn_count == 13:
        location_phantom = "b2"
    if turn_count == 14:
        location_phantom = "b1"    
    if turn_count == 15:
        location_phantom = "a1"
    if turn_count == 16:
        location_phantom = "a2"
    if turn_count >= 17:
        location_phantom = "a3"
        turn_count = 0
    if location_phantom == location_player:    
        print("You're attacked by a phantom!\n")
        health_points = health_points - 1
    
# Game Start

def area_start():
    print("You enter the haunted house.\n")
    area_c2()

# The First Floor

def area_a1():
    global location_player
    location_player = "a1"
    phantom_activity()
    health_display()
    print("[x][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Billiards Room\n")
    phantom_activity()
    travel_player = input("Actions: 1.) South 2.) East \n")
    if travel_player == "1":
        area_b1()
    if travel_player == "2":
        area_a2()
    else:
        area_a1()
    
def area_a2():
    global location_player
    location_player = "a2"
    phantom_activity()
    health_display()
    print("[ ][x][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Living Room\n")
    phantom_activity()
    travel_player = input("Actions: 1.) West 2.) South 3.) East \n")
    if travel_player == "1":
        area_a1()
    if travel_player == "2":
        area_b2()
    if travel_player == "3":
        print("The door is locked.\n")
        area_a2()
    else:
        area_a2()
    
def area_a3():
    global location_player
    location_player = "a3"
    phantom_activity()
    health_display()
    print("[ ][ ][x]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Study\n")
    travel_player = input("Actions: 1.) West \n")
    if travel_player == "1":
        area_a2()    
    else:
        area_a3()

def area_b1():
    global location_player
    location_player = "b1"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[x][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Stairwell\n")
    travel_player = input("Actions: 1.) North 2.) East 3.) Up 4.) Down \n")
    if travel_player == "1":
        area_a1()
    if travel_player == "2":
        area_b2()
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
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][x][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Parlor\n")
    travel_player = input("Actions: 1.) West. 2.) South 3.) East 4.) North \n")
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
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][x]")
    print("[ ][ ][ ]\n")
    print("Location: Dining Room\n")
    travel_player = input("Actions: 1.) West 2.) South \n")
    if travel_player == "1":
        area_b2()
    if travel_player == "2":
        area_c3()
    else:
        area_b3()
    
def area_c1():
    global location_player
    location_player = "c1"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[x][ ][ ]\n")
    print("Location: Washroom\n")
    travel_player = input("Actions: 1.) East \n")
    if travel_player == "1":
        area_c2()    
    else:
        area_c1()
        
def area_c2():
    global location_player
    location_player = "c2"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][x][ ]\n")
    print("Location: Foyer\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) East \n")
    if travel_player == "1":
        print("The door is locked.\n")
        area_c2()
    if travel_player == "2":
        area_b2()
    if travel_player == "3":
        area_c3()    
    else:
        area_c2()

def area_c3():
    global location_player
    location_player = "c3"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][x]\n")
    print("Location: Kitchen\n")
    travel_player = input("Actions: 1.) West 2.) Take North \n")
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
    phantom_activity()
    health_display()
    print("[x][ ]")
    print("[ ][ ]")
    print("[ ]\n")
    print("Location: Wine Cellar\n")
    travel_player = input("Actions: 1.) South 2.) East \n")
    if travel_player == "1":
        area_y1()
    if travel_player == "2":
        area_x2()    
    else:
        area_x1()

def area_x2():
    global location_player
    location_player = "x2"
    phantom_activity()
    health_display()
    print("[ ][x]")
    print("[ ][ ]")
    print("[ ]\n")
    print("Location: Storage Room\n")
    travel_player = input("Actions: 1.) West 2.) South \n")
    if travel_player == "1":
        area_x1()
    if travel_player == "2":
        area_y2()    
    else:
        area_x2()

def area_y1():
    global location_player
    location_player = "y1"
    phantom_activity()
    health_display()
    print("[ ][ ]")
    print("[x][ ]")
    print("[ ]\n")
    print("Location: Landing\n")
    travel_player = input("Actions: 1.) North 2.) East 3.) South 4.) Up \n")
    if travel_player == "1":
        area_x1()
    if travel_player == "2":
        area_y2()
    if travel_player == "3":
        print("The door is locked.")
        area_y1()
    if travel_player == "4":
        print("You ascend to the first floor.\n")
        area_b1()
    else:
        area_y1()

def area_y2():
    global location_player
    location_player = "y2"
    phantom_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][x]")
    print("[ ]\n")
    print("Location: Laundry Room\n")
    travel_player = input("Actions: 1.) North 2.) West \n")
    if travel_player == "1":        
        area_x2()
    if travel_player == "2":
        area_y1()    
    else:
        area_y2()

def area_z1():
    global location_player
    location_player = "z1"
    phantom_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][ ]")
    print("[x]\n")
    print("Location: Spandrel\n")
    travel_player = input("Actions: 1.) North. \n")
    if travel_player == "1":        
        area_y1()
    else:
        area_z1()

def area_z2():
    global location_player
    location_player = "z2"
    phantom_activity()
    health_display()
    print("[ ][ ]")
    print("[ ][ ]")
    print("[ ] x \n")
    print("Location: Hidden Chamber\n")
    travel_player = input("Actions: 1.) West \n")
    if travel_player == "1":        
        area_z1()
    else:
        area_z2()        

# The Second Floor

def area_d1():
    global location_player 
    location_player = "d1"
    phantom_activity()
    health_display()
    print("[x][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Guest Bedroom\n")
    travel_player = input("Actions: 1.) East \n")
    if travel_player == "1":
        area_d2()
    else:
        area_d1()

def area_d2():
    global location_player 
    location_player = "d2"
    phantom_activity()
    health_display()
    print("[ ][x][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Lounge\n")
    travel_player = input("Actions: 1.) West 2.) East 3.) South \n")
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
    phantom_activity()
    health_display()
    print("[ ][ ][x]")
    print("[ ][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Master Bedroom\n")
    travel_player = input("Actions: 1.) West 2.) South \n")
    if travel_player == "1":
        area_d2()
    if travel_player == "2":
        area_e3()    
    else:
        area_d3()

def area_e1():
    global location_player 
    location_player = "e1"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[x][ ][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Stairwell\n")
    travel_player = input("Actions: 1.) Up 2.) Down 3.) East \n")
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
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][x][ ]")
    print("[ ][ ][ ]\n")
    print("Location: Hallway\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) South \n")
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
    location_player = "e3"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][x]")
    print("[ ][ ][ ]\n")
    print("Location: Alcove\n")
    travel_player = input("Actions: 1.) North \n")
    if travel_player == "1":
        area_d3()
    else:
        area_e3()

def area_f1():
    global location_player 
    location_player = "f1"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[x][ ][ ]\n")
    print("Location: Bathroom\n")
    travel_player = input("Actions: 1.) East \n")
    if travel_player == "1":
        area_f2()
    else:
        area_f1()

def area_f2():
    global location_player 
    location_player = "f2"
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][x][ ]\n")
    print("Location: Corridor\n")
    travel_player = input("Actions: 1.) West 2.) North 3.) East \n")
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
    phantom_activity()
    health_display()
    print("[ ][ ][ ]")
    print("[ ][ ][ ]")
    print("[ ][ ][x]\n")
    print("Location: \n")
    travel_player = input("Actions: 1.) West\n")
    if travel_player == "1":
        area_f2()
    else:
        area_f3()                                        

# The Attic

def area_q1():
    global location_player
    location_player = "q1"
    phantom_activity()
    health_display()
    print("[x][ ][ ]\n")
    print("Location: Landing\n")
    travel_player = input("Actions: 1.) Down 2.) East \n")
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
    phantom_activity()
    health_display()
    print("[ ][x][ ]\n")
    print("Location: Loft\n")
    travel_player = input("Actions: 1.) West 2.) East \n")
    if travel_player == "1":
        area_q1()
    if travel_player == "2":
        print("The door is locked.")
        area_q2()    
    else:
        area_q2()

def area_q3():
    global location_player
    location_player = "q3"
    phantom_activity()
    health_display()
    print("[ ][ ][x]\n")
    print("Location: Garret\n")
    travel_player = input("Actions: 1.) West \n")
    if travel_player == "1":
        area_q2()
    else:
        area_q3()                        
    
area_start()