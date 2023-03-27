# sum of all number betn 1 to n :

def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

x=int(input("Enter a number:"))
result=sum(x)
print(result)