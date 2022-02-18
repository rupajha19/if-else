cost_prise=int(input("buying prise::"))
sell_prise=int(input("enter selling prise::"))
if sell_prise>cost_prise:
    amount=sell_prise-cost_prise
    print("thr profit is::",amount)
elif cost_prise>sell_prise:
    amount=cost_prise-sell_prise
    print("the loss is::",amount)
else:
    print("no profit")







# c_p=int(input("enter the cost prise"))
# s_p=int(input("enter the selling prise"))
# if c_p>s_p:
#     print("profit",c_p-s_p)
# elif c_p<s_p:
#     print("loss",c_p-s_p)
# else:
#     print("nothing")



