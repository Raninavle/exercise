data=[40,8,50,10,30,34,8,6,14]
#print(data.sort())
#print("max:",max(data))
#print("min:",min(data))
max=data[-1]
min=data[0]
for i in range(1,len(data)):
    if(max<data[i]):
        max=data[i]
    if(min>data[i]):
        min=data[i]
print(max,min)

data=[10,20,20,78,78,10,78,89,20]
result=set(data)
print(result)
for i in result:
    print(i,":",data.count(i))


class Father(object):
    pass
class Child(Father):
    pass
# Driver Code
print(issubclass(Child,Father)) #True
print(issubclass(Father, Child)) #Fal