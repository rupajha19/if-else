# If water in the filter is less than 1L then more water needs to be filled. If the water quantity
#  is between 1L and 10L then there is no need to fill water. If water is more than 10L then the 
#  water will overflow. Based on these conditions, complete the flowchart given below.


water=int(input("enter water ltr::"))
if water<1:
    print("more water need to fill")
elif water<=10: 
    print("no need to fill tank")
elif water>10:
    print("water will overflow")
else:
    print("if we need water we,ll call")
