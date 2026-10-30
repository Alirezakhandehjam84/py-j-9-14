



kala=[]
ghaymat=[]
while True :
    menu_sabad_kharid=input("\n---menu sabad kharid---\n"
                            "1.afzodan mahsol\n"
                            "2.namayesh sabad kharid\n"
                            "3.hazf mahsol\n"
                            "4.mohasebe tedad mahsolat\n"
                            "5.baresi vojod mahsol\n"
                            "0.khoroj\n"
                            "entekhabe shoma:")
    while True :
        match menu_sabad_kharid :
            case "1" :
                name_kala=input("name kala ra vared konid:")
                if name_kala in kala :
                    print("in kala as ghabl vojod darad")
                    break
                else :
                    ghaymat_kala=int(input("ghaymat kala ra vared konid:"))
                    if ghaymat_kala < 0 :
                        print("ghaymat bayad mosbat bashad")
                        break
                    else :
                        kala.append(name_kala)
                        ghaymat.append(ghaymat_kala)
                        print("ba moafaghiat sabt shod")
                        break
            case "2" :
                if len(kala)==0 :
                    print("sabad kharid khali ast")
                    break
                else :
                    ghaymat_kol = 0
                    for i in range(len(kala)) :
                        print(kala[i] , "-" , ghaymat[i])
                        ghaymat_kol = ghaymat_kol + ghaymat_kala[i]
                        print("ghymat tamam mahsolat sabad kharid:" , ghaymat_kol)
                        break
            case "3" :
                hazf=input("hazf kala as sabad kharid:")
                if hazf in kala :
                    index_kala=kala.index(hazf)
                    kala.remove(hazf)
                    ghaymat.pop(index_kala)
                    print("kala as sabad kharid hazf shod")
                    break
            case "4" :
                if len(kala)<0 :
                    print("sabad kharid khali ast")
                    break
                else :
                    print("tedad mahsolat sabad kharid:" , len(kala))
                    break
            case "5" :
                baresi=input("esm kalayi ke mikhahid check konid ra vared konid:")
                if baresi in kala :
                    print("kala vojod darad dar list shoma")
                    break
                else :
                    print("kala vojod nadarad dar list shoma")
                    break
            case "0" :
                print("bye bye")
                break
            case _:
                print("gozine eshtebah ast")
                break
            
