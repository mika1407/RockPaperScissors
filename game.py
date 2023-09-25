import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
  player = input("rock, paper or scissors?: ")

print("computer: ", computer)
print("player: ", player)