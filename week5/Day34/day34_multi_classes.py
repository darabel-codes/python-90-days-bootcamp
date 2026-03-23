print("==== STUDENT & COURSE SYSTEM ====")


# 📘 Course Class
class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def display_course(self):
        return f"{self.name} ({self.duration} months)"


# 👤 Student Class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course  # relationship here

    def display_info(self):
        print(f"{self.name} | {self.age} | {self.course.display_course()}")


# 📦 Data storage
students = []
courses = []


# 🧠 Pre-create some courses
courses.append(Course("Cybersecurity", 6))
courses.append(Course("Software Engineering", 8))
courses.append(Course("Data Science", 5))


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. View Courses")
    print("4. Exit")

    choice = input("Choose option: ")

    # ➕ Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        print("\nAvailable Courses:")
        for i, c in enumerate(courses, start=1):
            print(f"{i}. {c.display_course()}")

        course_choice = int(input("Select course number: ")) - 1

        if 0 <= course_choice < len(courses):
            selected_course = courses[course_choice]
            student = Student(name, age, selected_course)
            students.append(student)
            print("Student added successfully!")
        else:
            print("Invalid course selection.")

    # 📋 View Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- STUDENT LIST ---")
            for i, s in enumerate(students, start=1):
                print(f"{i}. ", end="")
                s.display_info()

    # 📘 View Courses
    elif choice == "3":
        print("\n--- COURSE LIST ---")
        for c in courses:
            print(c.display_course())

    # 🚪 Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")