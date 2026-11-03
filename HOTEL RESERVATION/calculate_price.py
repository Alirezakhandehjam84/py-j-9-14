



from hotel_data import rooms, reservations

def calculate_price():
    room_number = int(input("enter room number: "))
    found = False
    for room in rooms:
        if room[0] == room_number:
            found = True
            selected_room = room
    if found == False:
        print("room does not exist")
    else:
        nights = int(input("enter number of nights: "))
        if nights <= 0:
            print("invalid number of nights")
        else:
            total_price = selected_room[3] * nights
            print("Room Price:", selected_room[3], "$")
            print("Number Of Nights:", nights)
            print("Total Price:", total_price, "$")