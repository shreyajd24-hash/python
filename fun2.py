#check no. is divisible 5 abd 4
def div(x):
    if(x%5==0 & x%4==0):
        print("divisible")
    else:
        print("no")
    
x=int(input("enter x:"))
div(x)
