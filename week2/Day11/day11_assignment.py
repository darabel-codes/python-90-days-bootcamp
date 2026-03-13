# This code is to generate a simple calculator using functions
def add(a, b):
    return a + b
    
def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

print("===== SMART CALCULATOR =====")
print("Select operation:")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {substract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input. Please select a valid operation.")


print(f"\nThank you for using the Simple Calculator!")


