students = []

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    student_name = input(f"\nEnter name of student {i+1}: ")

    # Get number of subjects for this student
    num_subjects = int(input(f"Enter number of subjects for {student_name}: "))

    # Nested loop to collect scores
    scores = []
    for j in range(num_subjects):
        while True:  # validation loop
            score = input(f"Enter score for subject {j+1} (0-100): ")
            if score.isdigit() and 0 <= int(score) <= 100:
                scores.append(int(score))
                break
            else:
                print("Invalid input! Score must be a number between 0 and 100.")

    # Calculate total and average
    total = sum(scores)
    average = round(total / num_subjects, 2)

    # Store student data in dictionary
    student = {
        "name": student_name,
        "scores": scores,
        "total": total,
        "average": average,
        "highest": max(scores),
        "lowest": min(scores)
    }
    students.append(student)

print("\n=== STUDENT REPORTS ===")
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Scores: {s['scores']}")
    print(f"Total: {s['total']}, Average: {s['average']}")
    print(f"Highest: {s['highest']}, Lowest: {s['lowest']}")

with open("student_reports.txt", "w") as file:
    for s in students:
        file.write(f"{s['name']} - Scores: {s['scores']}, Total: {s['total']}, Average: {s['average']}, Highest: {s['highest']}, Lowest: {s['lowest']}\n")