x=input("Enter the Userid:")
y=input("Enter the passward: ")
Userid=("raninavle147@gmail.com")
Passward=("Rani@123")
if(x==Userid and y==Passward):
    print("Successfully login")
elif(x==Userid):
    print("Invalid Passward")
elif(y==Passward):
    print("Invalid Userid")   
else:
    print("Invalid Userid and Passward")


