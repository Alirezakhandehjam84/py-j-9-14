



while True :
    main_menu = input("1.kode meli 2.esm 3.famil 4.bimari 5.sabeghe bimari 6.telefon 7.adress 8.esme dr 9.exit :")
    while True :
        match main_menu :
            case "1" :
                kode_meli = input("kode meli ro bezan :")
                if kode_meli.isalnum()==True and len(kode_meli)==10 :
                    print("kode meli ok")
                else :
                    print("kode meli eshtebahe")
                    break
            case "2" :
                esm = input("esm khod ra vared konid :")
                if esm.isalpha()==True and len(esm)>=2 :
                    print("esm ok ")
                else :
                    print("esm not ok")
                    break
            case "3" :
                famili = input("famili ro bezan")
                if famili.isalpha()==True and len(famili)>=3 :
                    print("famili dorost ast")
                else :
                    print("fami;i eshtebahe")
                    break
            case "4" :
                bimari = input("che bimari dari? :")
                if bimari.isalpha()==True and len(bimari)>=3 :
                    print("in bimari voojod dare")
                else :
                    print("hamchin bimari voojod nadare")
                    break
            case "5" :
                sabeghe_bimari = input("sabeghe bimari khod ra vared konid :")
                if sabeghe_bimari.isalpha()==True and len(sabeghe_bimari)>=4 :
                    print("sabeghe bimari shoma sabt shod ")
                else :
                    print("sabt nashod")
                    break 
            case "6" :
                telefon = input("shomare telefon khod ra vared konid:")
                if telefon.isalnum()==True and len(telefon)==11 :
                    print("shomare ok")
                else :
                    print("shomare is invalid")
                    break
            case "7" :
                adress = input("adress ro vared kon :")
                if adress.isalnum()==True and len(adress)>10 :
                    print("adress ok ast")
                else :
                    print("adress eshtebahe")
                    break
            case "8" :
                esm_dr = input("esme doctor chist? :")
                if esm_dr.isalpha()==True and len(esm_dr)>=2:
                    print("doctor hast")
                else :
                    print("esme doctor eshtebahe")
                    break
            case _ :
                break