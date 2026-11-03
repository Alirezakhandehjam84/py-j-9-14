



from contacts_data import contacts

def showing():

    if len(contacts) == 0:
        print("there is no contact")

    else:
        for i in range(len(contacts)):
            print("Contact:", i+1)
            print("Name:", contacts[i][0])
            print("Phone:", contacts[i][1])