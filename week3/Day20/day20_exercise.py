# This is a program for Student Grade Analyzer
print("===== STUDENT GRADE ANALYZER =====")

# Getting the student name
student_name = input("Enter the student's name: ")

# Getting the number of subjects
no_of_subjects = int(input("Please enter the number of subjects the student is offering: "))

# Getting the grades for each subject
scores = []

for i in range(no_of_subjects):
    subject = input(f"Enter the name of subject {i + 1}: ")
    grade = float(input(f"Enter the grade for {subject}: "))
    scores.append(grade)

# Calculating the average grade
average_grade = sum(scores) / no_of_subjects

# Determining the grade category

if average_grade >= 70:
    grade_category = "A"
elif average_grade >= 60:
    grade_category = "B"
elif average_grade >= 50:
    grade_category = "C"
elif average_grade >= 40:
    grade_category = "D"
else:
    grade_category = "F"

# # Displaying the results

# print("\n===== STUDENT'S RESULT =====")
# print(f"Student Name: {student_name}")
# print(f"Student's Scores: {scores}")
# print(f"Student's Total Score: {sum(scores)}")
# print(f"Average Grade: {average_grade:.2f}")
# print(f"Grade Category: {grade_category}")

# To save each student's result in a file, we can use the following code:
with open("student_results.txt", "a") as file:
    file.write(f"Student Name: {student_name}\n")
    file.write(f"Student's Scores: {scores}\n")
    file.write(f"Student's Total Score: {sum(scores)}\n")
    file.write(f"Average Grade: {average_grade:.2f}\n")
    file.write(f"Grade Category: {grade_category}\n")
    file.write("-" * 30 + "\n")
file.close()

# To read and display all the results from the file, we can use the following code:
print("\n===== ALL STUDENTS' RESULTS =====")
with open("student_results.txt", "r") as file:
    results = file.read()
    print(results)
file.close()
