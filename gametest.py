# Create a 2D map as a list of lists
map_size = 5
map_app = [[" " for _ in range(map_size)] for _ in range(map_size)]

# Function to display the map
def map_display():
    for row in map_app:
        print("[" + "][".join(row) + "]")

# Function to update the map based on player actions
def update_map(x, y, new_value):
    map_app[y - 1][x - 1] = new_value

# Temporary loop for testing purposes
def game_loop():
    while True:
        map_display()
        command_menu()
        user_input = input("Enter a command: ")
        if user_input == "exit":
            break
        # Handle user commands and update the map accordingly
        # For example, if the user moves north, update_map(x, y, "X")

# Command menu
def command_menu():
    print("Commands: North (n), South (s), East (e), West (w), Exit (exit)")

# Initiate the game
game_loop()