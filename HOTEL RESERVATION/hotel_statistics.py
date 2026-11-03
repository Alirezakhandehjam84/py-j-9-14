



from hotel_data import rooms, reservations

def hotel_statistics():
    total_rooms = len(rooms)
    reserved_rooms = 0
    available_rooms = 0
    total_income = 0
    for room in rooms:
        if room[4] == "Reserved":
            reserved_rooms += 1
        else:
            available_rooms += 1
    for reservation in reservations:
        total_income += reservation[6]
    if total_rooms > 0:
        occupancy = (reserved_rooms / total_rooms) * 100
    else:
        occupancy = 0
    print("----- HOTEL STATISTICS -----")
    print("Total Rooms:", total_rooms)
    print("Reserved Rooms:", reserved_rooms)
    print("Available Rooms:", available_rooms)
    print("Total Income:", total_income, "$")
    print("Occupancy Rate:", occupancy, "%")