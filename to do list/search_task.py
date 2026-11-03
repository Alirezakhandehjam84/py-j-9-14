



from task_data import tasks
def searching ():
    search=input("enter the task name that you want to search:")
    if search in tasks :
        print("task find")
    else :
        print("task not find")