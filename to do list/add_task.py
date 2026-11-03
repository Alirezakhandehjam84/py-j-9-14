



from task_data import tasks
def adding(ezafe:str) :
    if ezafe.strip()=="" :
        print("task can not be empety")
    elif ezafe in tasks :
        print("this task is already exist")
    else :
        tasks.append(ezafe)
        print("task added")
        
