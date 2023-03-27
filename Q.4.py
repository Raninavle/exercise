#find second largest number using bubble sort?


data=[70,75,80,96,12]
size=len(data)
max=data[0]
smax=0
for i in range(1,size):
    if(max<data[i]):
        smax=max
        max=data[i]
    elif(smax<data[i]):
        smax=data[i]
print(smax,max)
