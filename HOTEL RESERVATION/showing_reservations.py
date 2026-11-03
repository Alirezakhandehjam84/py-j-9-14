



from hotel_data import reservations

def show_all_reservations():
    if len(reservations) == 0:
        print("there is no reservation")
    else:
        for reservation in reservations:
            print("Reservation ID:", reservation[0])
            print("Customer Name:", reservation[1])
            print("Phone:", reservation[2])
            print("Room Number:", reservation[3])
            print("Number Of People:", reservation[4])
            print("Number Of Nights:", reservation[5])
            print("Total Price:", reservation[6], "$")
            print("---------------------------")