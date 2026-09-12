def values(x,y,z):
    x+=10
    y+=10
    z+=10
    return x,y,z
val1=int(input("enter val1:"))
val2=int(input("enter val2:"))
val3=int(input("enter val3:"))
retval=values(val1,val2,val3)
for i in retval:
    print(i)
