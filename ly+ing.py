a=input("enter any character::")
if "ly" in a:
    print(a[0:-2]+"ing")
elif "ing" in a:
    print(a[0:-3]+ "ly")
else:
    print("do once again")
    