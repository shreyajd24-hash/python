age=int(input("enter:"))
assert age>0, " age is negative"
if age>18:
    print("eligible")
else:
    print("not eligible")