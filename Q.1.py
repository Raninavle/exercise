# sum of following series:
#   1!+2!+3!+4!+...n

def fact(n):
    f=1
    sum=0
    for i in range(1,n+1):
        f=f*i
        sum+=f
    return sum

x=int(input("Enter a number:"))
result=fact(x)
print(result)


