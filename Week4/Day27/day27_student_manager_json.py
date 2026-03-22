import json

print("===== STUDENT MANAGER (JSON) =====")

# -------------------------------
# LOAD STUDENTS (SAFE VERSION)
# -------------------------------
def load_students():
    try:
        with open("students.json", "r") as file:
            data = file.read().strip()

            if not data:
                return []

            result = json.loads(data)

            # 🔥 Ensure it's always a list
            if isinstance(result, dict):
                return [result]

            return result

    except (FileNotFoundError, json.JSONDecodeError):
        return []

# -------------------------------
# SAVE STUDENTS
# -------------------------------
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# -------------------------------
# START PROGRAM
# -------------------------------
students = load_students()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # -------------------------------
    # ADD STUDENT
    # -------------------------------
    if choice == "1":
        name = input("Enter name: ")

        try:
            age = int(input("Enter age: "))
            score = int(input("Enter score (out of 400): "))
        except ValueError:
            print("Age and score must be numbers!")
            continue

        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course,
            "score": score
        }

        students.append(student)
        save_students(students)

        print("✅ Student added successfully!")

    # -------------------------------
    # VIEW STUDENTS
    # -------------------------------
    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n=== STUDENT RECORDS ===")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} | {student['age']} | {student['course']} | {student['score']}")

    # -------------------------------
    # DELETE STUDENT
    # -------------------------------
    elif choice == "3":
        if not students:
            print("No students to delete.")
            continue

        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']}")

        try:
            num = int(input("Enter number to delete: "))
            if 1 <= num <= len(students):
                removed = students.pop(num - 1)
                save_students(students)
                print(f"✅ Deleted: {removed['name']}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    # -------------------------------
    # UPDATE STUDENT
    # -------------------------------
    elif choice == "4":
        if not students:
            print("No students to update.")
            continue

        for i, student in enumerate(students, start=1):
            print(f"{i}. {student['name']}")

        try:
            num = int(input("Enter number to update: "))
            if 1 <= num <= len(students):
                student = students[num - 1]

                print("Leave blank to keep old value")

                name = input(f"Name ({student['name']}): ") or student['name']
                age = input(f"Age ({student['age']}): ")
                course = input(f"Course ({student['course']}): ") or student['course']
                score = input(f"Score ({student['score']}): ")

                student['name'] = name
                student['age'] = int(age) if age else student['age']
                student['course'] = course
                student['score'] = int(score) if score else student['score']

                save_students(students)
                print("✅ Student updated successfully!")

            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    # -------------------------------
    # EXIT
    # -------------------------------
    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid option.")