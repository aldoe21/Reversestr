#code is based on str to list, again list to str and reverse and pop or remove

#this is str to list
s="francis"
a=list(s)
print("This is str to list")
print(a)
print(type(a))
print("\n")

#this is remove letter "n" from list and reverse and its type
print("This is remove 'n' from list")
a.remove("n")
print(a)
print(type(a))
print("\n")


#list to str and revrese and its type
print("This is list to str and reverse")
l=""
for i in a:
    l=l+i
    
print((l))
print(l[::-1])
print(type(l))
print("\n")


#for reverse str another format
print("This is reverse another format 'check code' ")
str=""
for i in s:
    str=i+str 

print(str)
print(type(str))
