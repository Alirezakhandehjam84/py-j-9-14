



from hotel_data import rooms

def show_available_rooms():
    found = False
    for room in rooms:
        if room[4] == "Available":
            found = True
            print("Room:", room[0])
            print("Type:", room[1])
            print("Capacity:", room[2])
            print("Price:", room[3], "$")
            print("-------------------")
    if found == False:
        print("there is no available room")