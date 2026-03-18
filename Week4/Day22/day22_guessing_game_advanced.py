import random

print ("===== GUESSING GAME (ADVANCED) =====")

# Generate a random number between 1 and 100

secret_number = random.randint(1, 100)

# Choose difficulty level
def play_game():
    secret_number = random.randint(1, 100)
    print("\nChoose a difficulty level: ")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    choice = input("Select an option: ")

    if choice == "1":
        attempts = 10
    elif choice == "2":
        attempts = 5
    elif choice == "3":
        attempts = 3
    else:
        print("Invalid choice! Defaulting to Hard level.")
        attempts = 5

    # Game loop

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        
        guess = input("Enter your guess (1-100): ")
        
        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.")
            continue
        
        guess = int(guess)
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts -= 1

    # End of game

    if attempts == 0:
        print(f"Game over! The secret number was: {secret_number}")
play_game()
    
# Replay option
replay = input("\nDo you want to play again? (yes/no): ")
if replay.lower() == "yes":
    # Restart the game
    print("\nRestarting the game...")
    # You can call the main game function here if you encapsulate the game logic in a function
    play_game()
else:
    print("Thank you for playing! Goodbye!")
