




nomre = float(input("nomre ro vared kon mashti:"))
if 20<nomre or nomre<0 :
    print("nomre ro eshteb zadi" , "🤦‍♂️")
elif 18<=nomre<=20 :
    if 19.5<=nomre<=20:
        print("ayval bab A++" , "👌")
    if 19<=nomre<19.5 :
        print("khayli khobe A+")
    if 18.5<=nomre<19 :
        print("khobe edame bede A-")
    if 18<=nomre<18.5 :
        print("talashet ro bishtar kon A--")
elif 16<=nomre<18 :
    if 17.5<=nomre<=18 :
        print("mitoni talashet ro bishtar koni B++")
    if 17<=nomre<17.5 :
        print("yekam bishtar B+")
    if 16.5<=nomre<17 :
        print("bad nisti B-")
    if 16<=nomre<16.5 :
        print("moragheb bash B--")
elif 12<=nomre<16 :
    if 15<=nomre<16 :
        print("khobe to in jayghah c++")
    if 14<=nomre<15 :
        print("bazam talashet ro bokon c+")
    if 13<=nomre<14 :
        print("c-")
    if 12<=nomre<13 :
        print("labe marzi c--")
elif 10<=nomre<12 :
    if 11<=nomre<12 :
        print("D++")
    if 10<=nomre<11 :
        print("D+")
else :
    print("dige oftadi begzar boro soragh chiz dige" , "🤣")
