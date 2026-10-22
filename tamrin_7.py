



factor_pish_ghaza=[]
factor_ghazay_asly=[]
factor_noshidani=[]
tedad_kol=[]
while True :
    menu_asly = input("\n\n---welcom to our resturant---\n"
                        "1.pish ghaza\n"
                        "2.ghazay asly\n"
                        "3.noshidani\n"
                        "4.exit\n"
                        "entekhabe shoma:")
    while True :
        match menu_asly :
            case "1" :
                menu_pish_ghaza=input("\n1.soup->100\n"
                                      "2.salad sezar->180\n"
                                      "3.sib zamini sorkh karde->120\n"
                                      "4.piaz halgheyi->140\n"
                                      "5.non sir->130\n"
                                      "6.bal morgh->220\n"
                                      "7.naget morgh->190\n"
                                      "8.panir mozarela sokhari->200\n"
                                      "9.role gosht->170\n"
                                      "10.homos->150\n"
                                      "11.exit\n"
                                      "entekhabe shoma:")
                match menu_pish_ghaza :
                    case "1" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_1 =tedad*1.1*100
                        factor_pish_ghaza.append(ghaymat_pish_1)
                        continue
                    case "2" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_2 =tedad *1.1*180
                        factor_pish_ghaza.append(ghaymat_pish_2)
                        continue
                    case "3" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_3 =tedad*1.1*120
                        factor_pish_ghaza.append(ghaymat_pish_3)
                        continue
                    case "4" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_4 =tedad*1.1*140
                        factor_pish_ghaza.append(ghaymat_pish_4)
                        continue
                    case "5" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_5 =tedad*1.1*130
                        factor_pish_ghaza.append(ghaymat_pish_5)
                        continue
                    case "6" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_6 =tedad*1.1*220
                        factor_pish_ghaza.append(ghaymat_pish_6)
                        continue
                    case "7" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_7 =tedad*1.1*190
                        factor_pish_ghaza.append(ghaymat_pish_7)
                    case "8" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_8 =tedad*1.1*200
                        factor_pish_ghaza.append(ghaymat_pish_8)
                    case "9" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_9 =tedad*1.1*170
                        factor_pish_ghaza.append(ghaymat_pish_9)
                    case "10" :
                        tedad =int(input("chand ta?"))
                        ghaymat_pish_10 =tedad*1.1*150
                        factor_pish_ghaza.append(ghaymat_pish_10)
                    case "11" :
                        print("factor pish ghazaye shoma:" ,factor_pish_ghaza)
                        break
                    case _:
                        print("ghozine eshtebah ast")
                        continue        
            case "2" :
                menu_ghaza_asly = input("\n---ghazaye asly---\n"
                                        "1.ghazaye chini\n"
                                        "2.ghazaye italiayi\n"
                                        "3.ghazaye irani\n"
                                        "4.exit\n")
                match menu_ghaza_asly :
                    case "1" :
                        menu_ghaza_chini =input("---ghazaye chini---"
                                                "\n1.bereng sorkh shode ba morgh->350\n"
                                                "2.nodel->320\n"
                                                "3.morgh kong paa->450\n"
                                                "4.morgh torsh o shirin-420\n"
                                                "5.ghosht o borocly->480\n"
                                                "6.khamir shekam por->300\n"
                                                "7.tofoy->380\n"
                                                "8.soup vanton->280\n"
                                                "9.morgh porteghaly->430\n"
                                                "10.ordak pekani->630\n"
                                                "11.exit\n"
                                                "entekhabe shoma:"
                                                ) 
                        match menu_ghaza_chini :
                            case "1":
                                tedad =int(input("chand ta?"))
                                ghaymat_asly_1 =tedad*1.1*350
                                factor_ghazay_asly.append(ghaymat_asly_1)
                                continue
                            case "2" :
                                tedad =int(input("chand ta?"))
                                ghaymat_asly_2 =tedad*1.1*320
                                factor_ghazay_asly.append(ghaymat_asly_2)
                                continue
                            case "3" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_3=tedad*1.1*450
                                factor_ghazay_asly.append(ghaymat_asly_3)
                                continue
                            case "4" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_4 =tedad*1.1*420
                                factor_ghazay_asly.append(ghaymat_asly_4)
                                continue
                            case "5" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_5=tedad*1.1*480
                                factor_ghazay_asly.append(ghaymat_asly_5)
                                continue
                            case "6" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_6=tedad*1.1*300
                                factor_ghazay_asly.append(ghaymat_asly_6)
                                continue 
                            case "7" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_7=tedad*1.1*380
                                factor_ghazay_asly.append(ghaymat_asly_7)
                                continue                            
                            case "8" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_8=tedad*1.1*280
                                factor_ghazay_asly.append(ghaymat_asly_8)
                                continue                            
                            case "9" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_9=tedad*1.1*430
                                factor_ghazay_asly.append(ghaymat_asly_9)
                                continue                            
                            case "10" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_10=tedad*1.1*630
                                factor_ghazay_asly.append(ghaymat_asly_10)
                                continue
                            case "11" :
                                break
                            case _:
                                print("ghozine eshtebah ast")
                                continue
                    case "2" :
                        menu_ghaza_italiayi =input("\n---ghazaye italiayi---\n"
                                                    "1.pitzza margarita->400\n"
                                                    "2.spageti->420\n"
                                                    "3.fotochini->450\n"
                                                    "4.lazania->480\n"
                                                    "5.rezotoy->390\n"
                                                    "6.raviloyi->410\n"
                                                    "7.pitzza panir->420\n"
                                                    "8.morgh parmezan->490\n"
                                                    "9.niuki->370\n"
                                                    "10.pene arrabita->360\n"
                                                    "11.exit\n"
                                                    )
                        match menu_ghaza_italiayi :
                            case "1" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_1=tedad*1.1*400
                                factor_ghazay_asly.append(ghaymat_asly_italia_1)
                                continue
                            case "2" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_2=tedad*1.1*420
                                factor_ghazay_asly.append(ghaymat_asly_italia_2)
                                continue
                            case "3" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_3=tedad*1.1*450
                                factor_ghazay_asly.append(ghaymat_asly_italia_3)
                                continue
                            case "4" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_4=tedad*1.1*480
                                factor_ghazay_asly.append(ghaymat_asly_italia_4)
                                continue
                            case "5" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_5=tedad*1.1*390
                                factor_ghazay_asly.append(ghaymat_asly_italia_5)
                                continue
                            case "6" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_6=tedad*1.1*410
                                factor_ghazay_asly.append(ghaymat_asly_italia_6)
                                continue
                            case "7" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_7=tedad*1.1*420
                                factor_ghazay_asly.append(ghaymat_asly_italia_7)
                                continue
                            case "8" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_8=tedad*1.1*490
                                factor_ghazay_asly.append(ghaymat_asly_italia_8)
                                continue
                            case "9" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_9=tedad*1.1*370
                                factor_ghazay_asly.append(ghaymat_asly_italia_9)
                                continue
                            case "10" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_italia_10=tedad*1.1*360
                                factor_ghazay_asly.append(ghaymat_asly_italia_10)
                                continue
                            case "11" :
                                break
                            case _ :
                                print("gozine eshtebah ast")
                                continue
                    case "3" :
                        menu_ghaza_irani = input("\n---ghazaye irani---\n"
                                                 "1.kabab kobide->450\n"
                                                 "2.jooje kabab->420\n"
                                                 "3.ghorme sabzi->380\n"
                                                 "4.fesenjan->450\n"
                                                 "5.gheime->350\n"
                                                 "6.zereshk polo bamorgh->400\n"
                                                 "7.tahchin->390\n"
                                                 "8.ghayme bademjoon->370\n"
                                                 "9.baghali polo ba mahiche->600\n"
                                                 "10.mirza ghasemi->300\n"
                                                 "11.exit"
                                                 )
                        match menu_ghaza_irani :

            
                            case "1" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_1=tedad*1.1*450
                                factor_ghazay_asly.append(ghaymat_asly_irani_1)
                                continue
                            case "2" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_2=tedad*1.1*420
                                factor_ghazay_asly.append(ghaymat_asly_irani_2)
                                continue
                            case "3" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_3=tedad*1.1*380
                                factor_ghazay_asly.append(ghaymat_asly_irani_3)
                                continue
                            case "4" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_4=tedad*1.1*450
                                factor_ghazay_asly.append(ghaymat_asly_irani_4)
                                continue
                            case "5" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_5=tedad*1.1*350
                                factor_ghazay_asly.append(ghaymat_asly_irani_5)
                                continue
                            case "6" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_6=tedad*1.1*400
                                factor_ghazay_asly.append(ghaymat_asly_irani_6)
                                continue
                            case "7" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_7=tedad*1.1*390
                                factor_ghazay_asly.append(ghaymat_asly_irani_7)
                                continue
                            case "8" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_8=tedad*1.1*370
                                factor_ghazay_asly.append(ghaymat_asly_irani_8)
                                continue
                            case "9" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_9=tedad*1.1*600
                                factor_ghazay_asly.append(ghaymat_asly_irani_9)
                                continue
                            case "10" :
                                tedad=int(input("chand ta?"))
                                ghaymat_asly_irani_10=tedad*1.1*300
                                factor_ghazay_asly.append(ghaymat_asly_irani_10)
                                continue
                            case "11" :
                                break
                            case _:

                                print("gozine eshtebah ast")
                                continue
            case "3" :
                menu_noshidani = input("\n---noshidani---\n"
                                       "1.abe porteghal->120\n"
                                       "2.limonad->100\n"
                                       "3.cocacola->80\n"
                                       "4.doogh->70\n"
                                       "5.chay->50\n"
                                       "6.ghahve->100\n"
                                       "7.copochino->180\n"
                                       "8.shayke tot farangi->190\n"
                                       "9.abe anbe->170\n"
                                       "10.abe gaz dar->60\n"
                                       "11.exit"
                                       "entekhabe shoma:"
                                       )
                match menu_noshidani :
                    case "1" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_1=tedad*1.1*120
                        factor_noshidani.append(ghaymat_noshidani_1)
                        continue
                    case "2" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_2=tedad*1.1*100
                        factor_noshidani.append(ghaymat_noshidani_2)
                        continue
                    case "3" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_3=tedad*1.1*80
                        factor_noshidani.append(ghaymat_noshidani_3)
                        continue
                    case "4" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_4=tedad*1.1*70
                        factor_noshidani.append(ghaymat_noshidani_4)
                        continue
                    case "5" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_5=tedad*1.1*50
                        factor_noshidani.append(ghaymat_noshidani_5)
                        continue
                    case "6" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_6=tedad*1.1*100
                        factor_noshidani.append(ghaymat_noshidani_6)
                        continue
                    case "7" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_7=tedad*1.1*180
                        factor_noshidani.append(ghaymat_noshidani_7)
                        continue
                    case "8" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_8=tedad*1.1*190
                        factor_noshidani.append(ghaymat_noshidani_8)
                        continue
                    case "9" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_9=tedad*1.1*170
                        factor_noshidani.append(ghaymat_noshidani_9)
                        continue
                    case "10" :
                        tedad =int(input("chand ta?"))
                        ghaymat_noshidani_10=tedad*1.1*60
                        factor_noshidani.append(ghaymat_noshidani_10)
                        continue
                    case "11" :
                        break
                    case _ :
                        print("gozine eshtebah ast")
                        continue
            case "4" :
                print("factor pish ghazaye shoma:" , sum(factor_pish_ghaza))
                print("factor ghazahaye shoma:" , sum(factor_ghazay_asly))
                print("factor noshidani shoma:" , sum(factor_noshidani))
                tedad_kol.append(factor_pish_ghaza)
                tedad_kol.append(factor_ghazay_asly)
                tedad_kol.append(factor_noshidani)
                print("tedad sefareshat shoma:" , len(tedad_kol))





