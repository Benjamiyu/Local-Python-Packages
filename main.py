import random

#list of play options
play_options = ["rock", "paper", "scissors"]

R = play_options[0] #"rock" 
P = play_options[1] #"paper"
S = play_options[2] #"scissors"

print("Select play options.")
print(R)
print(P)
print(S)

# Take input from the player
user_play = input("Enter a choice (rock, paper, scissors): ")

# Random selections from the play options by Computer
computer_play = random.choice(play_options)


# Play options for the Player and Computer
print(f"\nPlayer ({user_play}) : CPU ({computer_play})\n")

if user_play == computer_play:
    print(f"Both players selected {user_play}. It's a tie!")
elif user_play == "rock":
    if computer_play == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif user_play == "paper":
    if computer_play == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif user_play == "scissors":
    if computer_play == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")




