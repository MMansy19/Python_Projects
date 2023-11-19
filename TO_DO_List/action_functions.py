def add(list,task):
    list.append(task)

def view(list):
    for index,task in enumerate(list):
        print(f"({index+1}) {task} \n")

def remove(list,task_number):
    list.pop(task_number-1)

