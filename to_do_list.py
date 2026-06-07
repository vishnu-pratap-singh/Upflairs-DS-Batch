class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("✅ Task added successfully!")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("📋 No tasks available.")
        else:
            print("\n----- TO-DO LIST -----")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        self.view_tasks()

        if len(self.tasks) == 0:
            return

        try:
            task_no = int(input("\nEnter task number to delete: "))

            if 1 <= task_no <= len(self.tasks):
                removed = self.tasks.pop(task_no - 1)
                print(f"❌ '{removed}' deleted successfully!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number.")


class App:

    def __init__(self):
        self.todo = TodoList()

    def run(self):

        while True:
            print("\n===== TO-DO LIST MENU =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.todo.add_task()

            elif choice == "2":
                self.todo.view_tasks()

            elif choice == "3":
                self.todo.delete_task()

            elif choice == "4":
                print("Thank you for using To-Do List App!")
                break

            else:
                print("Invalid choice! Try again.")


# Driver Code
app = App()
app.run()