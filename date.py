year=int(input("enter year:"))
if year%400==0 and year%4==0:
    print(year)
else:
    pass
month=int(input("enter the month:"))
if month in (1,3,7,8,10,12):
    month_length=31
elif month==2:
    if year:
        month_length=29
    else:
        month_length=28
else:
    month_length=30

date=int(input("enter the date:"))
if date<month_length:
    date+=1
else:
    date=1
    if month==12:
        month=1
        year=year+1
    else:
        month=month+1
print("the next date is(yyy-mm-dd)",(year,month,date))












# year = int(input('Enter the year : '))
# month = int(input('Enter the month between 1 to 12 : '))
# date = int(input('Enter a date between 1 to 31 : '))

# # print((date+1),"/",month,"/",year)
# print(year,"/", month,"/",(date+1))





