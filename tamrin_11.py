


balance=0
translation=[]
total_deposits = 0
while True :
    menu_asly=input("\n---bank---\n"
                    "1.variz pol\n"
                    "2.bardasht pol\n"
                    "3.namayesh mojodi\n"
                    "4.namayesh tarakonesh ha\n"
                    "5.namayesh majmoe varizi ha\n"
                    "0.khoroj\n"
                    "entekhab shoma:")
    while True :
        match menu_asly :
            case "1" :
                varizi=int(input("variz pol:"))
                if varizi>0 :
                    balance = balance + varizi
                    total_deposits=total_deposits +varizi
                    translation.append("varizi:" , str(varizi))
                    print("variz anjam shod")
                    break
                else :
                    print("adad vared shode bayad mosbat bashad")
            case "2" :
                bardashti = int(input("bardasht pol:"))
                if bardashti>0 :
                    if bardashti>=balance :
                        balance = balance - bardashti
                        translation.append("bardashti:" , str(bardashti))
                        print("bardasht anjam shod")
                        break
                    else :
                        print("mojodi kafi nist")
                        break
                else :
                    print("adad bardashti bayad mosbat bashad")
                    break
            case "3" :
                print("mojodi shoma:" , balance)
                break
            case "4" :
                if len(translation)>0 :
                    print("tarakonesh haye shoma:" , translation)
                    break
                else :
                    print("tarakonesh vojod nadarad")
                    break
            case "5" :
                print("Total deposits:", total_deposits)
                break
            case "0" :
                print("mamnoon ke as bank ma astefade kardid")
                break
            case _:
                print("gozine nadorost")
                break
            







