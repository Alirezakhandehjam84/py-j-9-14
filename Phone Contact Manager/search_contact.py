



from contacts_data import contacts

def searching():
    if len(contacts) == 0:
        print("there is no contact")
    else:
        search = input("enter the name for searching:")
        found = False
        for contact in contacts:
            if search == contact[0]:
                found = True
                print("Name:", contact[0])
                print("Phone:", contact[1])
        if found == False:
            print("could not find your contact")