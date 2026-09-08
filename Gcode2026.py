
todos = []

def show_todos():
    if not todos:
        print("\nNo tasks yet.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(todos, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['task']}")

while True:
    print("\n--- TO-DO APP ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        todos.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        show_todos()

    elif choice == "3":
        show_todos()
        if todos:
            try:
                number = int(input("Enter task number to complete: "))
                todos[number - 1]["done"] = True
                print("Task completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        show_todos()
        if todos:
            try:
                number = int(input("Enter task number to remove: "))
                todos.pop(number - 1)
                print("Task removed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
