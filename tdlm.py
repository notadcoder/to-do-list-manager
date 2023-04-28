class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        if self.due_date:
            return "{} (due {})".format(self.description, self.due_date)
        else:
            return self.description


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        self.tasks.pop(index)

    def modify_task(self, index, new_description=None, new_due_date=None):
        task = self.tasks[index]
        if new_description:
            task.description = new_description
        if new_due_date:
            task.due_date = new_due_date

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                print("Task {}: {}".format(i+1, task))


def main():
    todo_list = ToDoList()

    while True:
        print()
        print("Choose an option:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Modify task")
        print("4. Show tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            if due_date:
                task = Task(description, due_date)
            else:
                task = Task(description)
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index-1)
        elif choice == "3":
            index = int(input("Enter task index to modify: "))
            new_description = input("Enter new description (press enter to skip): ")
            new_due_date = input("Enter new due date (press enter to skip): ")
            todo_list.modify_task(index-1, new_description, new_due_date)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
