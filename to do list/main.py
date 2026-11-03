



from add_task import adding
from show_task import showing
from complet_task import completing
from delete_task import deleting
from search_task import searching
while True :
    main_menu=input("\n---to do list---\n"
                    "1.add enw task\n"
                    "2.show all tasks\n"
                    "3.completed tasks\n"
                    "4.delete task\n"
                    "5.search task\n"
                    "0.exit\n"
                    "your choise:")
    match main_menu :
        case "1" :
            ezafe =input("enter your task:")
            adding(ezafe)
            continue
        case "2" :
            showing()
            continue
        case "3" :
            completing()
            continue
        case "4" :
            deleting()
            continue
        case "5" :
            searching()
            continue
        case "0" :
            print("goodbye")
            break
        case _:
            print("invalid option")
