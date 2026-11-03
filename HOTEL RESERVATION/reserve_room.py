



from hotel_data import rooms, reservations

def reserve_room():
    name = input("enter your full name: ")
    phone = input("enter your phone number: ")
    if name.strip() == "":
        print("name can not be empty")
    elif not phone.isdigit() or len(phone) != 11 or not phone.startswith("09"):
        print("invalid phone number")
    else:
        room_number = int(input("enter room number: "))
        found = False
        for room in rooms:
            if room[0] == room_number:
                found = True
                selected_room = room
        if found == False:
            print("room does not exist")
        elif selected_room[4] == "Reserved":
            print("room is already reserved")
        else:
            people = int(input("enter number of people: "))
            nights = int(input("enter number of nights: "))
            if people < 1 or people > selected_room[2]:
                print("invalid number of people")
            elif nights <= 0:
                print("invalid number of nights")
            else:
                reservation_id = len(reservations) + 1
                total_price = selected_room[3] * nights
                reservations.append([
                    reservation_id,
                    name,
                    phone,
                    room_number,
                    people,
                    nights,
                    total_price
                ])
                selected_room[4] = "Reserved"
                print("reservation successful!")
                print("Reservation ID:", reservation_id)
                print("Total Price:", total_price, "$")