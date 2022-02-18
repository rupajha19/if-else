# amount=int(input("enter total amount::"))
# discount=int(input("enter the dicount::"))
# discount=amount*(discount/100)
# if amount>10000:
#     print("payable amount::",amount-discount)
# else:
#     print(amount)




amount=int(input("enter total amount:"))
discount=amount*(10/100)
if amount>=10000:
    print(amount-discount)
else:
    print("no discpunt")


