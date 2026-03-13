# This program combines functions, loops and conditionals to create a smart calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def power(x, y):
    return x ** y

def modulus(x, y):
    if y !=0:
        return x % y
    else: 
        return "Error: Modulus by zero is not allowed."

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."
    
print("===== WELCOME TO THE SMART CALCULATOR =====")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Power")
    print("5. Modulus")
    print("6. Divide")
    print("7. Exit")

    choice = input("Enter your choice from 1-7: ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    elif choice == '7':
        print(f"Exiting the smart calculator. Goodbye!")
        break
    else:
        print(f"Invalid input. Please enter a number between 1 and 7.")