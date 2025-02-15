import random

def play_round(entities):
    """Simulates one round of rock-paper-scissors eliminations."""
    if len(entities) < 2:
        return entities  # End if one or no entities remain

    next_round = []
    random.shuffle(entities)  # Shuffle entities for random pairings

    # Pair entities and have them play
    for i in range(0, len(entities) - 1, 2):
        player1, player2 = entities[i], entities[i + 1]
        choice1, choice2 = random.choice(["rock", "paper", "scissors"]), random.choice(["rock", "paper", "scissors"])
        
        print(f"{player1} ({choice1}) vs {player2} ({choice2})")
        
        if choice1 == choice2:
            # If it's a tie, both survive this round
            print("It's a tie!")
            next_round.extend([player1, player2])
        elif (choice1 == "rock" and choice2 == "scissors") or \
             (choice1 == "paper" and choice2 == "rock") or \
             (choice1 == "scissors" and choice2 == "paper"):
            # Player 1 wins
            print(f"{player1} wins!")
            next_round.append(player1)
        else:
            # Player 2 wins
            print(f"{player2} wins!")
            next_round.append(player2)

    # If odd number of entities, last one gets a bye to next round
    if len(entities) % 2 == 1:
        print(f"{entities[-1]} gets a bye to the next round.")
        next_round.append(entities[-1])

    return next_round

def rock_paper_scissors_tournament():
    # Initialize entities
    entities = [f"Entity_{i+1}" for i in range(100)]
    round_number = 1

    while len(entities) > 1:
        print(f"\n--- Round {round_number} ---")
        entities = play_round(entities)
        print(f"Remaining entities: {len(entities)}")
        round_number += 1

    print(f"\nWinner: {entities[0]}!" if entities else "No winner.")

if __name__ == "__main__":
    rock_paper_scissors_tournament()
