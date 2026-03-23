import json

print("==== STUDENT MANAGER (PERSISTENT) ====")


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"{self.name} | {self.age} | {self.course}")

    # 🔄 Convert object → dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    # 🔁 Convert dictionary → object
    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["age"], data["course"])


# 📂 Load students from file
def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            return [Student.from_dict(s) for s in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# 💾 Save students to file
def save_students(students):
    with open("students.json", "w") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)


students = load_students()


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    # ➕ Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        new_student = Student(name, age, course)
        students.append(new_student)

        save_students(students)

        print("Student saved successfully!")

    # 📋 View Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- STUDENT LIST ---")
            for i, student in enumerate(students, start=1):
                print(f"{i}. ", end="")
                student.display_info()

    # 🚪 Exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")