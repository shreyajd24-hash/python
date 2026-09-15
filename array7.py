import array as arr 
data=arr.array('i',[4,5,6])
print(data)
print(data.buffer_info())
print(id(data))
print(data.count(6))
data.append(500)
print(data)
#data.extend(70,80,90)

newdata=arr.array('i',[100,200,300,400])
listdata=[10,20,30,40]
newdata.fromlist(listdata)
print(newdata)
print(newdata.index(100))
print(data)
data.pop()
print(data)

copylist=data.tolist()
print(copylist)

