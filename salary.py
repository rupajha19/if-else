salary=int(input("Enter salary......."))
year_of_service=int(input("enter year of service....."))
bonus=salary*(5/100)
if year_of_service>5:
  print ("Bonus is",bonus+salary)
else:
  print ("No bonus:", salary)


