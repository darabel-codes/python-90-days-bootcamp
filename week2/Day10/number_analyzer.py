print("----- NUMBER ANALYZER ----- ")

number = []
n = int(input("How many numbers do you want to analyze? ")) 

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)

print(f"\nNumbers entered: {number}")

print("\nStatistics:")
print(f"Total numbers: {len(number)}")
print(f"Maximum: {max(number)}")
print(f"Minimum: {min(number)}")
print(f"sum: {sum(number)}")
print(f"Average: {sum(number)/len(number)}")