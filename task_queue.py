from collections import deque

task_queue = deque()

while True:
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. Process task")
    print("3. Show queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Is this task high priority? (yes/no): ").lower()
        ready = input("Is the task ready to run? (yes/no): ").lower()

        # Boolean logic
        if (priority == "yes" and ready == "yes") or priority == "yes":
            task_queue.append(task)
            print("Task added to the queue.")
        else:
            print("Task does not meet the execution criteria.")

    elif choice == "2":
        if task_queue:
            task = task_queue.popleft()
            print(f"Executing task: {task}")
        else:
            print("Queue is empty.")

    elif choice == "3":
        if task_queue:
            print("Current queue:")
            for task in task_queue:
                print("-", task)
        else:
            print("Queue is empty.")

    elif choice == "4":
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Please try again.")