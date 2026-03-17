# This is a program to manage a contacts book using dictionaries in Python. The program allows you to add, view, and delete contacts from the book.

# Initialize an empty contacts book

contacts_book = {}

# Function to add a contact

def add_contact():
    name = input(f"Please enter the name of the contact: ")
    phone_number = int(input(f"Please enter the phone number of the contact: "))
    
    contacts_book[name] = phone_number
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts_book:
        print(f"No contacts found.")
    else:
        print(f"Contacts Book:")
        for name, phone_number in contacts_book.items():
            print(f"{name}: {phone_number}")

def delete_contact():
    name = input(f"Please enter the name of the contact to delete: ")
    if name in contacts_book:
        del contacts_book[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found in the contacts book.")

def search_contact():
    name = input(f"Please enter the name of the contact to search: ")
    if name in contacts_book:
        print(f"Contact found: {name}: {contacts_book[name]}")
    else:
        print(f"Contact {name} not found in the contacts book.")
    
while True:
    print(f"\nPlease choose an option:")
    print(f"1. Add a contact")
    print(f"2. View contacts")
    print(f"3. Delete a contact")
    print(f"4. Search Contact")
    print(f"5. Exit")
        
    choice = input("Enter your choice (1-5): ")
        
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print(f"Exiting the contacts book. Goodbye!")
        break
    else:
        print(f"Invalid choice. Please try again.")


        