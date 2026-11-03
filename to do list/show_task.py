



from task_data import tasks
def showing() :
    if len(tasks)==0 :
        print("there is no task")
    else :
        for i in range(len(tasks)) :
            print(i+1 , "." , tasks[i])
        

