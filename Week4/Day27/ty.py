import json

print("==== STUDENT MANAGER (JSON) ====")


# Load students from JSON
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save students to JSON
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Choose option: ")

    # ➕ Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        save_students(students)
        print("Student saved!")

    # 📋 View Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- STUDENTS ---")
            for i, s in enumerate(students, start=1):
                print(f"{i}. {s['name']} | {s['age']} | {s['course']}")

    # ❌ Delete Student
    elif choice == "3":
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s['name']}")

        try:
            num = int(input("Enter number to delete: "))
            if 1 <= num <= len(students):
                removed = students.pop(num - 1)
                save_students(students)
                print(f"Deleted: {removed['name']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    # 🚪 Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")