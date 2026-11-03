



from contacts_data import contacts
def editing () :
    if len(contacts)==0 :
        print("there is no contact")
    else :
        for i in range(len(contacts)) :
            print(i+1 , "." ,contacts[i][0],contacts[i][1])
        choice=int(input("enter contact number for editing:"))
        if choice<1 or choice>len(contacts) :
            print("invalid option")
        else :
            print("Selected Contact:")
            print("Name:", contacts[choice-1][0])
            print("Phone:", contacts[choice-1][1])
            editing_menu=input("\n---what do you want to edit?---\n"
                               "1.edit name\n"
                               "2.edit phone\n"
                               "3.edit both\n"
                               "4.back\n"
                               "yoor choice:")
            match editing_menu :
                case "1" :
                    new_name = input("enter new name: ")
                    if new_name.strip() == "":
                        print("name can not be empty")
                    else:
                        contacts[choice-1][0] = new_name
                        print("name changed successfully!")
                case "2" :
                    new_phone = input("enter new phone number: ")
                    if not new_phone.isdigit() or len(new_phone) != 11 or not new_phone.startswith("09"):
                        print("invalid phone number")
                    else:
                        found = False
                        for i in range(len(contacts)):
                            if i != choice-1 and contacts[i][1] == new_phone:
                                found = True
                        if found:
                            print("this phone number already exists")
                        else:
                            contacts[choice-1][1] = new_phone
                            print("phone number changed successfully!")
                case "3":
                    new_name = input("enter new name: ")
                    new_phone = input("enter new phone number: ")
                    if new_name.strip() == "":
                        print("name can not be empty")
                    elif not new_phone.isdigit() or len(new_phone) != 11 or not new_phone.startswith("09"):
                        print("invalid phone number")
                    else:
                        found = False
                        for i in range(len(contacts)):
                            if i != choice-1 and contacts[i][1] == new_phone:
                                found = True
                        if found:
                            print("this phone number already exists")
                        else:
                            contacts[choice-1][0] = new_name
                            contacts[choice-1][1] = new_phone
                            print("contact changed successfully!")
                case "4":
                    print("back to main menu")
                case _:
                    print("invalid option")
        
            