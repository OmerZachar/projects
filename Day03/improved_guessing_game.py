import random

def play_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Guess the number (between 1 and 20), or enter 'x' to exit, 'n' to restart, or 's' to show the number: ")

        if guess.isdigit():
            guess = int(guess)
        elif guess.lower() == 'x':
            print("Exiting game.")
            return 'exit'
        elif guess.lower() == 'n':
            print("Restarting game.")
            return 'restart'
        elif guess.lower() == 's':
            print(f"The secret number was: {secret_number}")
            return 'show'
        else:
            print("Please enter a valid number or 'x', 'n', or 's' as specified.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return 'success'

def main():
    while True:
        result = play_game()
        if result == 'exit':
            break
        elif result == 'restart':
            continue
        elif result == 'show':
            continue
        elif result == 'success':
            choice = input("Do you want to play again? (yes/no): ")
            if choice.lower() != 'yes':
                print("Thanks for playing!")
                break


main()
