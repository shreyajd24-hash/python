password=input("enter password:")
username=input("enter username:")

if(password=="pass" and username=="admin"):
    print("succesful")
elif(password!="pass"):
    print("wrong password")
else:
    print("wrong username")