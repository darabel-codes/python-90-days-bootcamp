import random

print("===== GUESS THE NUMBER GAME!=====")
secret_number = random.randint(1, 10)

guess = 0
attempts = 0


while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess > secret_number:
        print("Too High!")
       
    elif guess < secret_number:
        print("Too Low!")
       
    else:
        print("Congratulations! You guessed the number!")

if attempts <= 3:
    print(f"You guessed the number in {attempts} attempts! Great job!")
