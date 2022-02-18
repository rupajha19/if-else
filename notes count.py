amount=int(input("enter amount::"))
note500=note200=note100=note50=note20=note10=note5=note1=0
if amount>=500:
    note500=amount//500
    amount=amount-note500*500
if amount>=200:
    note200=amount//200
    amount=amount-note200*200
if amount>=100:
    note100=amount//100
    amount=amount-note100*100
if amount>=50:
    note50=amount//50
    amount=amount-note50*50
if amount>=20:
    note20=amount//20
    amount=amount-note20*20
if amount>=10:
    note10=amount//10
    amount=amount-note10*10
if amount>=5:
    note5=amount//5
    amount=amount-note5*5
if amount>=1:
    note1=amount//1
    amount=amount-note1*1
print("500\t=\t",note500)
print("200\t=\t",note200)
print("100\t=\t",note100)
print("50\t=\t",note50)
print("20\t=\t",note20)
print("10\t=\t",note10)
print("5\t=\t",note5)
print("1    1\t=\t",note1)



