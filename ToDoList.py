class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks!")