







hadsha=[]
while True :
    menu_asly=input("\n---menu asly---\n"
                    "1.sabte hads\n"
                    "2.namayesh hads ha\n"
                    "3.namayesh tedad hads ha\n"
                    "4.namayesh bozorg tarin hads\n"
                    "5.pak kardan tamam hads ha\n"
                    "0.khoroj\n"
                    "entekhabe shoma:")
    while True :
        match menu_asly :
            case "1" :
                sabte_hads=int(input("hads khod ra vared konid:"))
                if sabte_hads in hadsha :
                    print("in adad ghablan sabt shode ast")
                    break
                else :
                    hadsha.append(sabte_hads)
                    print("hads sabt shod")
                    break
            case "2" :
                if len(hadsha)==0 :
                    print("hadsi vojod nadarad")
                    break
                else :
                    print("list hads haye shoma:" , hadsha)
                    break
            case "3" :
                if len(hadsha)==0 :
                    print("hadsi hanoz vojod nadarad")
                    break
                else :
                    print("tedad hads haye shoma:" , len(hadsha))
                    break
            case "4" :
                if len(hadsha) == 0:
                    print("hadsi vojod nadarad!")
                    break
                else:
                    largest = hadsha[0]
                    for guess in hadsha:
                        if guess > largest:
                            largest = guess
                print("bozorg tarin hads:", largest)
                break
            case "5" :
                if len(hadsha)==0 :
                    print("hadsi baraye pak kardan vojod nadarad")
                    break
                else :
                    hadsha.clear()
                    print("tamame hads ha pak shodand")
                    break
            case "6" :
                print("khoda negahdar")
                break
            case _ :
                print("gozine eshtebah ast")
                break
            