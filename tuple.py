#tuple concept as i known for
a=0
b=0
c=0
t=(1,2,3)

#type 1 unpacking
a,b,c=t
print(a,b,c)
print("\n")

#type 2 unpacking - I
t=(1,2,3,4)
a,*b,c=t
print(a,b,c)
print("\n")

#type 2 unpacking - II
d=0
t=(1,2,3,4,5)
a,*b,c,d=t
print(a,b,c,d)
print("\n")

#swapping, becoming a tuple and gets unpacked
a,b=b,a
print(a,b)
print("\n")

#packing and unpacking is also applies for List and Tuple
a,b=[b,a]
print(a,b)
