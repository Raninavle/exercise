# python program to put even and odd element of a list into two different list?
list=[]
n=int(input("Enter a length of list  :"))
for i in range(1,n+1):
    e=int(input("Enter a element :"))
    list.append(e)
print(list)
even=[]
odd=[]
for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even number list:",even)
print("Odd number list:",odd)