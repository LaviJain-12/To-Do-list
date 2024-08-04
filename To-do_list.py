class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task index")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Marked task as completed: {self.tasks[index]['task']}")
        else:
            print("Invalid task index")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
