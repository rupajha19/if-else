number=int(input("enter number: "))
a=number%10
b=(number//10)%10
c=(number//100)%10
d=(number//1000)%10
new_number=(a*1000)+(b*100)+(c*10)+(d*1)
if number>1000:
    print(new_number)
else:
    print("wrong")

