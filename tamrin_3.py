



while True :
    hoghoogh = int(input("lotfan hoghoogh khod ra be milyon vared konid:"))

    if hoghoogh>200 or hoghoogh<5 :
        print("error")
        continue
    
    if 100<=hoghoogh<=200 :
        hoghoogh_ba_maliat = hoghoogh * 0.65
    elif 90<=hoghoogh<100 :
        hoghoogh_ba_maliat = hoghoogh * 0.8
    elif 70<=hoghoogh<90 :
        hoghoogh_ba_maliat = hoghoogh * 0.85
    elif 60<=hoghoogh<70 :
        hoghoogh_ba_maliat = hoghoogh * 0.90
    elif 50<=hoghoogh<60 :
        hoghoogh_ba_maliat = hoghoogh * 0.95
    elif 40<=hoghoogh<50 :
        hoghoogh_ba_maliat = hoghoogh * 0.97
    elif 30<=hoghoogh<40 :
        hoghoogh_ba_maliat = hoghoogh * 0.98
    
    else :
        print("moaf as maliat")
        continue
    print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
