import random

def guessing_game():
    # Set the range for the random number (1 to 10)
    lower_limit = 1
    upper_limit = 10

    # Generate a random number for the user to guess
    secret_number = random.randint(lower_limit, upper_limit)

    # Initialize the score
    score = 0

    print("Welcome to the Guessing Game! Try to guess the number between 1 and 10.")

    while True:
        # Get user input for the guess
        user_guess = input("Enter your guess (1-10) or 'exit' to end the game: ")

        # Check if the user wants to exit the game
        if user_guess.lower() == 'exit':
            print(f"Game over. Your final score is {score}. The correct number was {secret_number}.")
            break

        # Validate user input
        if not user_guess.isdigit() or not (1 <= int(user_guess) <= 10):
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        # Convert the user input to an integer
        user_guess = int(user_guess)

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number. Your score is {score}.")
            break
        else:
            # Provide a hint and update the score
            print("Incorrect guess. Try again!")
            score += 1

            # Provide an additional hint if the user's guess is close to the correct number
            if abs(secret_number - user_guess) <= 2:
                print("Hint: You're close to the correct number.")

if __name__ == "__main__":
    guessing_game()
