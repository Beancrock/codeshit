# dictionaries

x1y1z1 = {
    "x_column": 1,
    "y_row": 1,
    "z_level": 1,
    "map_app": " "
}
x2y1z1 = {
    "x_column": 2,
    "y_row": 1,
    "z_level": 1,
    "map_app": " "
}
x3y1z1 = {
    "x_column": 3,
    "y_row": 1,
    "z_level": 1,
    "map_app": " "
}
x4y1z1 = {
    "x_column": 4,
    "y_row": 1,
    "z_level": 1,
    "map_app": " "
}
x5y1z1 = {
    "x_column": 5,
    "y_row": 1,
    "z_level": 1,
    "map_app": " "
}

x1y2z1 = {
    "x_column": 1,
    "y_row": 2,
    "z_level": 1,
    "map_app": " "
}
x2y2z1 = {
    "x_column": 2,
    "y_row": 2,
    "z_level": 1,
    "map_app": " "
}
x3y2z1 = {
    "x_column": 3,
    "y_row": 2,
    "z_level": 1,
    "map_app": " "
}
x4y2z1 = {
    "x_column": 4,
    "y_row": 2,
    "z_level": 1,
    "map_app": " "
}
x5y2z1 = {
    "x_column": 5,
    "y_row": 2,
    "z_level": 1,
    "map_app": " "
}

x1y3z1 = {
    "x_column": 1,
    "y_row": 3,
    "z_level": 1,
    "map_app": " "
}
x2y3z1 = {
    "x_column": 2,
    "y_row": 3,
    "z_level": 1,
    "map_app": " "
}
x3y3z1 = {
    "x_column": 3,
    "y_row": 3,
    "z_level": 1,
    "map_app": " "
}
x4y3z1 = {
    "x_column": 4,
    "y_row": 3,
    "z_level": 1,
    "map_app": " "
}
x5y3z1 = {
    "x_column": 5,
    "y_row": 3,
    "z_level": 1,
    "map_app": " "
}

x1y4z1 = {
    "x_column": 1,
    "y_row": 4,
    "z_level": 1,
    "map_app": " "
}
x2y4z1 = {
    "x_column": 2,
    "y_row": 4,
    "z_level": 1,
    "map_app": " "
}
x3y4z1 = {
    "x_column": 3,
    "y_row": 4,
    "z_level": 1,
    "map_app": " "
}
x4y4z1 = {
    "x_column": 4,
    "y_row": 4,
    "z_level": 1,
    "map_app": " "
}
x5y4z1 = {
    "x_column": 5,
    "y_row": 4,
    "z_level": 1,
    "map_app": " "
}

x1y5z1 = {
    "x_column": 1,
    "y_row": 5,
    "z_level": 1,
    "map_app": " "
}
x2y5z1 = {
    "x_column": 2,
    "y_row": 5,
    "z_level": 1,
    "map_app": " "
}
x3y5z1 = {
    "x_column": 3,
    "y_row": 5,
    "z_level": 1,
    "map_app": " "
}
x4y5z1 = {
    "x_column": 4,
    "y_row": 5,
    "z_level": 1,
    "map_app": " "
}
x5y5z1 = {
    "x_column": 5,
    "y_row": 5,
    "z_level": 1,
    "map_app": " "
}

# map display

def map_display():
    print("[" + x1y1z1["map_app"] + "][" + x2y1z1["map_app"] + "][" + x3y1z1["map_app"] + "][" + x4y1z1["map_app"] + "][" + x5y1z1["map_app"] + "]")
    print("[" + x1y2z1["map_app"] + "][" + x2y2z1["map_app"] + "][" + x3y2z1["map_app"] + "][" + x4y2z1["map_app"] + "][" + x5y2z1["map_app"] + "]")
    print("[" + x1y3z1["map_app"] + "][" + x2y3z1["map_app"] + "][" + x3y3z1["map_app"] + "][" + x4y3z1["map_app"] + "][" + x5y3z1["map_app"] + "]")
    print("[" + x1y4z1["map_app"] + "][" + x2y4z1["map_app"] + "][" + x3y4z1["map_app"] + "][" + x4y4z1["map_app"] + "][" + x5y4z1["map_app"] + "]")
    print("[" + x1y5z1["map_app"] + "][" + x2y5z1["map_app"] + "][" + x3y5z1["map_app"] + "][" + x4y5z1["map_app"] + "][" + x5y5z1["map_app"] + "]")
    print()

# command menu

def command_menu():
    print("North: (1) South: (2) East: (3) West: (4) Search: (5) Item: (6)")
    print()

# temp loop for testing purposes    

def game_loop():
    pickle = True
    while pickle == True:
        map_display()
        command_menu()
        break

# intitate game

game_loop()