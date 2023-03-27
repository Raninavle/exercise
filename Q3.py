x=input("Enter the Userid:")
y=input("Enter the Passward:")
Userid=("Navlerani122")
Passward=("Rani*123")
if(x==Userid and y==Passward):
    print("Successfully login....please wait")
elif(x==Userid):
    print("Invalid Passward")  
elif(y==Passward):
    print("Invalid Userid")      
else:
    print("Invalid Userid and Passward....try again")

import random
x=random.randint(1000,9999)
print("please re-enter captcha:",x)

c=int(input("Enter the above 4 digit number:"))
if(c==x):
    print("sucessfully login..")
else:
    print("failed to login..")    
