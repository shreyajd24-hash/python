def outer(x,y):
    def inner():
        print("in inner function")
    print("in outer function")
    return x,y
    
retval=outer(10,20)
print(retval)
for i in retval:
    print(i)