



from contacts_data import contacts

def adding():
    name = input("enter contact name: ")
    if name.strip() == "":
        print("name can not be empty")
    else:
        phone = input("now enter phone number: ")
        if phone.isdigit()!=True or len(phone) != 11 or not phone.startswith("09"):
            print("invalid phone number")
        else:
            duplicate = False
            for contact in contacts:
                if contact[1] == phone:
                    duplicate = True
            if duplicate:
                print("this phone number already exists!")
            else:
                contacts.append([name, phone])
                print("contact added successfully!")