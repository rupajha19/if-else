# People 5 years and above in age can go to school.

# People 18 years and above in age can vote in elections.

# People 21 years and above in age can drive a car.

# People 24 years and above in age can marry.

# People 25 years and above in age can legally drink.

child=int(input("enter child age"))
if child==5 or child>5:
    print("child can go school")
    voter=int(input("enter voting age"))
    if voter==18 or voter>18:
        print("voter can vote in election")
        drink=int(input("enter drinking age"))
        if drink==25 or drink>25:
            print("drinker can drink legally")
            drive=int(input("enter age"))
            if drive==24:
                print("you can drive car")
                age=int(input("enter marry age"))
                if age==24:

                    print("you can marry")
                else:
                    print("you cannot marry")
            else:
                print("you can not drive")
        else:
            print("you can not drink")
    else:
        print("you can not vote in election")
else:
    print("child can not go school")
