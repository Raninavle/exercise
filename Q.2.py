
# write a program to check given number is armstrong or not:

def arm(t,s):
    if(t==0):
        if(num==s):
            print("number is armstrong")
            return s
        else:
            print("number is not armstrong")
            return s
    else:
        k=t%10
        s+=k**v
        t//=10
        return arm(t,s)
        
num=int(input("Enter a number:"))
v=len(str(num))
result=arm(num,0)


            

