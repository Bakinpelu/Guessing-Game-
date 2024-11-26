# Beatrice Akinpelu
# 11/10/2024

# This program generates a random number and lets the user guess it.
# The program provides feedback on whether the guess is too high or too low and continues until the user chooses to stop.

import random 

def guessing_game():
    """Main function for the guessing game."""
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    print("Welcome to the Guessing Game!")
    
    while True:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))  # Get user's guess
            
            # Check if the user's guess matches the random number
            if user_guess == random_number:
                print("Congratulations! You guessed the correct number!")
                break
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print("Too low! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
def main():
    """Main program loop with an option to play again."""
    while True:
        guessing_game()  # Call the guessing game function
        play_again = input("Would you like to guess another number (Y/N)? ").strip().lower()
        
        if play_again == 'n':
            print("Thank you for playing! Goodbye!")
            break
        elif play_again == 'y':
            print("\nStarting a new game...\n")
        else:
            print("Invalid option! Exiting the game.")
            break

if __name__ == "__main__":
    main()
