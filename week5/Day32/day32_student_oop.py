# This is the student manager (oop) version

print("===== STUDENT MANAGER (OOP) =====")

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def display_info(self):
        print(f"{self.name} | {self.age} | {self.course}\n")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
# ➕ Add Student

    if choice == "1":
        name = input("\nEnter name of the Student: ")
        age = int(input("Enter Age of the Student: "))
        course = input("Enter Course of the Student: ")
    
        new_student = Student(name, age, course)
        students.append(new_student)
        print(f"Student added successfully!")

 # 📋 View Students
 
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n === STUDENT LIST ===")
            for i, student in enumerate(students, start=1):
                print(f"{1}. ", end="")
                student.display_info()
# 🚪 Exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        
    