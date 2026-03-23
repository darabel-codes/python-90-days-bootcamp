# This program is introduction to OOP

print("===== STUDENT CLASS SYSTEM =====")

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"{self.course}")
    
    def is_adult(self):
        return self.age >= 18

# Create Objects

student1 = Student("Jerome", 30, "Cybersecurity")
student2 = Student("David", 25, "Engineering")

# Display info

print("\n--- STUDENT 1 ---")
student1.display_info()
print(student1.is_adult())

print("\n--- STUDENT 2 ---")
student2.display_info()

