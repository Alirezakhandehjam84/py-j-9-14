



notes = []

while True:
    menu_asly=input("\n--- Notes Menu ---\n"
                    "1. Add a note\n"
                    "2. Show all notes\n"
                    "3. Edit a note\n"
                    "4. Delete a note\n"
                    "5. Search notes\n"
                    "0. Exit\n"
                    "entekhabe shoma: ")
    match menu_asly:
        case "1":
            note = input("Enter your note: ")
            notes.append(note)
            print("Note added successfully!")
        case "2":
            if len(notes) == 0:
                print("No notes found!")
            else:
                for i in range(len(notes)):
                    print(i + 1, "-", notes[i])
        case "3":
            if len(notes) == 0:
                print("No notes to edit!")
            else:
                for i in range(len(notes)):
                    print(i + 1, "-", notes[i])
                note_number = int(input("Enter note number to edit: "))
                if 1 <= note_number <= len(notes):
                    new_note = input("Enter the new note: ")
                    notes[note_number - 1] = new_note
                    print("Note edited successfully!")
                else:
                    print("Invalid note number!")
        case "4":
            if len(notes) == 0:
                print("No notes to delete!")
            else:
                for i in range(len(notes)):
                    print(i + 1, "-", notes[i])
                note_number = int(input("Enter note number to delete: "))
                if 1 <= note_number <= len(notes):
                    notes.pop(note_number - 1)
                    print("Note deleted successfully!")
                else:
                    print("Invalid note number!")
        case "5":
            search_word = input("Enter a word to search: ")
            found = False
            for note in notes:
                if search_word in note:
                    print(note)
                    found = True
            if found == False:
                print("No matching notes found!")
        case "6":
            print("Goodbye!")
            break
        case _:
            print("Invalid option!")