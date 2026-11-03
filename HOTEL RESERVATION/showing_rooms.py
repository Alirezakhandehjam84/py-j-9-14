



from hotel_data import rooms

def show_all_rooms():
    print("----- ALL HOTEL ROOMS -----")
    for room in rooms:
        print("Room:", room[0])
        print("Type:", room[1])
        print("Capacity:", room[2], "Person")
        print("Price:", room[3], "$")
        print("Status:", room[4])
        print("---------------------------")