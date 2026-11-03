



from hotel_data import rooms, reservations

def cancel_reservation():
    if len(reservations) == 0:
        print("there is no reservation")
    else:
        reservation_id = int(input("enter reservation ID: "))
        found = False
        for reservation in reservations:
            if reservation[0] == reservation_id:
                found = True
                selected_reservation = reservation
        if found == False:
            print("reservation not found")
        else:
            print("Name:", selected_reservation[1])
            print("Room:", selected_reservation[3])
            confirm = input("are you sure? (yes/no): ")
            if confirm == "yes":
                for room in rooms:
                    if room[0] == selected_reservation[3]:
                        room[4] = "Available"
                reservations.remove(selected_reservation)
                print("reservation cancelled successfully")
            elif confirm == "no":
                print("cancellation stopped")
            else:
                print("invalid option")