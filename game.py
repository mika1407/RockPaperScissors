import random

player_wins = 0
computer_wins = 0
tie = 0

while True:
  choices = ["rock","paper","scissors"]

  computer = random.choice(choices)
  player = None

  while player not in choices:
    player = input("rock, paper or scissors?: ").lower()

  if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")
    tie += 1
  elif player == "rock":
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You lose!")
      computer_wins += 1
    if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
      player_wins += 1
  elif player == "scissors":
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You lose!")
      computer_wins += 1
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
      player_wins += 1
  elif player == "paper":
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
      player_wins += 1
    if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You lose!")
      computer_wins += 1

  play_again = input("Play again? (yes/no): ").lower()

  if play_again != "yes":
      break

print("")
print("Results:")
print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Number of ties: ", tie)
print("****************")
print("Bye bye!")