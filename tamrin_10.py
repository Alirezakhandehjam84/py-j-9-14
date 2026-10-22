



while True :
    main_menu = input("1.esm 2.famili 3.sen 4.telefon 5.noe varzesh 6.exit :")
    while True :
        match main_menu :
            case "1" :
                esm = input("esmeto bezan:")
                if esm.isalpha()==True and len(esm)>=2 :
                    print("esm sabt shod")
                else :
                    print("esm eshtebahe")
                    break 
            case "2" :
                famili = input("familit chiye? :")
                if famili.isalpha()==True and len(famili)>=3 :
                    print("famili ok ")
                else :
                    print("famili eshtebah")
                    break
            case "3" :
                sen = input("seneto begoooo :")
                if sen.isalnum()==True and len(sen)<=2 and int(sen)>=10 :
                    print("sen ok")
                else :
                    print("sen not ok")
                    break
            case "4" :
                telefon = input("shomare khod ra vared konid")
                if telefon.isalnum()==True and len(telefon)==11 :
                    print("shomare doroste")
                else :
                    print("shomare not ok")
                    break 
            case "5" :
                noe_varzesh = input("che varzeshi mikhai? :")
                if noe_varzesh.isalpha()==True and len(noe_varzesh)>=4 :
                    print("varzesh sabt shod") 
                else :
                    print("sabt nashod")
                    break
            case _ :
                break