import random

option = ["rock", "paper", "scissors"]

playing = True

while playing:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player   : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a Tie Game!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 YOU WIN!!")

    else:
        print("😢 YOU LOSE!!")

    choice = input("Play again? (y/n): ").lower()

    if choice != "y":
        playing = False

print("----------- THANKS FOR PLAYING -----------")