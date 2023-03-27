# python program to find the intersection of two list?
list1=[]
list2=[]
n=int(input("Enter a length of list:"))
for i in range(1,n+1):
    e=int(input("Enter a element:"))
    list1.append(e)

n=int(input("Enter a length of list:"))
for i in range(1,n+1):
    e=int(input("Enter a element:"))
    list2.append(e)
print( "list1=",list1)
print("list2=",list2)
intersection=[]
for x in list1:
    for y in list2:
        if(x==y):
            intersection.append(x)
print(intersection)
