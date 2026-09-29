



while True :
    hoghoogh = int(input("lotfan hoghoogh khod ra be milyon vared konid:"))
    if hoghoogh>200 or hoghoogh<5 :
        print("error")
        continue
    if 100<=hoghoogh<=200 :
        hoghoogh_ba_maliat = hoghoogh * 0.65
        print(hoghoogh_ba_maliat)
    if 90<=hoghoogh<100 :
        hoghoogh_ba_maliat = hoghoogh * 0.8
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 70<=hoghoogh<90 :
        hoghoogh_ba_maliat = hoghoogh * 0.85
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 60<=hoghoogh<70 :
        hoghoogh_ba_maliat = hoghoogh * 0.90
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 50<=hoghoogh<60 :
        hoghoogh_ba_maliat = hoghoogh * 0.95
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 40<=hoghoogh<50 :
        hoghoogh_ba_maliat = hoghoogh * 0.97
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 30<=hoghoogh<40 :
        hoghoogh_ba_maliat = hoghoogh * 0.98
        print("hoghoogh shoma ba mohasebe maliat:" , hoghoogh_ba_maliat)
    if 5<=hoghoogh<30 :
        print("moaf as maliat")
    break