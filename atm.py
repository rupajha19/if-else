print("welcome to bank of india","insert your card")
card=input("choose your card type:/rupye/visa/credit/debit/")
if card=="rupye" or card=="visa" or card=="credit" or card=="debit":
    print("yes")
    language=(input("choose your language"))
    if language=="hindi" or language=="english":
        print("next")
        option=(input("select your prefer option:/withdrawl/check balance/change your pin"))
        if option=="withdrawl" or "check balance" or "change your pin":
            print("wait")
            pin=int(input("enter your pin"))
            
            if pin<9999:
                print("your pin has been matched")
                amount=int(input("enter your amount"))
                if amount <=500 and amount<10000:
                    print("your transaction has been successfully")
                    recipt=(input("would you like to take your recipt"))
                    if recipt=="yes" or "no":
                        print("collect your card")
                    else:
                        print("select yes or no ")
                else:
                    print("enter available amount in your account")
            else:
                print("please enter your correct pin")
        else:
            print("please choose your correct option") 
    else:
        print("please choose one language")
else:
    print("please choose any one card type")
