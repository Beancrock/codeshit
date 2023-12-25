'''
╔╦╦╦╗
╚╣╨╠╝
╔╩╦╩╗
╠╦╬╦╣
╚╝╨╚╝
'''

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
x3y3 = " "
x3y2 = " "
x3y1 = "☺"

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
    print(x1y5 + x2y5 + x3y5 + x4y5 + x5y5)
    print(x1y4 + x2y4 + x3y4 + x4y4 + x5y4)
    print(x1y3 + x2y3 + x3y3 + x4y3 + x5y3)
    print(x1y2 + x2y2 + x3y2 + x4y2 + x5y2)
    print(x1y1 + x2y1 + x3y1 + x4y1 + x5y1)
    print()

def room_x1y5():
    global player_loc_x
    global player_loc_y
    global x1y5
    player_loc_x = 1
    player_loc_y = 5
    x1y5 = "☺"
    grid()
    x1y5 = "╔"
    while True:
        player_choice = input("(S)outh (E)ast :")
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
    player_loc_x = 2
    player_loc_y = 5
    x2y5 = "☺"
    grid()
    x2y5 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
        print()
        if player_choice == "s":
            room_x2y4()
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
    player_loc_x = 3
    player_loc_y = 5
    x3y5 = "☺"
    grid()
    x3y5 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
        print()
        if player_choice == "s":
            room_x3y4()
        if player_choice == "e":
            room_x4y5()
        if player_choice == "w":
            room_x2y5()        
        else:
            print("Invalid input..")
            print()

def room_x4y5():
    global player_loc_x
    global player_loc_y
    global x4y5
    player_loc_x = 4
    player_loc_y = 5
    x4y5 = "☺"
    grid()
    x4y5 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
        print()
        if player_choice == "s":
            room_x4y4()
        if player_choice == "e":
            room_x5y5()
        if player_choice == "w":
            room_x3y5()
        else:
            print("Invalid input..")
            print()

def room_x5y5():
    global player_loc_x
    global player_loc_y
    global x5y5
    player_loc_x = 5
    player_loc_y = 5
    x5y5 = "☺"
    grid()
    x5y5 = "╗"
    while True:
        player_choice = input("(S)outh (W)est: ")
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
    player_loc_x = 1
    player_loc_y = 4
    x1y4 = "☺"
    grid()
    x1y4 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :")
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
    player_loc_x = 2
    player_loc_y = 4
    x2y4 = "☺"
    grid()
    x2y4 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (W)est :")
        print()
        if player_choice == "n":
            room_x2y5()
        if player_choice == "s":
            room_x2y3()
        if player_choice == "w":
            room_x1y4()
        else:
            print("Invalid input..")
            print()

def room_x3y4():
    global player_loc_x
    global player_loc_y
    global x3y4
    player_loc_x = 3
    player_loc_y = 4
    x3y4 = "☺"
    grid()
    x3y4 = "╨"
    while True:
        player_choice = input("(N)orth :")
        print()
        if player_choice == "n":
            room_x3y5()
        else:
            print("Invalid input..")
            print()

def room_x4y4():
    global player_loc_x
    global player_loc_y
    global x4y4
    player_loc_x = 4
    player_loc_y = 4
    x4y4 = "☺"
    grid()
    x4y4 = "╠"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast :")
        print()
        if player_choice == "n":
            room_x4y5()
        if player_choice == "s":
            room_x4y3()
        if player_choice == "e":
            room_x5y4()
        else:
            print("Invalid input..")
            print()

def room_x5y4():
    global player_loc_x
    global player_loc_y
    global x5y4
    player_loc_x = 5
    player_loc_y = 4
    x5y4 = "☺"
    grid()
    x5y4 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :")
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
    player_loc_x = 1
    player_loc_y = 3
    x1y3 = "☺"
    grid()
    x1y3 = "╔"
    while True:
        player_choice = input("(S)outh (E)ast :")
        print()
        if player_choice == "s":
            room_x1y1()
        if player_choice == "e":
            room_x2y3()
        else:
            print("Invalid input..")
            print()

def room_x2y3():
    global player_loc_x
    global player_loc_y
    global x2y3
    player_loc_x = 2
    player_loc_y = 3
    x2y3 = "☺"
    grid()
    x2y3 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :")
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
    player_loc_x = 3
    player_loc_y = 3
    x3y3 = "☺"
    grid()
    x3y3 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
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
    player_loc_x = 4
    player_loc_y = 3
    x4y3 = "☺"
    grid()
    x4y3 = "╩"
    while True:
        player_choice = input("(N)orth (E)ast (W)est :")
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
    player_loc_x = 5
    player_loc_y = 3
    x5y3 = "☺"
    grid()
    x5y3 = "╗"
    while True:
        player_choice = input("(S)outh (W)est :")
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
    player_loc_x = 1
    player_loc_y = 2
    x1y2 = "☺"
    grid()
    x1y2 = "╠"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast: ")
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
    player_loc_x = 2
    player_loc_y = 2
    x2y2 = "☺"
    grid()
    x2y2 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
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
    player_loc_x = 3
    player_loc_y = 2
    x3y2 = "☺"
    grid()
    x3y2 = "╬"
    while  True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :")
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
    player_loc_x = 4
    player_loc_y = 2
    x4y2 = "☺"
    grid()
    x4y2 = "╦"
    while True:
        player_choice = input("(S)outh (E)ast (W)est :")
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
    player_loc_x = 5
    player_loc_y = 2
    x5y2 = "☺"
    grid()
    x5y2 = "╣"
    while True:
        player_choice = input("(N)orth (S)outh (E)ast :")
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
    player_loc_x = 1
    player_loc_y = 1
    x1y1 = "☺"
    grid()
    x1y1 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :")
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
    player_loc_x = 2
    player_loc_y = 1
    x2y1 = "☺"
    grid()
    x2y1 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :")
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
    player_loc_x = 3
    player_loc_y = 1
    x3y1 = "☺"
    grid()
    x3y1 = "╨"
    while True:
        player_choice = input("(N)orth :")
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
    player_loc_x = 4
    player_loc_y = 1
    x4y1 = "☺"
    grid()
    x4y1 = "╚"
    while True:
        player_choice = input("(N)orth (E)ast :")
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
    player_loc_x = 5
    player_loc_y = 1
    x5y1 = "☺"
    grid()
    x5y1 = "╝"
    while True:
        player_choice = input("(N)orth (W)est :")
        print()
        if player_choice == "n":
            room_x5y2()
        if player_choice == "w":
            room_x4y1()
        else:
            print("Invalid input..")
            print()            
           
room_x3y1()