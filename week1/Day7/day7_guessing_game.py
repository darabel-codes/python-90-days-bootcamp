# import random

# print("----- NUMBER GUESSING GAME -----")
# print("Welcome to the Guessing Game. You have 3 attempts only")

# for i in range(3):
#     secret_number = random.randint(1,10)
#     guess = int(input("Guess a numer between 1 and 10: "))
    
#     if guess == 0:
#         print("Error! Try Again. Number has to be from 1 to 10.")
#     elif guess == secret_number:
#         print("🎉 Correct! You guessed the number.")
#     elif guess > secret_number:
#         print("Too High!")
#     elif guess < secret_number:
#         print("Too Low!")
#     else:
#         print("❌ Wrong guess.")
#         print(f"The correct number was: {secret_number}")
# print()
# print("GAME OVER! Try after 30 Minutes.")


import random

print("=================================")
print("     PYTHON NUMBER GUESSING GAME ")
print("=================================")
print()

print("I am thinking of a number between 1 and 10.")
print("You have 3 attempts to guess it.")
print()

secret_number = random.randint(1, 10)

attempts = 3

for attempt in range(1, attempts + 1):

    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed correctly.")
        break

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Too low!")

    if attempt == attempts:
        print()
        print("❌ Game Over!")
        print(f"The correct number was {secret_number}.")

        print("Thanks for playing! Goodbye!")