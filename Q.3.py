# sum of all prime number betn 1 to n :

def prime(n):
    sum=0
    for i in range(2,n+1):
        for j in range(2,i):
            if(i%j==0):
              break
        else:
            print(i)
            sum+=i 
    return sum


x=int(input("Enter a number:"))
result=prime(x)
print("sum:",result)