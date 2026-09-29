



while True :
    user_name = input("please enter your user name :")
    password = input("now please enter your password :")
    if len (user_name) < 8 and len (password) < 10 :
        print("user name va password shoma monaseb nist dobare talash konid")
        continue
    if len (user_name)< 8 :
        print ("your user name is not long enough")
        continue
    if len (password)< 10 :
        print("your password is not strong enough")
        continue
    age = int(input("now please enter your age :"))
    if age > 100 or age < 0 :
        print("sen shoma sahih nemibashad")
        continue
    if age < 16 :
        print("zire sen mojaz")
    if 16<=age<=100 :
        print("login")
    break




    