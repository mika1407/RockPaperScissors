import random

player_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]
running = True

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        prYellow("It's a tie!")
        tie += 1
    elif player == "rock" and computer == "scissors":
        prGreen("You win!")
        player_wins += 1
    elif player == "paper" and computer == "rock":
        prGreen("You win!")
        player_wins += 1
    elif player == "scissors" and computer == "paper":
        prGreen("You win!")
        player_wins += 1
    else:
        prRed("You lose!")
        computer_wins += 1

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m  {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))

print("")
prGreen("Results:")
print("You won: ", player_wins, "times.")
print("The computer won: ", computer_wins, "times.")
print("Number of ties: ", tie)
prRed("****************")
prYellow("Thanks for playing!")