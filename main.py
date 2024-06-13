# Create an array to contain all of the tasks, in this case a series of strings.

tasks = []

# Individual function to handle appending to tasks.

def addTask():
    task = input("Please enter your task: ")
    tasks.append(task)
    print("Task: '{task}', added to the list")

# A simple function that lists out all the contents of tasks.

def listTasks():
    if not tasks:
        print("There are not tasks currently.")
    else:
        print("\n")
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

# A simple function that will call pop on the index placement that we have called for removal of a task.

def deleteTask():
    listTasks()
    try:
        print("Select wich task you wish to delete:")
        taskToDelete = int(input("Enter the # you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete}, was removed")
        else:
            print(f"Task #{taskToDelete} number not found")

    except:
        print("Invalid input. Please provide a valid input")

# The "main" function.

if __name__ == "__main__":
    # Create a loop to run the app.
    print("Welcome!")
    
    while True:
        print("\n")
        print("Please select an option.")
        print("-------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please provide a valid input.")

    print("Goodbye")