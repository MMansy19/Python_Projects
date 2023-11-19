# Import functions from the action_functions module
from action_functions import *

# Initialize an empty list to store tasks
tasks = []

# Main loop to handle user input
while True:
    # Get user input for the desired action
    action = input("Enter a Command: add/view/remove/exit: ")

    # Check the user's action and perform the corresponding operation
    if action == "add":
        # If the action is 'add', prompt the user for a task and call the 'add' function
        task = input("Enter the task: ")
        add(tasks, task)
    elif action == "view":
        # If the action is 'view', call the 'view' function to display the current tasks
        view(tasks)
    elif action == "remove":
        # If the action is 'remove', call the 'view' function to display tasks, 
        # then prompt the user for the task number to remove and call the 'remove' function
        view(tasks)
        task_number = int(input("Enter the task number you want to remove: "))
        remove(tasks, task_number)
    elif action == "exit":
        # If the action is 'exit', print a goodbye message and exit the loop
        print("Thank you!")
        break
    else:
        # If the user enters an invalid command, inform them of the error
        print("Invalid Command")
