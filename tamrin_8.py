



while True :
    main_menu = input("1.esm 2.family 3.kode daneshjooi 4.sabtename dars 5.hazfe dars 6.exit : ")
    while True :
        match main_menu :
            case "1" :
                esm = input("esmeto bezan:")
                if esm.isalpha()==True and len(esm)>=3 :
                    print("esm ok")
                else:
                    print("esm eshtebahe")
                    break
            case "2" :
                famili = input("familit ro vared kon :")
                if famili.isalpha()==True and len(famili)>=4 :
                    print("famili shoma dorost vared shode")
                else :
                    print("famili eshtebahe")
                    break
            case "3" :
                kode_daneshjooi = input("kod ra vared kon:")
                if kode_daneshjooi.isalnum()==True and len(kode_daneshjooi)==8 :
                    print("kod ok")
                else :
                    print("kod not ok")
                    break
            case "4" :
                kod_dars = input("kod darsi ke mikhai bardari ri vared kon :")
                if kod_dars.isalnum()==True and len(kod_dars)==5 :
                    print("dars shoma sabt shod")
                else :
                    print("kod dars eshtebahe")
                    break
            case "5" :
                kod_dars = input("kod darsi ke mikhai hazf koni ro vared kon:")
                if kod_dars.isalnum()==True and len(kod_dars)==5 :
                    print("in dars hazf shod")
                else :
                    print("kod dars eshtebahe")
                    break
            case _ :
                break
                