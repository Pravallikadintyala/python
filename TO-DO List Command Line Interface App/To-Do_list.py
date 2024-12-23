import os

# A simple To-Do List CLI App

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "Completed" if task['completed'] else "Pending"
            file.write(f"{task['task']} [{status}]\n")
    print("Tasks saved successfully!")

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().rsplit(' [', 1)
                task = task_data[0]
                status = task_data[1][:-1]
                tasks.append({'task': task, 'completed': status == "Completed"})
        print("Tasks loaded successfully!")
    else:
        print("No saved tasks found.")
    return tasks

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        print(f"Debug: User chose option {choice}")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            save_tasks(tasks)
        elif choice == '6':
            tasks = load_tasks()
        elif choice == '7':
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main()
