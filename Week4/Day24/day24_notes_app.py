print("==== SIMPLE NOTES APP ====")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Clear Notes")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

                print("\n--- YOUR NOTES ---")
                print(notes)

        except FileNotFoundError:
            print("No notes found yet.")

    elif choice == "3":
        open("notes.txt", "w").close()
        print(f"Notes cleared successfully")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice.")