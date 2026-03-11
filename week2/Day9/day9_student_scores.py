students =[]
scores = []

n = int(input("How many students? "))    

for i in range(n):
    name = input(f"Enter the name of student {i+1}: ")
    students.append(name)
    score = float(input(f"Enter the score for {name}: "))
    scores.append(score)

print("\nStudent Scores:")
for i in range(n):
    print(f"{students[i]}: {scores[i]}")

average_score = sum(scores) / n
print(f"\nClass Average: {average_score:.2f}")  