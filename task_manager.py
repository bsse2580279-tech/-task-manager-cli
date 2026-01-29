import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    
    for task in tasks:
        status = "done" if task["completed"] else "w8"
        print(f"{task['id']}. [{status}] {task['title']}")

def main():
    while True:
        print("\n" + "="*30)
        print("Task MANAGER CLI")
        print("="*30)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task (coming soon)")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Complete feature coming soon!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()