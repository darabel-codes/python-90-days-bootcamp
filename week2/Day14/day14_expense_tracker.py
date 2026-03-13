expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nRecorded Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Amount: ${expense['amount']:.2f}, Category: {expense['category']}")

def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

while True:
    print("\n==== EXPENSE TRACKER MENU ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    print("5. Clear All Expenses")
    print("6. Average Expenses")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(amount, category)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Goodbye!")
       
    elif choice == "5":
        expenses.clear()
        print("All expenses cleared.")
    
    elif choice == "6":
        if expenses:
            average = sum(expense['amount'] for expense in expenses) / len(expenses)
            print(f"\nAverage Expense: ${average:.2f}")
        else:
            print("No expenses to calculate average.")
        break

    else:
        print("Invalid option. Try again.")