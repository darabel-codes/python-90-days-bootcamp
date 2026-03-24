class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"{self.name} | {self.age} | {self.course.display_course()}")