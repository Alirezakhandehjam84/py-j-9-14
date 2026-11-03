



from task_data import tasks,completed_tasks
def deleting():
    if len(tasks)==0 :
        print("there is nothing to delete")
    else :
        for i in range(len(tasks)) :
            print(i+1 , "." , tasks[i])
        number=input("enter task number to delete")
        if number.isdigit()==True :
            number=int(number)
            if number<1 or number>len(number) :
                print("please enter a valid number")
            else :
                tasks.pop(number-1)
                completed_tasks.clear()
                print("task deleted")
        else :
            print("please enter a number")