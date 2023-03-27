
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter Number:"))
print(fact(n))
print("-----------------------------------------")
def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
n=int(input("Enter Number:"))
print(sum(n))
print("-----------------------------------------")
def sumofdigit(n):
    if(n==0):
        return 0
    else:
        return n%10+sumofdigit(n//10)

n=int(input("Enter Number:"))
print(sumofdigit(n))
print("-----------------------------------------")

def fibo(a,b,n):
    if(n==0):
        return 
    else:
        c=a+b
        print(c,end=" ")
    return fibo(b,c,n-1)
       
n=int(input("Enter Number:"))
print(fibo(1,0,n))
print("-----------------------------------------")

def reverseofnumber(n,r):
    if(n==0):
        return r
    else:
        r=r*10+n%10
        n//=10
        return reverseofnumber(n,r)
n=int(input("Enter Number:"))
print(reverseofnumber(n,0))