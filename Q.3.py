def rev(n,r):
    if(n==0):
        return r
    else:
        r=r*10+n%10
        n//=10
        return rev(n,r)

num=int(input("Enter a number:"))
result=rev(num,0)
print("result:",result)
