



from contacts_data import contacts

def deleting():
    if len(contacts) == 0:
        print("there is no contact")
    else:
        for i in range(len(contacts)):
            print(i+1, ".", contacts[i][0], contacts[i][1])
        choice = int(input("enter contact number for deleting:"))
        if choice < 1 or choice > len(contacts):
            print("invalid option")
        else:
            print("Selected Contact:")
            print("Name:", contacts[choice-1][0])
            print("Phone:", contacts[choice-1][1])
            confirm = input("are you sure you want to delete this contact? (yes/no):")
            if confirm == "yes":
                contacts.pop(choice-1)
                print("contact deleted successfully!")
            elif confirm == "no":
                print("deletion cancelled")
            else:
                print("invalid option")