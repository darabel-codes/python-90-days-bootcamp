# This program is a todo list application that allows users to add, view, and delete tasks.

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
       
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("5. Clear All Tasks")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break
    
    elif choice == "5":
        tasks.clear()
        print("All tasks cleared.")

    else:
        print("Invalid option. Try again.")