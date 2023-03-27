#print 1 to 100 in snake and ladder pattern?

for i in range(10,0,-1):#10,9,8,7,6,5,4,3,2,1
    x=10*i# 100,90,80,70,60,50,40,30,20,10
    data=[]
    for j in range(0,10):#0,1,2,3,4,5,6,7,8,9
        data.append(x-j)#100, 99, 98, 97, 96, 95, 94, 93, 92, 91
                        #90, 89, 88, 87, 86, 85, 84, 83, 82, 81

    
    
    if(i%2!=0):
        data.reverse()
    for y in data:
        print(y,end=" ")
    print()