import random

choices = ['rock', 'paper', 'scissors']

# Get user input and convert to lowercase to prevent case-sensitivity errors
player_input = input("Let's play ROCK PAPER SCISSORS!\nrock....paper.....scissorsss\n\nEnter your choice: ").lower()

computer_choice = random.choice(choices)

print(f"\nYou chose {player_input}.")
print(f"I chose {computer_choice}.\n")

# 1. First, check if the input is even valid
if player_input not in choices:
    print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

# 2. Check for a tie
elif player_input == computer_choice:
    print(f"{player_input.upper()}!!")
    print("It's a tie!")

# 3. Check for player win conditions
elif (player_input == "rock" and computer_choice == "scissors") or \
     (player_input == "paper" and computer_choice == "rock") or \
     (player_input == "scissors" and computer_choice == "paper"):
    print(f"{player_input.upper()}!!")
    print("You win Dude😒")

# 4. If it's not a tie and you didn't win, I must have won
else:
    print(f"{player_input.upper()}!!")
    print("I win 🥳🍾.....better luck next time😁😁")