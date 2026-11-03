



from hotel_data import reservations

def search_reservation():
    if len(reservations) == 0:
        print("there is no reservation")
    else:
        search = input(
            "1.search by name\n"
            "2.search by phone\n"
            "3.search by room number\n"
            "choose: ")
        found = False
        match search:
            case "1":
                value = input("enter customer name: ")
                for reservation in reservations:
                    if value.lower() == reservation[1].lower():
                        found = True
                        print(reservation)
            case "2":
                value = input("enter phone number: ")
                for reservation in reservations:
                    if value == reservation[2]:
                        found = True
                        print(reservation)
            case "3":
                value = input("enter room number: ")
                for reservation in reservations:
                    if value == str(reservation[3]):
                        found = True
                        print(reservation)
            case _:
                print("invalid option")
                return
        if found == False:
            print("reservation not found")