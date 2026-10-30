



ketab=[]
while True :
    menu_ketabkhane =input("\n---menu ketabkhane---\n"
                           "1.afzodan ketab\n"
                           "2.namayesh ketab ha\n"
                            "3.jost o jo dar ketab ha\n"
                            "4.tedad ketab ha\n"
                            "5.pak kardan hameye ketab ha\n"
                            "0.khoroj\n"
                            "entekhabe shoma:")
    while True :
        match menu_ketabkhane :
            case "1" :
                name_ketab=input("esm ketab ra vared konid:")
                if name_ketab in ketab :
                    print("in ketab ghablan sabt shode ast")
                    break
                else :
                    ketab.append(name_ketab)
                    print("ketab azafe shod")
                    break
            case "2" :
                if len(ketab)==0 :
                    print("ketabi vojod nadarad")
                    break
                else :
                    print("list ketab ha:" , ketab)
                    break
            case "3" :
                jost_o_jo=input("esm ketab ra vared konid:")
                if jost_o_jo in ketab :
                    print("ketab peyda shod")
                    break
                else :
                    print("ketab yaft nashod")
                    break
            case "4" :
                if len(ketab)==0 :
                    print("ketabi vojod nadarad")
                    break
                else :
                    print("tedad ketab ha:" , len(ketab))
                    break
            case "5" :
                ketab.clear()
                print("tamam ketab ha hazf shodand")
                break
            case "0" :
                print("khoda hafez 🖐")