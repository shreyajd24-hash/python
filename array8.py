#array slicing

import array as arr 
data=arr.array('i',[5,6,8,89,66,30,668])
for i in data[::]:
    print(i)
    
for i in data[1::]:
    print(i)
    
for i in data[1:4]:
    print(i)
    
for i in data[4:1:-1]:
    print(i)