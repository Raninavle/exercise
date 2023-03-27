# for fact recursive function:
def fact(num):
    if(num==0):
        return 1
    else:
     return num*fact(num-1)

sum=0 
n=int(input("Enter a number:"))
for i in range(1,n+1):
    sum+=fact(i)

print("sum of factorial:",sum)



# for sum, recursive function:
def sumofdigit(n):
    if(n==0):
        return 0
    else:
        return n+sumofdigit(n-1)

num=int(input("Enter a number:"))
result=sumofdigit(num)
print("sum",result)