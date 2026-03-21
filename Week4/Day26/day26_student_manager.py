# This is a student manager applicaiton

print("===== STUDENT MANAGER APPLICATION =====")

students = []

# Function to load tasks from file
# def load_tasks():
#     try:
#         with open("students.txt", "r") as file:
#             lines = file.readlines()
            

#             for line in lines:
#                 if "|" in line:
#                     student = line.strip().split("|")
#                     students.append(f"1. {student['name']} | {student['age']} | {student['course']} | {student['score']}")
                    
#             return students
#     except FileNotFoundError:
#         return []


# To save student records to file
def save_students_record(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']} | {student['age']} | {student['course']} | {student['score']}\n")
        

while True:
    print("\n1. Add Student.")
    print("2. View Students.")
    print("3. Update Student.")
    print("4. Delete Student.")
    print("5. Exit.")

    choice = input("Choose an option: ")

# To Add Student

    if choice == "1":
        name = input("Enter student Name: ")
        age = input("Enter student Age: ")
        course = input("Enter student Course: ")
        score = input("Enter Student's Score: ")
        
        student = {
            "name": name,
            "age": age,
            "course": course,
            "score": score
        }
        
        students.append(student)
        save_students_record(students)
        print(f"Student Added Successfully1")


# To view students

    elif choice == "2":
        if not students:
            print(f"No student record found!")
        else:
            print(f"=== STUDENT RECORD ===")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} | {student['age']} | {student['course']} | {student['score']}")
    
    # ✏️ Update Student
    elif choice == "3":
        if not students:
            print("No students to update.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']}")

            try:
                num = int(input("Enter student number to update: "))
                if 1 <= num <= len(students):
                    students[num - 1]["name"] = input("New name: ")
                    students[num - 1]["age"] = input("New age: ")
                    students[num - 1]["course"] = input("New course: ")
                    print("Student updated!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    # ❌ Delete Student
    elif choice == "4":
        if not students:
            print("No students to delete.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']}")

            try:
                num = int(input("Enter student number to delete: "))
                if 1 <= num <= len(students):
                    removed = students.pop(num - 1)
                    print(f"Deleted: {removed['name']}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    # 🚪 Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
