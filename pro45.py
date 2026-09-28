#calculate factorial
n=int(input("enter a n:"))

def fact():
    fac=1
    for i in range(1,n+1):
        fac*=i
    print(fac)
fact()
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)