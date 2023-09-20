class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        status = "Done" if self.is_done else "Not Done"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

    def mark_task_as_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number-1].mark_as_done()

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do App:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_as_done(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
