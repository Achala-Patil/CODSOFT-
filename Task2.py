tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def delete_task(task_index):
    if task_index >= 0 and task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. [{status}] {task['task']}")
    else:
        print("No tasks in the to-do list.")

def update_task(task_index, new_task):
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["task"] = new_task
        print("Task updated successfully.")
    else:
        print("Task not found.")

def mark_task_completed(task_index):
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Task not found.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(task_index)
        elif choice == '5':
            view_tasks()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the to-do list!")

if __name__ == "__main__":
    main()
