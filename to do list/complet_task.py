



from task_data import tasks,completed_tasks
def completing():
    if len(tasks)==0 :
        print("there is no task")
    else :
        for i in range(len(tasks)) :
            print(i+1 , "." , tasks[i])
        number =input("enter the task number:")
        number=int(number)
        if number.isdigit()==True :
            if number<1 or len(tasks)<number :
                print("invalid task number")
            elif number in completed_tasks :
                print("this task already completed")
            else :
                completed_tasks.append(number)
                print("task complete")
        else :
            print("please enter a valid number")
