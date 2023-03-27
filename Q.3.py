# sort the list according to the second element in sublist ?

data=[[0,1],[0,9,2],[2,3,4,7],[9,11,12]]
size=len(data)
for j in range(1,size):
    for i in range(0,size-j):
        if(data[i][1]>data[i+1][1]):
            data[i],data[i+1]=data[i+1],data[i]
print(data)

x=sorted(data)
print(x)
