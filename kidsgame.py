import random

choices = ["paper", "stone", "scissors"]

def get_user_choice():
    user_choice = input("Enter your choice (paper, stone, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter again (paper, stone, scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
