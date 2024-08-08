# imported shit

import random

# variables and values

global x
global y
global time
global clock
global location

grid = [
        ["≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈"],
        ["≈", " ", " ", " ", "⌂", " ", " ", "۩", "≈", "≈", "▲", " ", " ", " ", "†", "▲", "↑", "≈"],
        ["≈", "▲", "∆", " ", " ", " ", " ", " ", "≈", "≈", "▲", "∆", " ", " ", " ", " ", " ", "≈"],
        ["≈", "▲", " ", " ", " ", " ", "▲", "▲", "≈", "≈", "⌂", " ", " ", " ", " ", "↑", "↑", "≈"],
        ["≈", "▲", "☼", " ", " ", " ", "▲", "▲", "≈", "≈", " ", " ", " ", "⌂", " ", " ", "۩", "≈"],
        ["≈", "▲", " ", " ", " ", "†", "▲", "↑", "≈", "≈", " ", " ", " ", "†", " ", "⌂", "↑", "≈"],
        ["≈", " ", " ", " ", "†", " ", "⌂", "↑", "≈", "≈", "▲", "☼", " ", " ", " ", "▲", "▲", "≈"],
        ["≈", "⌂", " ", " ", " ", " ", "↑", "↑", "≈", "≈", "▲", " ", " ", " ", " ", "▲", "▲", "≈"],
        ["≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈"],
        ["≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈"],
        ["≈", " ", " ", " ", "⌂", " ", " ", "۩", "≈", "≈", "▲", " ", " ", " ", "†", "▲", "↑", "≈"],
        ["≈", "▲", "∆", " ", " ", " ", " ", " ", "≈", "≈", "▲", "∆", " ", " ", " ", " ", " ", "≈"],
        ["≈", "▲", " ", " ", " ", " ", "▲", "▲", "≈", "≈", "⌂", " ", " ", " ", " ", "↑", "↑", "≈"],
        ["≈", "▲", "☼", " ", " ", " ", "▲", "▲", "≈", "≈", " ", " ", " ", "⌂", " ", " ", "۩", "≈"],
        ["≈", "▲", " ", " ", " ", "†", "▲", "↑", "≈", "≈", " ", " ", " ", "†", " ", "⌂", "↑", "≈"],
        ["≈", " ", " ", " ", "†", " ", "⌂", "↑", "≈", "≈", "▲", "☼", " ", " ", " ", "▲", "▲", "≈"],
        ["≈", "⌂", " ", " ", " ", " ", "↑", "↑", "≈", "≈", "▲", " ", " ", " ", " ", "▲", "▲", "≈"],
        ["≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈", "≈"]  
    ]

x = 5
y = 5
time = 1
clock = "Day"
location = " "

# game loop

def gameloop():
    loc()
    command()
    gameloop()

# game "time"

def gametime():
    global time
    global clock
    time = time + 1
    if time == 13:
        time = 1
        input("What a terrible day to have a curse. lmao. ")
    if time < 7:
        clock = "Day"
    if time > 6:
        clock = "Night"    
    if time == 7:
        input("What a horrible night to have a curse. lol.")
    print()

# location

def loc():
    global clock
    global location
    if grid[y][x] == " ":
        location = "Plains"
    elif grid[y][x] == "↑":
        location = "Forest"
    elif grid[y][x] == "▲":
        location = "Mountains"
    elif grid[y][x] == "≈":
        location = "Ocean"            
    elif grid[y][x] == "⌂":
        location = "Village"
    else:
        location = "???"        

#player actions and choices

def command():
    global clock
    global location
    print( "Time: " + clock + " Location: " + location)
    print()    
    print("[" + grid[y-2][x-2] + "][" + grid[y-2][x-1] + "][" + grid[y-2][x] + "][" + grid[y-2][x+1] + "][" + grid[y-2][x+2] + "]")
    print("[" + grid[y-1][x-2] + "][" + grid[y-1][x-1] + "][" + grid[y-1][x] + "][" + grid[y-1][x+1] + "][" +  grid[y-1][x+2] + "]")
    print("[" + grid[y][x-2] + "][" + grid[y][x-1] + "][☻][" + grid[y][x+1] + "][" + grid[y][x+2] + "]")
    print("[" + grid[y+1][x-2] + "][" + grid[y+1][x-1] + "][" + grid[y+1][x] + "][" + grid[y+1][x+1] + "][" +  grid[y+1][x+2] + "]")
    print("[" + grid[y+2][x-2] + "][" + grid[y+2][x-1] + "][" + grid[y+2][x] + "][" + grid[y+2][x+1] + "][" +  grid[y+2][x+2] + "]")
    
    print("Menu:")
    print()
    print("1. Move")
    print("2. Search")
    print("3. Map")
    print("4. Inventory")
    print("5. Stats")
    print()
    while True:
        player_choice = input("Enter the number that corresponds with your selection:")
        print()
        if player_choice == "1":
            movement()
            break
        if player_choice == "2":
            search()
            break 
        if player_choice == "3":
            map()
            break
        if player_choice == "4":
            inventory()
            break
        if player_choice == "5":
            character_stats()
            break
        else:
            print("Invalid input..")
            print()
    
# map display

def map():    
    
    print("Map:")
    for row in grid:
        print(row)
    print()
   
# player movement

def movement():
    global x
    global y
    while True:
        player_choice = input("(N)orth (S)outh (E)ast (W)est :").lower()
        print()
        if player_choice == "n":
            y = y - 1
            print("You travel north.")
            print()
            break
        if player_choice == "s":
            y = y + 1
            print("You travel south.")
            print()
            break
        if player_choice == "e":
            x = x + 1
            print("You travel east.")
            print()
            break 
        if player_choice == "w":
            x = x - 1
            print("You travel west.")
            print()
            break     
        else:
            print("Invalid input..")
            print()
    gametime()
    encounter()        

# player stats

def character_stats():
    input("You're a god in a dead, empty world.")
    print()

# player inventory

def inventory():
    input("Ya ain't got shit.")
    print()

# battle encounter randomization

def encounter():
    #print("A tapdancing hobgoblin appears...but he trips over his own feet and falls, breaking his own neck.")
    print()

# player area search (treasure or encounter, lore details?)

def search():
    input("You found an epic sword, but it turned into dust upon touch.")
    print()
    gametime()

gameloop()

