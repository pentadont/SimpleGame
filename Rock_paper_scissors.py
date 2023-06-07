rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper, or [s]cissors: ")

# Map player's input to their chosen move
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    print("Invalid input. Please choose either 'r', 'p', or 's'.")
    exit()

# Randomly generate computer's move
import random
moves = [rock, paper, scissors]
computer_move = random.choice(moves)

print("Player chooses:", player_move)
print("Computer chooses:", computer_move)

# Determine the winner
if player_move == computer_move:
    print("It's a tie!")
elif (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("Player wins!")
else:
    print("Computer wins!")
