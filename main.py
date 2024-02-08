from ToDoList import ToDoList
if __name__ == "__main__":
    print("let's to DO!!")
    todo = ToDoList()
    todo.add_task("洗濯")
    todo.show_tasks()
    todo.add_task("洗い物")
    todo.show_tasks()
    todo.remove_task("洗い物")
    todo.show_tasks()