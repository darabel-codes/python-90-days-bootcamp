import math_utils

print("===== SIMPLE CALCULATOR USING MODULE =====")

while True:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        result = math_utils.add(num1, num2)
        print(f"The result of addition is: {result}")
        
    elif choice == "2":
        result = math_utils.subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
        
    elif choice == "3":
        result = math_utils.multiply(num1, num2)
        print(f"The result of multiplication is: {result}")
        
    elif choice == "4":
        result = math_utils.divide(num1, num2)
        print(f"The result of division is: {result}")
        
    elif choice == "5":
        result = math_utils.power(num1, num2)
        print(f"The result of power is: {result}")
        
    elif choice == "6":
        result = math_utils.modulus(num1, num2)
        print(f"The result of modulus is: {result}")
    
    elif choice == "7":
        print("Exiting the calculator. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

