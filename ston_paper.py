import random

def get_user_choice():
    """
    Prompts the user to enter their choice and returns it.
    """
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    """
    Randomly selects and returns a choice for the computer.
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the user's choice and the computer's choice.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """The main function that runs the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    while play_again == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        while play_again not in ['yes', 'no']:
            print("Invalid input. Please type 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
    print("\nThank you for playing Rock-Paper-Scissors!")
# Start the game
play_game()
