print("==== TO-DO LIST APP (PRO) ====")

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            tasks = []

            for line in lines:
                if "|" in line:
                    task, status = line.strip().split("|")
                    tasks.append({"task": task, "done": status == "True"})

            return tasks
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['done']}\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. {task['task']} {status}")

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Search")
    print("6. Exit")

    choice = input("Choose an option: ")

    # ➕ Add Task
    if choice == "1":
        task_name = input("Enter new task: ").strip()

        if not task_name:
            print("Task cannot be empty.")
            continue

        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print("Task added successfully!")

    # 📋 View Tasks
    elif choice == "2":
        view_tasks(tasks)

    # 🗑️ Delete Task
    elif choice == "3":
        view_tasks(tasks)

        try:
            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed['task']}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    # ✅ Mark Task as Completed
    elif choice == "4":
        view_tasks(tasks)

        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                save_tasks(tasks)
                print("Task marked as completed ✔")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    # 🔍 Search Task
    elif choice == "5":
        keyword = input("Enter keyword: ").lower()

        found = False
        print("\n--- SEARCH RESULTS ---")

        for task in tasks:
            if keyword in task["task"].lower():
                status = "✔" if task["done"] else "❌"
                print(f"{task['task']} {status}")
                found = True

        if not found:
            print("No matching tasks found.")

    # 👋 Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")