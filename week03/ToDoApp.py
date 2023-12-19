class Task:
    def __init__(self, taskName, taskDescription, taskDue, taskPriority):
        self.name = taskName
        self.description = taskDescription
        self.due = taskDue
        self.priority = taskPriority


class Todo:
    def __init__(self):
        self.pendingTasks = []
        self.completedTasks = []

    def addTask(self, task):
        if task.name not in self.pendingTasks:
            self.pendingTasks.append(task)
        else:
            print("\nTask name already exists.")

    def displayAllTasks(self):
        flag = False
        print("\nThe pending tasks are: ")
        for task in self.pendingTasks:
            printTask(task)
            flag = True
        if not flag:
            print("\n   No tasks to show here")

        flag = False
        print("\nThe completed tasks are: ")
        for task in self.completedTasks:
            printTask(task)
            flag = True
        if not flag:
            print("\n   No tasks to show here")

    def taskCompletion(self, taskName):
        for task in self.pendingTasks:
            if taskName.lower() == task.name.lower():
                self.completedTasks.append(task)
                self.pendingTasks.remove(task)
                print("\nTask marked as completed successfully!")
                return

        print("\nTask not found.")

    def updateTask(self, taskName):
        for task in self.pendingTasks:
            if taskName.lower() == task.name.lower():
                while True:
                    try:
                        choice = int(input("""\nWhat do you wish to update?:
                        1. Name
                        2. Description
                        3. Due Date
                        4. Priority
                        5. Stop"""))

                        if choice == 5:
                            break
                        elif choice == 1:
                            name = input("\nEnter updated name: ")
                            task.name = name
                        elif choice == 2:
                            description = input("\nEnter updated description: ")
                            task.description = description
                        elif choice == 3:
                            dueDate = input("\nEnter updated due date: ")
                            task.due = dueDate
                        elif choice == 4:
                            while True:
                                priority = input("\nEnter updated priority (low, medium, high): ").lower()
                                if priority in {"low", "medium", "high"}:
                                    task.priority = priority
                                    break
                                else:
                                    print("Invalid priority. Please enter 'low', 'medium', or 'high'.")
                        else:
                            print("\nInvalid option chosen")

                    except ValueError:
                        print("\nPlease enter integers-only.")

                print("\nTask updated successfully!")
            return

        for task in self.completedTasks:
            if taskName.lower() == task.name.lower():
                while True:
                    try:
                        choice = int(input("""\nWhat do you wish to update?:\n
                        1. Name
                        2. Description
                        3. Due Date
                        4. Priority
                        5. Stop: 
                         """))

                        if choice == 5:
                            break
                        elif choice == 1:
                            name = input("\nEnter updated name: ")
                            task.name = name
                        elif choice == 2:
                            description = input("\nEnter updated description: ")
                            task.description = description
                        elif choice == 3:
                            dueDate = input("\nEnter updated due date: ")
                            task.due = dueDate
                        elif choice == 4:
                            while True:
                                priority = input("\nEnter updated priority (low, medium, high): ").lower()
                                if priority in {"low", "medium", "high"}:
                                    task.priority = priority
                                    break
                                else:
                                    print("Invalid priority. Please enter 'low', 'medium', or 'high'.")
                        else:
                            print("\nInvalid option chosen")

                    except ValueError:
                        print("\nPlease enter integers between(1-5) only.")

                print("\nTask updated successfully!")
            return

        print("\nTask not found")

    def remove(self, taskName):
        for task in self.pendingTasks:
            if task.name.lower() == taskName.lower():
                self.pendingTasks.remove(task)
                print("\nTask removed successfully!")
                return
        for task in self.completedTasks:
            if task.name.lower() == taskName.lower():
                self.completedTasks.remove(task)
                print("\nTask removed successfully!")
                return

        print("\nTask not found.")


def printTask(task):
    print(f"""
    Task name: {task.name}
    Task description: {task.description}
    Task Due: {task.due}
    Task Priority: {task.priority}""")

# def updateTask(task):
#     while True:
#         choice = input("""\nWhat do you wish to update?:
#         1. Name
#         2. Description
#         3. Due Date
#         4. Priority
#         5. Stop""")
#
#         if choice == "5":
#             break
#         elif choice == "1":
#             name = input("\nEnter updated Name: ")
#             task.name = name
#         elif choice == "2":
#             description = input("\nEnter updated Description: ")
#             task.description = description
#         elif choice == "3":
#             dueDate = input("\nEnter updated Due Date: ")
#             task.due = dueDate
#         elif choice == "4":
#             priority = input("\nEnter updated Priority: ")
#             task.priority = priority
#         else:
#             print("\nInvalid option chosen")
#
#     return task


def createTask():
    name = input("\nEnter the task name: ")
    desc = input("\nEnter the task description: ")
    dueDate = input("\nEnter the task due date: ")
    while True:
        priority = input("\nEnter updated Priority (low, medium, high): ").lower()
        if priority in {"low", "medium", "high"}:
            break
        else:
            print("Invalid priority. Please enter 'low', 'medium', or 'high'.")

    task = Task(name, desc, dueDate, priority)

    return task


def menu():
    print("""
        Menu
    1. View menu
    2. Add task
    3. Display all tasks
    4. Mark task as completed
    5. Update task
    6. Delete task
    7. Exit
    """)


def main():
    todo = Todo()
    print("\nWelcome to Kartik's To-Do interface!")

    menu()
    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                menu()
            elif choice == 2:
                task = createTask()
                todo.addTask(task)
            elif choice == 3:
                todo.displayAllTasks()
            elif choice == 4:
                name = input("\nEnter the completed task name: ")
                todo.taskCompletion(name)
            elif choice == 5:
                name = input("\nEnter the task(updation) name: ")
                todo.updateTask(name)
            elif choice == 6:
                name = input("\nEnter the task(deletion) name: ")
                todo.remove(name)
            elif choice == 7:
                print("\nThank you for using Kartik's To-Do app!")
                break
            else:
                print("\nInvalid choice entered.")

        except ValueError:
            print("\nPlease enter integers-only.")


if __name__ == '__main__':
    main()