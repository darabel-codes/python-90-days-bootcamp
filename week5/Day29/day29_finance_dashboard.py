# This is a finance dashboard

import json
from datetime import datetime

print("===== PERSONAL FINANCE DASHBOARD =====")

# Load the data from the JSON file

def load_data():
    try:
        with open("finance.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Data file not found.")
        return []
    
    # save data to the JSON file
def save_data(data):
    with open("finance.json", "w") as file:
        json.dump(data, file, indent=4)


    
# Add expense

def add_expense(data):
    amount = float(input("Enter amount: "))
    category = input("Enter category(food, transport, e.t.c): ")
    note =input("Enter note: ")
    
    # ✅ Add date and time
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date_time
    }
    data.append(expense)
    save_data(data)
    print("Expense added successfully.")

# View expenses

def view_expenses(data):
    if not data:
        print("No expenses found.")
        return
    print("\n===== EXPENSES =====")
    for index, expense in enumerate(data, start=1):
        print(f"{index}. ₦{expense['amount']} | {expense['category']} | {expense['note']}\n")
        print(f"{expense['date']}")
        

# Show summary

def show_summary(data):
    if not data:
        print("No data to analyse.")
        return
    
    total = sum(expense['amount'] for expense in data)
    
    categories = {}
    
    for expense in data:
        cat = expense['category']
        categories[cat] = categories.get(cat, 0) + expense['amount']
    
    print("\n==== SUMMARY ====")
    print(f"Total Expenses: ₦{total}")
    

    print("\nBy Category:")
    for cat, amt in categories.items():
        print(f"{cat}: ₦{amt}")
    
    return total

# view balance


def view_balance(data):
    income = float(input("Enter income: "))
    if not data:
        print(f"No Balance to view")
        return
    else:
        total_expenses = show_summary(data)
        balance = income - total_expenses
        print(f"Your balance is: {balance}")
        
data = load_data()


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. View Balance")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense(data)

    elif choice == "2":
        view_expenses(data)

    elif choice == "3":
        show_summary(data)
    
    elif choice =="4":
        view_balance(data)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        