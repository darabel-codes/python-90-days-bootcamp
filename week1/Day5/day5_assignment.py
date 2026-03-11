print("----- AGE ELIGIBILITY CHECKER -----")
print()

print("Welcome to the Age Eligibility Checker!")
print()

name = input("Please enter your name: ")
age = int(input("Enter your age: "))
print()

# if age >= 18:
#     print(f"Hello, {name}! You are eligible to vote.")

if age <= 12:
    print(f"Hello, {name}! You are a child.")

elif age <= 19:
    print(f"Hello, {name}! You are a Teenager.")

else:
    print(f"Hello, {name}! You are an Adult.")

    print()
print("Thank you for using the Age Eligibility Checker!")

