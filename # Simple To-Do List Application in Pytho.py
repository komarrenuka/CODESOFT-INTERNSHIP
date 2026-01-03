# Simple To-Do List Application in Python

# Store tasks in a list of dictionaries
tasks = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. [{status}] {task['task']}")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number-1]["completed"] = True
            print(f"Task '{tasks[task_number-1]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number-1)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
