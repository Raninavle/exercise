# python program to sort a list according to the length of the element within the sublist?

list=[[1,0,2],[11,56,1,4],[0,2,13,89,102,77],[7,6,19,98,23]]
size=len(list)
for i in range(1,size):
    for j in range(0,size-1):
        if(len(list[j])>len(list[j+1])):
            list[j],list[j+1]=list[j+1],list[j]
print(list)

#or
l=sorted(list,key=len)
print(l)
