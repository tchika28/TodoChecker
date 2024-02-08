from ToDoList import ToDoList
if __name__ == "__main__":
    print("let's to DO!!")
    todo = ToDoList()
   
    while True:
        print("\nCommands: \n1. Add task\n2. Remove task\n3. Show tasks\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            task =input("Enter task to remove: ")
            todo.remove_task(task)
        elif choice == '3':
            todo.show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")