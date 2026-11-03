



from add_contact import adding
from show_all_contacts import showing
from search_contact import searching
from edit_contact import editing
from delete_contact import deleting
from count_contacts import counting
while True:
    main_menu = input("\n--- PHONE CONTACT MANAGER ---\n"
        "1. Add Contact\n"
        "2. Show Contacts\n"
        "3. Search Contact\n"
        "4. Edit Contact\n"
        "5. Delete Contact\n"
        "6. Count Contacts\n"
        "7. Exit\n"
        "Enter your choice: ")
    match main_menu:
        case "1":
            adding()
        case "2":
            showing()
        case "3":
            searching()
        case "4":
            editing()
        case "5":
            deleting()
        case "6":
            counting()
        case "7":
            print("Goodbye!")
            break
        case _:
            print("Invalid option! Please try again.")
            continue