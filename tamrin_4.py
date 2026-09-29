


while True :
    nomre = float(input("please enter your grade:"))
    if nomre<0 or nomre>20 :
        print("incorrect grade please enter again")
        continue
    if 17<=nomre<=20 :
        if 17<=nomre<18 :
            print("your grade is :A")
        if 18<=nomre<19 :
            print("your grade is :A+")
        if 19<=nomre<=20 :
            print("your grade is :A++")
    if 14<=nomre<17 :
        if 14<=nomre<15 :
            print("your grade is :B")
        if 15<=nomre<16 :
            print("your grade is :B+")
        if 16<=nomre<17 :
            print("your grade is :B++")
    if 11<=nomre<14 :
        if 11<=nomre<12 :
            print("your grade is :C")
        if 12<=nomre<13 :
            print("your grade is :C+")
        if 13<=nomre<14 :
            print("your grade is :C++")
    if 8<=nomre<11 :
        if 8<=nomre<9 :
            print("your grade is :D")
        if 9<=nomre<10 :
            print("your grade is :D+")
        if 10<=nomre<11 :
            print("your grade is :D++")
    else :
        print("you failed :f--")
    break