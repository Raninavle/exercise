num=896
x=num%10
y=num//10
z=y%10
w=y//10
sum=x+z+w
print("sum:",sum)
#or
num=int(input("Enter a number:"))
sum=0
while (num!=0):
    x=num%10
    sum+=x
    num=num//10
print(sum)
