import json

DATA_FILE = "data.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {"income": 0, "expenses": []}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_income(data):
    amount = float(input("Enter income amount: "))
    data["income"] += amount
    save_data(data)
    print("Income added!")


def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Category: ")
    note = input("Note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    data["expenses"].append(expense)
    save_data(data)
    print("Expense added!")


def show_summary(data):
    total_expense = sum(exp["amount"] for exp in data["expenses"])
    balance = data["income"] - total_expense

    print("\n--- SUMMARY ---")
    print(f"Total Income: ₦{data['income']}")
    print(f"Total Expenses: ₦{total_expense}")
    print(f"Balance: ₦{balance}")

    categories = {}
    for exp in data["expenses"]:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    print("\nBy Category:")
    for cat, amt in categories.items():
        print(f"{cat}: ₦{amt}")


def view_transactions(data):
    print("\n--- TRANSACTIONS ---")
    for i, exp in enumerate(data["expenses"], start=1):
        print(f"{i}. ₦{exp['amount']} | {exp['category']} | {exp['note']}")


def search_expense(data):
    keyword = input("Enter keyword: ").lower()

    print("\n--- SEARCH RESULTS ---")
    found = False

    for exp in data["expenses"]:
        if keyword in exp["category"].lower() or keyword in exp["note"].lower():
            print(f"₦{exp['amount']} | {exp['category']} | {exp['note']}")
            found = True

    if not found:
        print("No match found.")