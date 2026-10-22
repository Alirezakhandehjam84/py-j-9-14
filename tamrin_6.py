



while True :
    print("welcome")
    main_menu = input("1.login to your account 2.make a new account 3.enter the problem 4.exit :")
    while True :
        match main_menu :
            case "1" :
                print("so you alredy have an accont")
                user_name = input("please enter your user name :")
                password = input("now please enter yourpassword :")
                if user_name.isalnum()!=True or password.isalnum()!=True :
                    print("the format is not ok")
                    continue
                if len(user_name)<8 and len(password)<10 :
                    print("your username and your password is too short")
                elif len(user_name)<8 :
                    print("your user name is too short")
                elif len(password)<10 :
                    print("your password is too short")
                else :
                    print("your're loged in")
                break
            case "2" :
                user_name_1 = input("please enter a username :")
                if len(user_name_1)<8 or user_name_1.isalnum()!=True :
                    print("username is not correct")
                    continue
                password_1 = input("now please enter your password :")
                if len(password_1)<10 or password_1.isalnum()!=True :
                    print("password is not correct")
                    continue
                age = input("now please enter your age:")
                if age.isdigit() or age<18:
                    print("your age is not correct")
                    continue
                email = input("now please enter your email :")
                if email.endswith("@gmail.com")!=True :
                    print("your email is not correct")
                    continue
                address = input("now please enter your address :")
                if address.isalnum()!=True :
                    print("unvalid address")
                    continue
                phone = input("now please enter your phone number:")
                if phone.startswith("09")!= True or len(phone)!=11 :
                    print("invalid phone number")
                    continue
                car_company = input("now enter your car company :")
                if car_company.isalnum()!=True :
                    print("ther is not such company")
                    continue
                car_model = input("now please enter your car model :")
                if car_model.isalnum()!=True :
                    print("invalid car model")
                    continue
                year = input("please enter the year that your car made :")
                if year.startswith("20")!=True or year.startswith("13")!=True or year.startswith("14")!=True or year.isdigit()!=True:
                    print("invalid year")
                    break
                break
            case "3":
                while True:
                    problem_menu = input("1. Engine Repair 2. Transmission Repair 3. Body Repair 4. Oil Change 5. Tire Replacement 6. Exit")

                    match problem_menu:

                        case "1":
                            print("Engine Repair will cost you 10000")

                        case "2":
                            print("Transmission Repair will cost you 8000")

                        case "3":
                            print("Body repair depends on the level of car damage")

                        case "4":
                            while True:
                                oil_menu = input("1. Iranian Oil 2. Foreign Oil 3. Exit")

                                match oil_menu:
                                    case "1":
                                        print("Iranian Oil will cost 2000")

                                    case "2":
                                        print("Foreign Oil will cost 5000")

                                    case "3":
                                        break

                                    case _:
                                        print("Invalid option")

                        case "5":
                            while True:
                                tire_menu = input("1. Iranian Tire 2. Foreign Tire 3. Exit")

                                match tire_menu:
                                    case "1":
                                        print("Iranian Tire will cost 10000")

                                    case "2":
                                        print("Foreign Tire will cost 20000")

                                    case "3":
                                        break

                                    case _:
                                        print("Invalid option")

                        case "6":
                            break

                        case _:
                            print("Invalid option")
            case "4":
                break
            case _:
                print("invalid option")
                break
            
                        
                
                
                
                
        
                