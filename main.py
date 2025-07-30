import csv
import os

FILENAME = "tasks.csv"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            tasks = list(reader)
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Status", "Due Date"])  # Header
        writer.writerows(tasks)

def add_task():
    title = input("Enter task title: ")
    desc = input("Enter description: ")
    due_date = input("Enter due date (e.g., tomorrow, 2025-08-01): ")
    tasks = load_tasks()
    tasks.append([title, desc, "Pending", due_date])
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        due = task[3] if len(task) > 3 else "N/A"
        print(f"{i}. [{task[2]}] {task[0]} - {task[1]} (Due: {due})")

def mark_done():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index][2] = "Done"
            save_tasks(tasks)
            print("✅ Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("🗑️ Task deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def search_tasks():
    keyword = input("Enter keyword to search in task titles: ").lower()
    tasks = load_tasks()
    found = False
    print("\n🔎 Search Results:")
    for i, task in enumerate(tasks, start=1):
        if keyword in task[0].lower():
            due = task[3] if len(task) > 3 else "N/A"
            print(f"{i}. [{task[2]}] {task[0]} - {task[1]} (Due: {due})")
            found = True
    if not found:
        print("❌ No matching tasks found.")

def filter_tasks():
    status_filter = input("Enter status to filter by (Pending / Done): ").capitalize()
    if status_filter not in ["Pending", "Done"]:
        print("❌ Invalid status. Please type 'Pending' or 'Done'.")
        return

    tasks = load_tasks()
    filtered = [task for task in tasks if task[2] == status_filter]

    print(f"\n📂 {status_filter} Tasks:")
    if not filtered:
        print("No tasks with this status.")
        return

    for i, task in enumerate(filtered, start=1):
        due = task[3] if len(task) > 3 else "N/A"
        print(f"{i}. [{task[2]}] {task[0]} - {task[1]} (Due: {due})")

def menu():
    while True:
        print("\n=== My Personal Task Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Search Tasks by Title")
        print("6. Filter Tasks by Status")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_tasks()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            print("👋 Exiting. See you next time!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
  
