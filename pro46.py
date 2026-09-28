#Write a function that takes two integers a and b prints all even numbers between them (inclusive)
a=int(input("enter a:"))
b=int(input("enter b:"))
for i in range(a,b):
    if i%2==0:
        print(i)