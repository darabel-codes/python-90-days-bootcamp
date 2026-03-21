# This program is about JSON(JavaScript Object Notation)

import json

print("===== STUDENT MANAGER (JSON) =====")

# Load students from JSON

def load_students():
    try:
        with open("students.json", "r") as file:
            student = file.read().strip()

            if not student:  # if file is empty
                return []

            return json.loads(student)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Saving students to JSON

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


students = load_students()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter the name of student: ")
        age = input("Enter the age of the student: ")
        course = input ("Enter the course of study: ")
        score = input("Enter the school of the student (out of 400): ")
        
        student = {
            "name": name,
            "age": age,
            "course": course,
            "score": score
        }
        
        students.append(student)
        save_students()
        print(f"Student Record added successfully!")

# To view student record

    elif choice == "2":
        try:
            if not students:
                print("No student records found")
            else:
                print(f"=== STUDENTS RECORD ===")
                for student in students:
                    print(f"{student['name']} | {student['age']} | {student['course']} | {student['score']}\n")
        except ValueError:
            print(f"Invalid Number. Enter a valid option")

# Deleting student's record

    elif choice == "3":
        for student in students:
            print(f"{1.} {student['name']}\n")
        try:
            num = int(input("Enter the number of student to delete: "))
            if 1 <= num <= len(students):
                remove = students.pop(num - 1)
                save_students()
                print(f"Deleted: {remove['name']}")
            else:
                print(f"Invalid number")
        except ValueError:
            print("Enter a valid number: ")
    
      # 🚪 Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")       
        
