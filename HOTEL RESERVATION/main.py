



from showing_rooms import show_all_rooms
from availble_rooms import show_available_rooms
from reserve_room import reserve_room
from cancel_reservation import cancel_reservation
from search_reservation import search_reservation
from calculate_price import calculate_price
from showing_reservations import show_all_reservations
from hotel_statistics import hotel_statistics

while True:
    main_menu = input(
        "\n======= HOTEL RESERVATION =======\n"
        "1. Show All Rooms\n"
        "2. Show Available Rooms\n"
        "3. Reserve Room\n"
        "4. Cancel Reservation\n"
        "5. Search Reservation\n"
        "6. Calculate Price\n"
        "7. Show All Reservations\n"
        "8. Hotel Statistics\n"
        "9. Exit\n"
        "Choose: ")
    match main_menu:
        case "1":
            show_all_rooms()
        case "2":
            show_available_rooms()
        case "3":
            reserve_room()
        case "4":
            cancel_reservation()
        case "5":
            search_reservation()
        case "6":
            calculate_price()
        case "7":
            show_all_reservations()
        case "8":
            hotel_statistics()
        case "9":
            print("Thank you for using our hotel system!")
            break
        case _:
            print("invalid option")