import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

all_characters = letters + numbers + symbols

print("=====WELCOME TO THE PASSWORD GENERATOR!=====")

# password_length = int(input("Enter the desired password length: "))
letters_count = int(input("How many letters do you want in your password? "))
numbers_count = int(input("How many numbers do you want in your password? "))
symbols_count = int(input("How many symbols do you want in your password? "))

password_length = letters_count + numbers_count + symbols_count

# password = "".join(random.choice(all_characters) for _ in range(password_length))       
# print(f"Generated Password: {password}")



password = ""

for i in range(password_length):
    password += random.choice(all_characters)

print("Generated Password:", password)