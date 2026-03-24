class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def display_course(self):
        return f"{self.name} ({self.duration} months)"