#SIMPLE TO DO LIST MANAGER PROGRAM.

def show_tasks(tasks):
    """
    Displays the current list of tasks.
    """
    if not tasks:
        print("\n--- Your list is currently empty! ---")
    else:
        print("\n--- Your Current Tasks ---")
        # enumerate helps to display index starting from 1
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def main():
    # Attempt to load existing tasks from a text file
    try:
        with open("tasks.txt", "r") as file:
            # Strip newline characters and store in a list
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        tasks = []

    while True:
        print("\n1. View Tasks | 2. Add Task | 3. Delete Task | 4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        
        elif choice == '2':
            new_task = input("Enter the task description: ")
            tasks.append(new_task)
            print("✅ Task added successfully!")
        
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    # pop() removes the item at the given index
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ Deleted: '{removed}'")
                except (ValueError, IndexError):
                    # Handles non-integer input or out-of-range numbers
                    print("❌ Invalid number! Please try again.")
        
        elif choice == '4':
            # Save the final list to the file before closing
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print("Settings saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
      
