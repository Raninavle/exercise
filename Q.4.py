# fibonacci series:

def fibo(n):
    a=1
    b=0
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c  
    return 

n=int(input("Enter a number:"))
result=fibo(n)
print(result)
