# If this number is less than 10 then print "10 se chota hai". If it is greater than 10 
# and lesser than 20 then print "20 se chota hai". Else if it is greater than 20 then print 
# "20 se bada hai". Complete the flowchart as per the above instructions.


num=int(input("enter number::"))
if num<10:
    print("10 se chota hai")
elif num<200:
    print("20 se chota hai")
else:
    print("error")
if num>20:
    print("20 se bada hai")
    