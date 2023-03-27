# python program to merge two list and sort it?
list1=[]
list2=[]
n=int(input("Enter a length of list:"))
for i in range(1,n+1):
    e=int(input("Enter a element:"))
    list1.append(e)
print(list1)
n=int(input("Enter a length of list:"))
for i in range(1,n+1):
    e=int(input("Enter a element:"))
    list2.append(e)
print(list2)

data=list1+list2
print(data)
size=len(data)
for j in range(1,size):
    for i in range(0,size-j):
        if(data[i]>data[i+1]):
              data[i],data[i+1]=data[i+1],data[i]
print(data)





