#Rock, Paper, Scissors Project for ST1
import random
while True:
    human_action = input("Please select a single option from (Rock, Paper or Scissors):  ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {human_action}, Leeroy chose {computer_action}.\n")

    if human_action == computer_action:
        print(f"Both players selected {human_action}. It's a tie!")
    elif human_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif human_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif human_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break