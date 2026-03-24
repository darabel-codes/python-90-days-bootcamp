from student import Student
from course import Course
from utils import show_menu

print("==== MODULAR STUDENT SYSTEM ====")

students = []
courses = [
    Course("Cybersecurity", 6),
    Course("Software Engineering", 8),
    Course("Data Science", 5)
]

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        print("\nCourses:")
        for i, c in enumerate(courses, start=1):
            print(f"{i}. {c.display_course()}")

        course_choice = int(input("Select course: ")) - 1

        if 0 <= course_choice < len(courses):
            student = Student(name, age, courses[course_choice])
            students.append(student)
            print("Student added!")

        else:
            print("Invalid course.")

    elif choice == "2":
        print("\n--- STUDENTS ---")
        for s in students:
            s.display_info()

    elif choice == "3":
        print("\n--- COURSES ---")
        for c in courses:
            print(c.display_course())

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")