def outer():
    def inner():
        print("in inner function")
    print("in outer function")
    inner()
    
print("start code")
outer()
print("end")