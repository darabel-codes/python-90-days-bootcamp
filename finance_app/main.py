import finance_utils

print("==== SMART FINANCE MANAGER ====")

data = finance_utils.load_data()

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Show Summary")
    print("5. Search Expense")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        finance_utils.add_income(data)

    elif choice == "2":
        finance_utils.add_expense(data)

    elif choice == "3":
        finance_utils.view_transactions(data)

    elif choice == "4":
        finance_utils.show_summary(data)

    elif choice == "5":
        finance_utils.search_expense(data)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")